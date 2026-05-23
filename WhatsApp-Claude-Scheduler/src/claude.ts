import Anthropic from '@anthropic-ai/sdk';
import { jobsDb, contactsDb, conversationDb } from './db';
import { scheduleJob, cancelJob } from './scheduler';
import { sendMessage } from './openwa';

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const SYSTEM_PROMPT = `You are a WhatsApp assistant that helps the user send and schedule WhatsApp messages.
The current date and time is: ${new Date().toISOString()}

You have tools to:
- Send a message immediately
- Schedule a one-time message for a future date/time
- Schedule a recurring message using a cron expression
- List all scheduled messages
- Cancel a scheduled message
- Save contacts (name → phone number) so the user can refer to people by name
- List saved contacts

When the user mentions a person by name, look up their number in contacts first.
Phone numbers should always be in international format: +[country code][number] (e.g. +447911123456).
For scheduled_time, always use ISO 8601 format (e.g. 2025-06-01T14:30:00).
For cron_expression, use standard 5-field cron syntax (minute hour day month weekday).
Be friendly and confirm what you scheduled in plain language.`;

const tools: Anthropic.Tool[] = [
  {
    name: 'send_now',
    description: 'Send a WhatsApp message immediately.',
    input_schema: {
      type: 'object' as const,
      properties: {
        recipient: { type: 'string', description: 'Phone number in international format e.g. +447911123456' },
        message: { type: 'string', description: 'Message text to send' },
      },
      required: ['recipient', 'message'],
    },
  },
  {
    name: 'schedule_message',
    description: 'Schedule a WhatsApp message for a future time, or on a recurring cron schedule. Provide either scheduled_time (one-off) or cron_expression (recurring), not both.',
    input_schema: {
      type: 'object' as const,
      properties: {
        recipient: { type: 'string', description: 'Phone number in international format e.g. +447911123456' },
        message: { type: 'string', description: 'Message text to send' },
        scheduled_time: { type: 'string', description: 'ISO 8601 datetime for one-time delivery e.g. 2025-06-01T14:30:00' },
        cron_expression: { type: 'string', description: 'Cron expression for recurring delivery e.g. "0 9 * * 1" = every Monday 9am' },
        description: { type: 'string', description: 'Short human-readable label for this job' },
      },
      required: ['recipient', 'message', 'description'],
    },
  },
  {
    name: 'list_scheduled_messages',
    description: 'List all pending scheduled messages.',
    input_schema: { type: 'object' as const, properties: {} },
  },
  {
    name: 'cancel_scheduled_message',
    description: 'Cancel a pending scheduled message by its ID.',
    input_schema: {
      type: 'object' as const,
      properties: {
        job_id: { type: 'string', description: 'The UUID of the job to cancel' },
      },
      required: ['job_id'],
    },
  },
  {
    name: 'add_contact',
    description: 'Save a contact name mapped to a phone number for future use.',
    input_schema: {
      type: 'object' as const,
      properties: {
        name: { type: 'string', description: 'Contact name' },
        phone_number: { type: 'string', description: 'International phone number e.g. +447911123456' },
      },
      required: ['name', 'phone_number'],
    },
  },
  {
    name: 'list_contacts',
    description: 'List all saved contacts.',
    input_schema: { type: 'object' as const, properties: {} },
  },
];

type ToolInput = Record<string, string>;

async function executeTool(name: string, input: ToolInput): Promise<string> {
  switch (name) {
    case 'send_now': {
      await sendMessage(input.recipient, input.message);
      return `Message sent to ${input.recipient}.`;
    }

    case 'schedule_message': {
      const job = jobsDb.create({
        recipient: input.recipient,
        message: input.message,
        scheduled_time: input.scheduled_time ?? null,
        cron_expression: input.cron_expression ?? null,
        description: input.description,
      });
      scheduleJob(job);
      return `Scheduled (ID: ${job.id}): "${job.description}" → ${job.scheduled_time || job.cron_expression}`;
    }

    case 'list_scheduled_messages': {
      const jobs = jobsDb.listPending();
      if (jobs.length === 0) return 'No pending scheduled messages.';
      return jobs.map(j =>
        `• [${j.id.slice(0, 8)}] ${j.description} — to: ${j.recipient} at ${j.scheduled_time || j.cron_expression}`
      ).join('\n');
    }

    case 'cancel_scheduled_message': {
      const cancelled = cancelJob(input.job_id);
      return cancelled ? `Job ${input.job_id} cancelled.` : `No pending job found with that ID.`;
    }

    case 'add_contact': {
      contactsDb.upsert(input.name, input.phone_number);
      return `Saved ${input.name} → ${input.phone_number}`;
    }

    case 'list_contacts': {
      const contacts = contactsDb.list();
      if (contacts.length === 0) return 'No contacts saved.';
      return contacts.map(c => `• ${c.name}: ${c.phone_number}`).join('\n');
    }

    default:
      return `Unknown tool: ${name}`;
  }
}

export async function processMessage(sender: string, userText: string): Promise<string> {
  // Resolve contact name if user said something like "message John"
  const resolvedText = userText.replace(/\b([A-Z][a-z]+)\b/g, (match) => {
    const contact = contactsDb.find(match.toLowerCase());
    return contact ? `${match} (${contact.phone_number})` : match;
  });

  conversationDb.add(sender, 'user', resolvedText);

  const messages: Anthropic.MessageParam[] = conversationDb.getHistory(sender).map(h => ({
    role: h.role,
    content: h.content,
  }));

  let response = await anthropic.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 1024,
    system: SYSTEM_PROMPT,
    tools,
    messages,
  });

  // Agentic tool-use loop
  while (response.stop_reason === 'tool_use') {
    const toolUseBlocks = response.content.filter(
      (b): b is Anthropic.ToolUseBlock => b.type === 'tool_use'
    );

    const toolResults: Anthropic.ToolResultBlockParam[] = [];
    for (const block of toolUseBlocks) {
      const result = await executeTool(block.name, block.input as ToolInput);
      console.log(`[claude] tool=${block.name} result="${result}"`);
      toolResults.push({ type: 'tool_result', tool_use_id: block.id, content: result });
    }

    // Add assistant turn + tool results and continue
    messages.push({ role: 'assistant', content: response.content });
    messages.push({ role: 'user', content: toolResults });

    response = await anthropic.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 1024,
      system: SYSTEM_PROMPT,
      tools,
      messages,
    });
  }

  const replyText = response.content
    .filter((b): b is Anthropic.TextBlock => b.type === 'text')
    .map(b => b.text)
    .join('');

  conversationDb.add(sender, 'assistant', replyText);
  return replyText;
}
