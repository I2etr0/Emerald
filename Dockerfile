# Базовый образ Python
FROM python:latest

# Устанавливаем зависимости системы (если нужны)
RUN apt update && \
    apt install -y vim curl wget

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt и устанавливаем зависимости
COPY requirements.txt .

# Копируем файлы проекта
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт, на котором работает приложение (например, 8000)
# EXPOSE 8000
# TODO: открыть SSH порт

# Запускаем Python-скрипт
CMD ["python", "bot.py"]