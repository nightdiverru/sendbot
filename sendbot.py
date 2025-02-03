import os
import json
import asyncio
from datetime import datetime
from telegram import Bot, InputFile

# Загружаем настройки из файла settings.json
def load_settings():
    try:
        with open('settings.json', 'r', encoding='utf-8') as file:
            settings = json.load(file)
        return settings
    except Exception as e:
        print(f"Ошибка при загрузке настроек: {e}")
        return None

# Замените на ваш токен и ID чата
TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'  # ID чата, куда бот будет отправлять сообщения

# Загрузка настроек
settings = load_settings()
if not settings:
    exit("Не удалось загрузить настройки. Проверьте файл settings.json.")

# Функция для логирования
def log_message(message):
    now = datetime.now()
    log_filename = now.strftime("%Y-%m-%d") + "-sendbot.log"  # Формат имени файла: nowdate-sendbot.log
    log_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # Формат времени для записи в лог
    with open(log_filename, 'a', encoding='utf-8') as log_file:
        log_file.write(f"[{log_timestamp}] {message}\n")
    print(f"[{log_timestamp}] {message}")  # Также выводим в консоль для удобства

# Асинхронная функция для отправки сообщения и картинки
async def send_message_and_image():
    try:
        # Чтение сообщения из файла
        message_path = os.path.join(settings['folder_path'], settings['message_file'])
        if not os.path.exists(message_path):
            log_message(f"Файл {message_path} не найден.")
            return

        with open(message_path, 'r', encoding='utf-8') as file:
            message_text = file.read()

        # Чтение картинки
        image_path = os.path.join(settings['folder_path'], settings['image_file'])
        if not os.path.exists(image_path):
            log_message(f"Файл {image_path} не найден.")
            return

        with open(image_path, 'rb') as image_file:
            image = InputFile(image_file)

        # Отправка сообщения и картинки
        bot = Bot(token=TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message_text)
        await bot.send_photo(chat_id=CHAT_ID, photo=image)
        log_message("Сообщение и картинка успешно отправлены.")

    except Exception as e:
        log_message(f"Ошибка при отправке сообщения: {e}")

# Асинхронная функция для планирования задачи
async def schedule_task():
    if settings['send_day'] == 0:
        # Если send_day = 0, отправляем каждые send_hour часов и send_minute минут
        while True:
            await send_message_and_image()
            await asyncio.sleep(settings['send_hour'] * 3600 + settings['send_minute'] * 60)
    else:
        # Иначе отправляем в указанный день месяца
        while True:
            now = datetime.now()
            if now.day == settings['send_day'] and now.hour == settings['send_hour'] and now.minute == settings['send_minute']:
                await send_message_and_image()
                # Ждем до следующего месяца
                await asyncio.sleep(30 * 24 * 3600)  # Примерно 30 дней
            else:
                # Проверяем каждую минуту
                await asyncio.sleep(60)

# Основная асинхронная функция
async def main():
    log_message("Бот запущен.")
    await schedule_task()

# Запуск асинхронного цикла
if __name__ == "__main__":
    asyncio.run(main())
