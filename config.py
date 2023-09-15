import os

from dotenv import find_dotenv, load_dotenv
from aiogram.types.bot_command import BotCommand

if not find_dotenv():
    exit('отсутствует файл .env')

else:
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = [
    BotCommand(command="start", description="Запустить бота"),
    BotCommand(command='equations', description='Решать квадратные уравнения'),
    BotCommand(command='formula', description='Формула для решения')
]
