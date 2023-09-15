import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from loguru import logger

from config import bot_token, DEFAULT_COMMANDS
from handlers import setup_all_routers


async def main():
    logger.add("debug.log", format="{time} {level} {message}", level='DEBUG')
    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(setup_all_routers())
    await bot.set_my_commands(commands=DEFAULT_COMMANDS)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logger.info('Начало работы.')
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Остановка работы.')