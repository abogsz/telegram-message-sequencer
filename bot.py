import asyncio
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

TOTAL_QUESTIONS = 155
DELAY = 1


async def main():
    if not TOKEN or not CHANNEL_ID:
        raise ValueError("BOT_TOKEN or CHANNEL_ID is not set in .env")

    bot = Bot(token=TOKEN)

    for question in range(1, TOTAL_QUESTIONS + 1):

        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"سوال {question}"
        )

        await asyncio.sleep(DELAY)

        for option in range(1, 5):

            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=f"گزینه {option}"
            )

            await asyncio.sleep(DELAY)

    print("ارسال تمام شد.")


if __name__ == "__main__":
    asyncio.run(main())
