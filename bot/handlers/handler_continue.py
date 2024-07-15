from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import PurchaseStates

from keyboards.keyboard import Keyboard
from messages import vpn_choose_period_message


async def handle_continue(callback_query: CallbackQuery, state: FSMContext) -> None:
    current_state: str = await state.get_state()
    if current_state == PurchaseStates.go_buy_vpn:
        keyboard: Keyboard = Keyboard().get_keyboard(
            "one_month", "three_month", "six_month", "twelve_month", "back"
        )

        await state.set_state(PurchaseStates.vpn_choose_period)
        await callback_query.message.answer(
            vpn_choose_period_message(), reply_markup=keyboard
        )
