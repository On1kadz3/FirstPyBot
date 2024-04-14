import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config
from routers import cmd_router
from routers import dice_router

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN.get_secret_value())
dp = Dispatcher()
dp.include_router(cmd_router)
dp.include_router(dice_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
