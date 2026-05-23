import axios from 'axios';

const client = axios.create({
  baseURL: process.env.OPENWA_URL || 'http://localhost:2785',
  headers: {
    'X-API-Key': process.env.OPENWA_API_KEY || '',
    'Content-Type': 'application/json',
  },
  timeout: 10_000,
});

function toChatId(recipient: string): string {
  // Accept +1234567890, 1234567890, or already-formatted 1234567890@c.us
  if (recipient.includes('@')) return recipient;
  return `${recipient.replace(/^\+/, '')}@c.us`;
}

export async function sendMessage(recipient: string, message: string): Promise<void> {
  const sessionId = process.env.OPENWA_SESSION_ID || 'default';
  await client.post(`/api/sessions/${sessionId}/messages/send-text`, {
    chatId: toChatId(recipient),
    text: message,
  });
}

export async function getSessions(): Promise<{ id: string; status: string }[]> {
  const response = await client.get('/api/sessions');
  return response.data;
}
