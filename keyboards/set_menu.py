from aiogram.types import BotCommand
from aiogram import Bot

from lexicon.user_lexicon import COMMANDS_LIST


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
                                command=command,
                                description=description
                          ) for command,
                          description in COMMANDS_LIST.items()]
    await bot.set_my_commands(main_menu_commands)
