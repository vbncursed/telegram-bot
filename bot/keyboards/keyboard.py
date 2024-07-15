from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Keyboard:
    def __init__(self):
        self.buttons = {
            "go_buy_vpn": InlineKeyboardButton(
                text="Перейти к покупке vpn!", callback_data="go_buy_vpn"
            ),
            "about": InlineKeyboardButton(text="Подробнее", callback_data="about"),
            "to_main": InlineKeyboardButton(
                text="Спасибо, понял", callback_data="main"
            ),
            "back": InlineKeyboardButton(text="Назад", callback_data="back"),
            "continue": InlineKeyboardButton(
                text="Продолжить", callback_data="continue"
            ),
            "one_month": InlineKeyboardButton(text="Месяц", callback_data="one_month"),
            "three_month": InlineKeyboardButton(
                text="Три месяца", callback_data="three_month"
            ),
            "six_month": InlineKeyboardButton(
                text="Шесть месяцев", callback_data="six_month"
            ),
            "twelve_month": InlineKeyboardButton(
                text="Один год", callback_data="twelve_month"
            ),
            "payment_page": InlineKeyboardButton(
                text="Купить", callback_data="payment_page"
            ),
            "paid_btn": InlineKeyboardButton(text="Оплатил", callback_data="paid"),
            "from_payment": InlineKeyboardButton(
                text="На главную", callback_data="from_payment"
            ),
        }

    def get_keyboard(self, *button_names) -> InlineKeyboardMarkup:
        buttons = [self.buttons[name] for name in button_names]

        # Группировка кнопок в ряды
        rows = []
        if (
            "one_month" in button_names
            and "three_month" in button_names
            and "six_month" in button_names
            and "twelve_month" in button_names
            and "back" in button_names
        ):
            rows.append([self.buttons["one_month"], self.buttons["three_month"]])
            rows.append([self.buttons["six_month"], self.buttons["twelve_month"]])
            rows.append([self.buttons["back"]])
        else:
            rows.append(buttons)

        return InlineKeyboardMarkup(inline_keyboard=rows)
