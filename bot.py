import asyncio
import os

from telegram import Bot
from telegram.error import RetryAfter
from telegram.request import HTTPXRequest


TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

TOTAL_QUESTIONS = 155
DELAY = 2

OPTION_EMOJIS = ["🔴", "🔵", "🟢", "🟡"]


async def send_message(bot, text):
    while True:
        try:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=text
            )
            return

        except RetryAfter as error:
            wait_time = error.retry_after

            print(
                f"Flood control detected. "
                f"Waiting {wait_time} seconds..."
            )

            await asyncio.sleep(wait_time)


async def main():

    if not TOKEN or not CHANNEL_ID:
        raise ValueError(
            "BOT_TOKEN or CHANNEL_ID is not set"
        )

    request = HTTPXRequest(
        read_timeout=60,
        write_timeout=60,
        connect_timeout=60,
        pool_timeout=10,
    )

    bot = Bot(
        token=TOKEN,
        request=request,
    )

    print("Starting...")
    print(f"Questions: {TOTAL_QUESTIONS}")
    print(f"Delay: {DELAY} seconds")

    for question in range(1, TOTAL_QUESTIONS + 1):

        # Question
        await send_message(
            bot,
            f"📝 سؤال {question}:"
        )

        await asyncio.sleep(DELAY)

        # Options
        for option in range(1, 5):

            await send_message(
                bot,
                f"{OPTION_EMOJIS[option - 1]} گزینه {option}"
            )

            await asyncio.sleep(DELAY)

        print(f"Question {question} completed.")

    print("All messages sent successfully.")


if __name__ == "__main__":
    asyncio.run(main())
