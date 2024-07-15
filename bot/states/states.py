from aiogram.fsm.state import StatesGroup, State


class PurchaseStates(StatesGroup):
    main_menu = State()  # Главное меню
    vpn_info = State()  # Информация о VPN
    go_buy_vpn = State()  # Покупка VPN
    vpn_choose_period = State()  # Выбор периода подписки
    one_month = State()  # Один месяц подписки
    three_month = State()  # Три месяца подписки
    six_month = State()  # Шесть месяцев подписки
    twelve_month = State()  # Двенадцать месяцев подписки
    payment_page = State()  # Страница с реквезитами
    payment_completed = State()  # Страница успешного платежа
