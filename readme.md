# Проект @bot

## Описание
Проект @bot представляет собой Python-приложение, использующее виртуальное окружение и различные зависимости для выполнения своих задач. В проекте используется библиотека `python-dotenv` для загрузки конфигурации из `.env` файла.

## Установка

### Клонирование репозитория
```bash
git clone https://github.com/vbncursed/telegram_bot.git
cd bot
```

### Создание и активация виртуального окружения
#### На Windows
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### На MacOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

## Конфигурация
Создайте файл `.env` в корневом каталоге проекта и добавьте необходимые переменные окружения. Пример:
```plaintext:.env
DOMAIN=example.org
ADMIN_EMAIL=admin@example.org
ROOT_URL=${DOMAIN}/app
```

## Запуск приложения
После настройки окружения и установки зависимостей, вы можете запустить приложение:
```bash
python main.py
```

## Структура проекта
- `bot/` - основной код приложения
- `venv/` - виртуальное окружение
- `bot/requirements.txt` - список зависимостей
- `bot/.env` - файл конфигурации окружения
- `.gitignore` - файл для исключения из контроля версий

## Лицензия
Этот проект лицензирован под лицензией MIT. Подробности см. в файле LICENSE.

## Авторы
- [Eduard](https://github.com/vbncursed)