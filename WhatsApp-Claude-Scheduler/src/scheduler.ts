import cron from 'node-cron';
import { jobsDb, ScheduledJob } from './db';
import { sendMessage } from './openwa';

// Holds active cron tasks keyed by job ID
const activeTasks = new Map<string, cron.ScheduledTask>();

async function fireJob(job: ScheduledJob): Promise<void> {
  try {
    await sendMessage(job.recipient, job.message);
    jobsDb.markSent(job.id);
    console.log(`[scheduler] Sent job ${job.id} to ${job.recipient}`);
  } catch (err) {
    console.error(`[scheduler] Failed to send job ${job.id}:`, err);
  }
}

export function scheduleJob(job: ScheduledJob): void {
  if (job.cron_expression) {
    const task = cron.schedule(job.cron_expression, () => fireJob(job));
    activeTasks.set(job.id, task);
    return;
  }

  if (job.scheduled_time) {
    const fireAt = new Date(job.scheduled_time).getTime();
    const delay = fireAt - Date.now();
    if (delay <= 0) {
      // Missed — fire immediately then mark sent
      fireJob(job);
      return;
    }
    const timer = setTimeout(() => {
      fireJob(job);
      activeTasks.delete(job.id);
    }, delay);
    // Store as a fake ScheduledTask so we can cancel it uniformly
    activeTasks.set(job.id, {
      stop: () => clearTimeout(timer),
    } as unknown as cron.ScheduledTask);
  }
}

export function cancelJob(jobId: string): boolean {
  const task = activeTasks.get(jobId);
  if (task) {
    task.stop();
    activeTasks.delete(jobId);
  }
  return jobsDb.cancel(jobId);
}

export function loadPersistedJobs(): void {
  const pending = jobsDb.listPending();
  for (const job of pending) {
    scheduleJob(job);
  }
  console.log(`[scheduler] Loaded ${pending.length} persisted job(s)`);
}
