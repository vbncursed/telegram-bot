from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import PurchaseStates

from keyboards.keyboard import Keyboard
from messages import (
    vpn_choose_period_message,
    one_month_message,
    three_month_message,
    six_month_message,
    twelve_month_message,
    payment_page_message,
    paid_message,
    author_contact,
)

from os import getenv
from dotenv import load_dotenv

load_dotenv()
CREATOR_ID = getenv("CREATOR_ID")


async def handle_vpn_choose_period(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard(
        "one_month", "three_month", "six_month", "twelve_month", "back"
    )

    await state.set_state(PurchaseStates.vpn_choose_period)
    await callback_query.message.answer(
        text=vpn_choose_period_message(), reply_markup=keyboard
    )


async def handle_one_month(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("payment_page", "back")

    await state.set_state(PurchaseStates.one_month)
    await callback_query.message.answer(
        text=one_month_message(telegram_id=callback_query.message.chat.id),
        reply_markup=keyboard,
    )


async def handle_three_month(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("payment_page", "back")

    await state.set_state(PurchaseStates.three_month)
    await callback_query.message.answer(
        text=three_month_message(telegram_id=callback_query.message.chat.id),
        reply_markup=keyboard,
    )


async def handle_six_month(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("payment_page", "back")

    await state.set_state(PurchaseStates.six_month)
    await callback_query.message.answer(
        text=six_month_message(telegram_id=callback_query.message.chat.id),
        reply_markup=keyboard,
    )


async def handle_twelve_month(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("payment_page", "back")

    await state.set_state(PurchaseStates.twelve_month)
    await callback_query.message.answer(
        text=twelve_month_message(telegram_id=callback_query.message.chat.id),
        reply_markup=keyboard,
    )


async def handle_payment(callback_query: CallbackQuery, state: FSMContext) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("paid_btn", "back")

    await state.set_state(PurchaseStates.payment_page)
    await callback_query.message.answer(
        text=payment_page_message(), reply_markup=keyboard
    )


async def handle_payment_completed(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    keyboard: Keyboard = Keyboard().get_keyboard("from_payment")

    await state.set_state(PurchaseStates.payment_completed)
    await callback_query.message.answer(text=paid_message(), reply_markup=keyboard)

    await callback_query.message.answer(text=author_contact())
