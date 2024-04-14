import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config
from routers import cmd_router
from routers import dice_router
from routers import set_bot_commands
from commands_list import ru_commands_list


async def on_startup(bot: Bot):
    await set_bot_commands.set_bot_commands(bot=bot)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.include_router(cmd_router)
    dp.include_router(dice_router)
    await dp.start_polling(bot, ru_com_list=ru_commands_list)


if __name__ == "__main__":
    asyncio.run(main())
