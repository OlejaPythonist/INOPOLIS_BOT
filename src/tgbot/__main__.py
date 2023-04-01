import logging
import os

from aiogram import Bot, Dispatcher, executor  # type: ignore
from bot.handlers.user import register_handlers


def create_bot() -> Dispatcher:
    API_TOKEN = os.environ["BOT_TOKEN"]

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    return dp


if __name__ == "__main__":
    dp = create_bot()
    register_handlers(dp)
    executor.start_polling(dp)

