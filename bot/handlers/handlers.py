from aiogram import Router
from aiogram.types import CallbackQuery, InputFile
from aiogram.fsm.context import FSMContext
from states.states import PurchaseStates

from keyboards.keyboard import Keyboard
from handlers.handler_back import handle_back
from handlers.handler_continue import handle_continue
from messages import (
    welcome_message,
    vpn_info_message,
    go_buy_vpn_message,
)
from handlers.handlers_payment import (
    handle_vpn_choose_period,
    handle_one_month,
    handle_three_month,
    handle_six_month,
    handle_twelve_month,
    handle_payment,
    handle_payment_completed,
)

router: Router = Router()


@router.callback_query()
async def handle_callback(callback_query: CallbackQuery, state: FSMContext) -> None:
    data: str = callback_query.data
    await callback_query.message.delete()  # Удаление старого сообщения

    action_map: dict[str, callable] = {
        "main": handle_main_menu,
        "about": handle_about,
        "go_buy_vpn": handle_go_buy_vpn,
        "vpn_choose_period": handle_vpn_choose_period,
        "one_month": handle_one_month,
        "three_month": handle_three_month,
        "six_month": handle_six_month,
        "twelve_month": handle_twelve_month,
        "back": handle_back,
        "continue": handle_continue,
        "payment_page": handle_payment,
        "paid": handle_payment_completed,
        "from_payment": handle_from_payment,
    }

    await action_map[data](callback_query, state)


async def handle_main_menu(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("go_buy_vpn", "about")
    user_name: str = callback_query.from_user.full_name

    await state.set_state(PurchaseStates.main_menu)
    await callback_query.message.answer(
        text=welcome_message(user_name=user_name),
        reply_markup=keyboard,
    )


async def handle_about(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("to_main")

    await state.set_state(PurchaseStates.vpn_info)
    await callback_query.message.answer(text=vpn_info_message(), reply_markup=keyboard)


async def handle_go_buy_vpn(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("continue", "back")
    video_path = "../video.mp4"
    video = InputFile(video_path)

    await state.set_state(PurchaseStates.go_buy_vpn)
    await callback_query.message.answer_video(
        video, caption=go_buy_vpn_message(), reply_markup=keyboard
    )


async def handle_from_payment(callback_query: CallbackQuery, state: FSMContext) -> None:
    await handle_main_menu(callback_query, state)
