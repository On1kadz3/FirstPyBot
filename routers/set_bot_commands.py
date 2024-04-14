from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    from commands_list import ru_commands_list as ru_cmd_list
    from commands_list import en_commands_list as en_cmd_list
    ru_commands = []
    for cmd in ru_cmd_list:
        ru_commands.append(BotCommand(command=cmd['command'], description=cmd['description']))

    en_commands = []
    for cmd in en_cmd_list:
        en_commands.append(BotCommand(command=cmd['command'], description=cmd['description']))

    await bot.set_my_commands(ru_commands, language_code="ru", scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(en_commands, language_code="en", scope=BotCommandScopeAllPrivateChats())
