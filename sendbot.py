import os
import json
import asyncio
from datetime import datetime
from telegram import Bot, InputFile
from telegram.error import TelegramError

# Load settings
def load_settings():
    try:
        with open('settings.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Config error: {str(e)}")
        return None

# Async logger
async def log_message(msg):
    now = datetime.now()
    log_file = f"{now.strftime('%Y-%m-%d')}-telegrambot.log"
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {msg}\n"
    
    # Write to log file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    # Print to console
    print(log_entry.strip())

# Main posting function
async def send_post():
    try:
        settings = load_settings()
        if not settings:
            await log_message("Config loading failed")
            return

        # Validate files
        msg_path = os.path.join(settings['folder_path'], settings['message_file'])
        img_path = os.path.join(settings['folder_path'], settings['image_file'])
        
        if not all(os.path.exists(p) for p in [msg_path, img_path]):
            await log_message("Missing message/image file")
            return

        # Read content
        with open(msg_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Initialize bot
        bot = Bot(token=settings['token'])
        
        # Send media with caption
        async with bot:
            with open(img_path, 'rb') as img_file:
                await bot.send_photo(
                    chat_id=settings['chat_id'],
                    photo=InputFile(img_file),
                    caption=text
                )
        await log_message("Post successfully sent")

    except TelegramError as e:
        await log_message(f"Telegram API error: {str(e)}")
    except Exception as e:
        await log_message(f"Unexpected error: {str(e)}")

# Scheduler
async def scheduler():
    settings = load_settings()
    if not settings:
        return

    await log_message("Scheduler started")
    
    while True:
        now = datetime.now()
        
        if settings['send_day'] == 0:
            # Periodic mode
            await send_post()
            interval = settings['send_hour'] * 3600 + settings['send_minute'] * 60
            await asyncio.sleep(interval)
        else:
            # Monthly mode
            if now.day == settings['send_day'] and \
               now.hour == settings['send_hour'] and \
               now.minute == settings['send_minute']:
                await send_post()
                await asyncio.sleep(86400)  # Wait 24h after post
            else:
                await asyncio.sleep(60)  # Check every minute

async def main():
    await log_message("Bot initialized")
    await scheduler()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
