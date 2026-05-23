import 'dotenv/config';
import express from 'express';
import { webhookRouter } from './webhook';
import { loadPersistedJobs } from './scheduler';

const app = express();
app.use(express.json());

app.use('/webhook', webhookRouter);

app.get('/health', (_req, res) => res.json({ status: 'ok' }));

const PORT = parseInt(process.env.PORT || '3000', 10);

app.listen(PORT, () => {
  console.log(`[server] Listening on port ${PORT}`);
  loadPersistedJobs();
});
