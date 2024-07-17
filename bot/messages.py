from dotenv import load_dotenv
from os import getenv

load_dotenv()
CARD_NUMBER = getenv("CARD_NUMBER")
CREATOR_ID = getenv("CREATOR_ID")
CREATOR_TAG = getenv("CREATOR_TAG")
EXCEPTION_IDS = getenv("EXCEPTION_IDS")


def welcome_message(user_name) -> str:
    return f"Добро пожаловать, <b>{user_name}!</b>\nЯ помогу тебе обезопасить свою интернет-активность и обеспечить конфиденциальность.\nГотов начать?"


def vpn_info_message() -> str:
    return (
        "С VPN ты сможешь:\n1. Обходить географические ограничения и получать доступ к контенту из любой точки мира.\n2. Защищать свои данные от хакеров и наблюдения.\n3. Анонимно и безопасно пользоваться общественными Wi-Fi сетями.\nИ многое другое!"
        ""
    )


def go_buy_vpn_message() -> str:
    return "Инструкция. Приложение Streisand есть на ios/macos.\n1. Копируем ссылку которая придет после оплаты.\n2. Заходим в приложение Streisand.\n3. Нажимаем на плюсик справа сверху и вставить из буфера обмена.\n4. Разрешаем вставку, и большую синюю кнопку.\n5. Далее разрешаем добавить новую VPN конфигурацию, и вводим пароль от телефона(этот этап обязателен с любым VPN)"


def vpn_choose_period_message() -> str:
    return "Выбери период подписки VPN, который ты хочешь купить."


def one_month_message(telegram_id: int) -> str:
    if str(telegram_id) in EXCEPTION_IDS:
        return "450 рублей – стоимость подписки на один месяц."
    else:
        return "150 рублей – стоимость подписки на один месяц."


def three_month_message(telegram_id: int) -> str:
    if str(telegram_id) in EXCEPTION_IDS:
        return "1275 рублей – стомость подписки на три месяца."
    else:
        return "425 рублей – стомость подписки на три месяца."


def six_month_message(telegram_id: int) -> str:
    if str(telegram_id) in EXCEPTION_IDS:
        return "2400 рублей – стоимость подписки на шесть месяцев."
    else:
        return "800 рублей – стоимость подписки на шесть месяцев."


def twelve_month_message(telegram_id: int) -> str:
    if str(telegram_id) in EXCEPTION_IDS:
        return "4500 рублей – стоимость подписки на один год."
    else:
        return "1500 рублей – стоимость подписки на один год."


def payment_page_message() -> str:
    return f'Для оплаты подписки переведите деньги по номеру карты: Т-банк: <code>{CARD_NUMBER}</code> , Эдуард К.\n\nВ данный момент онлайн оплата еще не настроена, она находится в разработке, вы можете написать главному администратору бота {CREATOR_TAG}, прислать ему чек оплаты и он выдаст вам конфиг для подключения VPN. Также после того как нажмете кнопку "Оплатил" вас перенесет в чат с главным администратором'


def paid_message() -> str:
    return "Вы успешно оплатили подписку, вы можете начать пользоваться VPN."


def author_contact() -> str:
    return "Если у вас есть вопросы, пожалуйста, свяжитесь с нашим создателем: {CREATOR_TAG}"
