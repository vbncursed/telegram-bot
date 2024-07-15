from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import PurchaseStates

from keyboards.keyboard import Keyboard
from messages import welcome_message, go_buy_vpn_message, vpn_choose_period_message


async def handle_back(callback_query: CallbackQuery, state: FSMContext) -> None:
    current_state: str = await state.get_state()

    if current_state == PurchaseStates.go_buy_vpn:
        keyboard: Keyboard = Keyboard().get_keyboard("go_buy_vpn", "about")
        await callback_query.message.answer(
            text=welcome_message(user_name=callback_query.from_user.full_name),
            reply_markup=keyboard,
        )
        await state.set_state(PurchaseStates.main_menu)

    elif current_state == PurchaseStates.vpn_choose_period:
        keyboard: Keyboard = Keyboard().get_keyboard("continue", "back")
        await callback_query.message.answer(
            text=go_buy_vpn_message(), reply_markup=keyboard
        )
        await state.set_state(PurchaseStates.go_buy_vpn)

    elif current_state in (
        PurchaseStates.one_month,
        PurchaseStates.three_month,
        PurchaseStates.six_month,
        PurchaseStates.twelve_month,
    ):
        keyboard: Keyboard = Keyboard().get_keyboard(
            "one_month", "three_month", "six_month", "twelve_month", "back"
        )

        await callback_query.message.answer(
            text=vpn_choose_period_message(), reply_markup=keyboard
        )
        await state.set_state(PurchaseStates.vpn_choose_period)

    elif current_state == PurchaseStates.payment_page:
        keyboard: Keyboard = Keyboard().get_keyboard(
            "one_month", "three_month", "six_month", "twelve_month", "back"
        )

        await callback_query.message.answer(
            text=vpn_choose_period_message(), reply_markup=keyboard
        )
        await state.set_state(PurchaseStates.vpn_choose_period)

    elif current_state == PurchaseStates.payment_completed:
        keyboard: Keyboard = Keyboard().get_keyboard("go_buy_vpn", "about")
        await callback_query.message.answer(
            text=welcome_message(user_name=callback_query.from_user.full_name),
            reply_markup=keyboard,
        )
        await state.set_state(PurchaseStates.main_menu)
