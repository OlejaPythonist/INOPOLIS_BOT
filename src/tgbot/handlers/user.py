import asyncio
from typing import Callable, Iterator
from aiogram import Dispatcher  # type: ignore
from aiogram import types
from tgbot.keyboards.user import commands_keyboard
from tgbot.parsing.parse_info import (
    get_bachelor_text,
    get_master_text,
    get_postgraduate_text,
    parse
)


async def start(message: types.Message) -> None:
    photo = open("images/UNI_photo.jpg", "rb")
    name = message.from_user.username
    await message.answer_photo(
        photo,
        caption=f"Привет, {name}, это бот команды ENIGMA",
        reply_markup=commands_keyboard
    )  # текст нужно придумать


async def help(message: types.Message) -> None:
    await message.reply(
        "Привет)",
        reply_markup=commands_keyboard
    )  # текст нужно придумать


async def answer(
        call: types.CallbackQuery,
        url: str,
        get_info: Callable[[str], Iterator[tuple[str, str]]]) -> None:
    await call.message.answer("ПОИСК ИНФОРМАЦИИ НАЧАЛСЯ")

    try:
        texts = await parse(url, get_info)
    except asyncio.TimeoutError as ex:
        await call.message.answer("С сайтом неполадки. Попробуйте снова позже")
        raise ex
    except Exception as ex:
        await call.message.answer("Что-то пошло не так...")
        raise ex

    if not texts:
        await call.message.answer("Информация не найдена")

    for text in texts:
        await call.message.answer(text)


async def bachelor(call: types.CallbackQuery) -> None:
    url = "https://apply.innopolis.university/bachelor/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    await answer(call, url, get_bachelor_text)


async def master(call: types.CallbackQuery) -> None:
    url = "https://apply.innopolis.university/master/datascience/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    await answer(call, url, get_master_text)


async def postgraduate(call: types.CallbackQuery) -> None:
    url = "https://apply.innopolis.university/postgraduate-study/"\
          "?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
    await answer(call, url, get_postgraduate_text)


async def trash(message: types.Message) -> None:
    await message.answer(
        "Вы ввели неправильную комманду.\nУзнать условия поступления:",
        reply_markup=commands_keyboard
    )


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start,
        commands=["start"]
    )
    dp.register_message_handler(
        help,
        commands=["help"]
    )
    dp.register_message_handler(trash)
    dp.register_callback_query_handler(
        bachelor,
        lambda c: c.data == "bachelor"
    )
    dp.register_callback_query_handler(
        master,
        lambda c: c.data == "master"
    )
    dp.register_callback_query_handler(
        postgraduate,
        lambda c: c.data == "postgraduate"
    )
