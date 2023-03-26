import logging

from aiogram import Bot, Dispatcher, executor  # type: ignore
from handlers.user import register_handlers


def create_bot() -> Dispatcher:
    API_TOKEN = "5898637870:AAHcm8TsaycPaxLEXrOg-v1F5x5RZRbG08M"

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    return dp


if __name__ == "__main__":
    dp = create_bot()
    register_handlers(dp)
    executor.start_polling(dp)

