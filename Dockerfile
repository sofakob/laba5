# Используйте официальный образ Python как базовый
FROM python:3.8-slim

# Установите рабочий каталог в контейнере
WORKDIR /app

# Скопируйте файлы приложения и тестов в контейнер
COPY . .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запустите тесты (предполагается, что у вас есть файл test.py)
CMD ["python", "laba5Test.py"]