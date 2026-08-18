# Telegram Question Publisher

Simple Python script for automatically sending numbered questions and 4 options to a Telegram channel.

## Setup

```bash
pip install -r requirements.txt
````

Create `.env`:

```env
BOT_TOKEN=your_bot_token
CHANNEL_ID=@your_channel
```

Configure `TOTAL_QUESTIONS` and `DELAY` in `bot.py`.

Make sure the bot is an admin of the channel.

## Run

```bash
python bot.py
```

