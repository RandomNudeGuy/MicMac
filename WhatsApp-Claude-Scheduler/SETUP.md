# WhatsApp Claude Scheduler — Setup Guide

## Prerequisites
- Node.js 18+ (you have this)
- Docker Desktop (you have this)
- A secondary WhatsApp number to link

---

## Step 1 — Get a Claude API Key

1. Go to https://console.anthropic.com
2. Sign up / log in
3. Click **API Keys** → **Create Key**
4. Copy the key (starts with `sk-ant-...`) — you only see it once

---

## Step 2 — Configure environment

```bash
cd WhatsApp-Claude-Scheduler
cp .env.example .env
```

Open `.env` and fill in:
- `ANTHROPIC_API_KEY` — the key from Step 1
- `OPENWA_API_KEY` — pick any random string (e.g. `mySecretKey123`)
- `WEBHOOK_SECRET` — pick any random string (e.g. `webhookSecret456`)

The `OPENWA_API_KEY` and `WEBHOOK_SECRET` values just need to match between `.env` and `docker-compose.yml` — you're setting them, they don't come from anywhere external.

---

## Step 3 — Install dependencies

```bash
npm install
```

---

## Step 4 — Start OpenWA

```bash
docker compose up -d
```

Wait ~30 seconds for it to start, then open:
**http://localhost:2785/api/docs** — you should see the Swagger UI.

---

## Step 5 — Link your WhatsApp number

1. Open the OpenWA dashboard or call the sessions API:
   ```bash
   curl -X POST http://localhost:2785/api/sessions \
     -H "X-API-Key: mySecretKey123" \
     -H "Content-Type: application/json" \
     -d '{"id": "default"}'
   ```
2. A QR code will appear in the OpenWA logs or dashboard
3. On your phone: WhatsApp → **Linked Devices** → **Link a Device** → scan the QR

Your WhatsApp is now linked. OpenWA will maintain the session across restarts.

---

## Step 6 — Start the middleware server

```bash
npm run dev
```

You should see:
```
[server] Listening on port 3000
[scheduler] Loaded 0 persisted job(s)
```

---

## Step 7 — Test it

Send a WhatsApp message **to your linked number** from your main phone:

> "Schedule a message to +447911123456 saying 'call me back' tomorrow at 10am"

You'll get a reply from the bot confirming the schedule.

---

## Example commands you can send

| What you say | What happens |
|---|---|
| `Schedule a message to +12025551234 saying "Happy birthday!" on June 5th at 9am` | One-time scheduled message |
| `Every Monday at 8am send the group +447900000000 "Good morning team"` | Recurring message |
| `Show me my scheduled messages` | Lists pending jobs |
| `Cancel job abc12345` | Cancels that job |
| `Add contact Sarah +447911123456` | Saves Sarah's number |
| `Message Sarah: dinner at 7?` | Sends immediately using saved contact |

---

## Running in the background (optional)

Install `pm2` to keep the server running even after closing Terminal:

```bash
npm install -g pm2
npm run build
pm2 start dist/index.js --name whatsapp-bot
pm2 save
pm2 startup   # follow the printed command to auto-start on login
```

---

## Stopping everything

```bash
# Stop the middleware
pm2 stop whatsapp-bot   # if using pm2
# or just Ctrl+C in the terminal

# Stop OpenWA
docker compose down
```
