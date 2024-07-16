# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r bot/requirements.txt

# Копируем файл .env в контейнер
COPY bot/.env /app/bot/.env

# Запускаем бота
CMD ["python", "bot/bot.py"]