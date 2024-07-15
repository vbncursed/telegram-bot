import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from messages import welcome_message
from keyboards.keyboard import Keyboard
from states.states import PurchaseStates
from handlers.handlers import router as handler_router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
CREATOR_ID = getenv("CREATOR_ID")

dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with `/start` command
    """
    try:
        user_name: str = message.from_user.full_name
        keyboard: Keyboard = Keyboard().get_keyboard("go_buy_vpn", "about")
        chat_id: int = CREATOR_ID

        await state.set_state(PurchaseStates.main_menu)
        await message.answer(
            welcome_message(user_name=user_name),
            reply_markup=keyboard,
        )
        await message.bot.send_message(
            chat_id=chat_id,
            text=f"Пользователь: <b>{user_name}</b>\nID: <code>{message.from_user.id}</code>\nTag: <code>@{message.from_user.username}</code> @{message.from_user.username}\nНачал взаимодействие с ботом.",
        )
    except Exception as e:
        print(e)


async def main() -> None:
    bot: Bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Регистрация роутера для обработки нажатий кнопок
    dp.include_router(handler_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
