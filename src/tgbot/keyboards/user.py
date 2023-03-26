from aiogram.types import (  # type: ignore
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


commands_keyboard = InlineKeyboardMarkup()

bachelor = InlineKeyboardButton(
    "Бакалавриат",
    callback_data="bachelor"
)
master = InlineKeyboardButton(
    "Магистратура",
    callback_data="master"
)
postgraduate = InlineKeyboardButton(
    "Аспирантура",
    callback_data="postgraduate"
)

commands_keyboard.add(bachelor, master, postgraduate)
