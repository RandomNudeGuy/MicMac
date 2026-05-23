import { Router, Request, Response } from 'express';
import crypto from 'crypto';
import { processMessage } from './claude';
import { sendMessage } from './openwa';

export const webhookRouter = Router();

function verifySignature(req: Request): boolean {
  const secret = process.env.WEBHOOK_SECRET;
  if (!secret) return true; // Skip verification if no secret configured

  const signature = req.headers['x-webhook-signature'] as string | undefined;
  if (!signature) return false;

  const expected = crypto
    .createHmac('sha256', secret)
    .update(JSON.stringify(req.body))
    .digest('hex');

  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
}

webhookRouter.post('/', async (req: Request, res: Response): Promise<void> => {
  if (!verifySignature(req)) {
    res.status(401).json({ error: 'Invalid signature' });
    return;
  }

  // Acknowledge immediately so OpenWA doesn't retry
  res.status(200).json({ ok: true });

  const { event, data } = req.body as {
    event: string;
    data: {
      from?: string;
      body?: string;
      type?: string;
      isGroupMsg?: boolean;
    };
  };

  if (event !== 'message.received') return;
  if (!data?.body || !data?.from) return;
  if (data.type !== 'chat') return; // text messages only

  const sender = data.from;
  const text = data.body.trim();

  console.log(`[webhook] Message from ${sender}: ${text}`);

  try {
    const reply = await processMessage(sender, text);
    if (reply) await sendMessage(sender, reply);
  } catch (err) {
    console.error('[webhook] Error processing message:', err);
    await sendMessage(sender, 'Sorry, something went wrong. Please try again.');
  }
});
