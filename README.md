# Telegram Scheduled Posting Bot
This is a Python-based bot for Telegram that allows you to automatically send messages and images to a specified chat or channel on a scheduled basis. The bot can send posts either monthly on a specific day and time or periodically at a specified interval.

# Features
Scheduled Posting: Send messages and images to a Telegram chat or channel at a specific time or interval.
### Key improvements:
#### Full Async Architecture
Uses async/await for all I/O operations

#### Modern PTB 20.x+ Syntax
Proper use of the context manager for a bot

#### Smart Scheduling

In periodic mode: precise intervals

In monthly mode: check every minute

#### Error Handling
Separate Telegram API error handling

#### Clean Logging
Asynchronous logging with writing to a file


## Customizable Content:

Text message from a .txt file.

Image from a .png file.

## Flexible Scheduling:

Monthly posting on a specific day and time.

Periodic posting at a specified interval (e.g., every 1 hour).

Logging: All actions are logged in a file for easy debugging and tracking.

# Prerequisites
Before running the bot, ensure you have the following:

Python 3.7 or higher.

### Telegram Bot:

Create a Telegram bot using BotFather.

Obtain the bot's API Token.

### Chat ID:

For a group chat: Add the bot to the group and send a message. Use https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates to find the chat_id.

For a channel: Add the bot as an admin and use the channel`s username (e.g., @my_channel).

# Installation
## Clone the repository or download the bot script:


`git clone https://github.com/your-repo/telegram-scheduled-bot.git`
`cd telegram-scheduled-bot`

## Install the required libraries:

`pip install python-telegram-bot schedule`

# Prepare the files:

## Create a folder named tosend in the same directory as the script.

Inside the **tosend** folder, place:

A text file named message.txt containing the message you want to send.

An image file named img.png (or any other image format supported by Telegram).

# Configure the bot:

Create a settings.json file in the same directory as the script with the following content:

```json

{
  "folder_path": "tosend",
  "message_file": "message.txt",
  "image_file": "img.png",
  "send_day": 15,
  "send_hour": 10,
  "send_minute": 0
}
```
## Set variables in sendbot.py:

**CHAT_ID:** The ID of the chat or channel where the bot will send messages.

**TOKEN:** Your Telegram bot's API token.

# Configuration Options
### settings.json fields	description:
**folder_path** - Path to the folder containing the message and image files.

**message_file** - Name of the text file containing the message (e.g., message.txt).

**image_file** - Name of the image file to be sent (e.g., img.png).

**send_day** - Day of the month to send the message (set to 0 for periodic posting).

**send_hour** - Hour of the day to send the message.

**send_minute** - Minute of the hour to send the message.


# Scheduling Modes
## Monthly Posting:

Set send_day to a specific day of the month (e.g., 15 for the 15th).

Example:

```json
{
  "send_day": 15,
  "send_hour": 10,
  "send_minute": 0
}
```
The bot will send the message on the 15th of every month at 10:00 AM.

## Periodic Posting:

Set send_day to 0.

Specify the interval using send_hour and send_minute.

Example:

```json
{
  "send_day": 0,
  "send_hour": 1,
  "send_minute": 30
}
```
The bot will send the message every 1 hour and 30 minutes.

# Running the Bot
## Start the bot:
Run the script using Python:

```python
python telegram_bot.py
```
## Check the logs:

Logs are saved in a file named nowdate-telegrambot.log (e.g., 2023-10-15-telegrambot.log).

Each log entry includes a timestamp and a description of the action.

# Logs
Logs are saved in a file named nowdate-telegrambot.log (e.g., 2023-10-15-telegrambot.log). Each log entry includes:

A timestamp in the format YYYY-MM-DD HH:MM:SS.

A description of the action (e.g., "Message and image sent successfully").

Example log:

[2023-10-15 10:00:00] Bot started.
[2023-10-15 10:00:01] Message and image sent successfully.

# Troubleshooting
### File Not Found:

Ensure the message.txt and img.png files exist in the tosend folder.

### Invalid Token or Chat ID:

Double-check the token and chat_id in settings.json.

### Permissions:

Ensure the bot has permission to send messages in the specified chat or channel.

### Logs:

Check the log file for detailed error messages.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Support
For questions or issues, please open an issue on the GitHub repository.

Enjoy automating your Telegram posts! 🚀
