import Database from 'better-sqlite3';
import path from 'path';
import { randomUUID } from 'crypto';
import fs from 'fs';

const dataDir = path.join(__dirname, '../data');
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

const db = new Database(path.join(dataDir, 'scheduler.db'));

db.exec(`
  CREATE TABLE IF NOT EXISTS scheduled_jobs (
    id TEXT PRIMARY KEY,
    recipient TEXT NOT NULL,
    message TEXT NOT NULL,
    scheduled_time TEXT,
    cron_expression TEXT,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
  );

  CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    phone_number TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
  );

  CREATE TABLE IF NOT EXISTS conversation_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
  );
`);

export interface ScheduledJob {
  id: string;
  recipient: string;
  message: string;
  scheduled_time: string | null;
  cron_expression: string | null;
  description: string;
  status: string;
  created_at: string;
}

export interface Contact {
  name: string;
  phone_number: string;
}

export const jobsDb = {
  create(job: Omit<ScheduledJob, 'id' | 'status' | 'created_at'>): ScheduledJob {
    const id = randomUUID();
    db.prepare(`
      INSERT INTO scheduled_jobs (id, recipient, message, scheduled_time, cron_expression, description)
      VALUES (?, ?, ?, ?, ?, ?)
    `).run(id, job.recipient, job.message, job.scheduled_time ?? null, job.cron_expression ?? null, job.description);
    return db.prepare('SELECT * FROM scheduled_jobs WHERE id = ?').get(id) as ScheduledJob;
  },

  listPending(): ScheduledJob[] {
    return db.prepare("SELECT * FROM scheduled_jobs WHERE status = 'pending' ORDER BY created_at DESC").all() as ScheduledJob[];
  },

  cancel(id: string): boolean {
    const result = db.prepare("UPDATE scheduled_jobs SET status = 'cancelled' WHERE id = ? AND status = 'pending'").run(id);
    return result.changes > 0;
  },

  markSent(id: string): void {
    db.prepare("UPDATE scheduled_jobs SET status = 'sent' WHERE id = ?").run(id);
  },
};

export const contactsDb = {
  upsert(name: string, phoneNumber: string): void {
    db.prepare('INSERT OR REPLACE INTO contacts (name, phone_number) VALUES (?, ?)').run(name.toLowerCase(), phoneNumber);
  },

  find(name: string): Contact | undefined {
    return db.prepare('SELECT * FROM contacts WHERE name = ?').get(name.toLowerCase()) as Contact | undefined;
  },

  list(): Contact[] {
    return db.prepare('SELECT * FROM contacts ORDER BY name').all() as Contact[];
  },
};

export const conversationDb = {
  add(sender: string, role: 'user' | 'assistant', content: string): void {
    db.prepare('INSERT INTO conversation_history (sender, role, content) VALUES (?, ?, ?)').run(sender, role, content);
    // Keep only the last 20 messages per sender to avoid unbounded growth
    db.prepare(`
      DELETE FROM conversation_history
      WHERE sender = ? AND id NOT IN (
        SELECT id FROM conversation_history WHERE sender = ? ORDER BY id DESC LIMIT 20
      )
    `).run(sender, sender);
  },

  getHistory(sender: string): { role: 'user' | 'assistant'; content: string }[] {
    return db.prepare(
      'SELECT role, content FROM conversation_history WHERE sender = ? ORDER BY id ASC'
    ).all(sender) as { role: 'user' | 'assistant'; content: string }[];
  },
};
