import logging
import asyncio

from environs import Env
import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

from middlewares.check_register import RegisterCheck
from keyboards.set_menu import set_main_menu
from config.config import bot_config
from db.database import create_tables
from handlers import routers_list


def setup_logging():
    """Функция конфигурации логирования"""
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
               ' [%(asctime)s] - %(name)s - %(message)s',
    )
    logger = logging.getLogger(__name__)
    logger.info('Starting bot')


async def main():
    """
    Функция конфигурирования и запуска бота

    Создал объекты бота и диспетчера
    Зарегистрировал роутеры в диспетчере
    Создал url для соединения с базой
    Пропускаем накопившиеся апдейты и запускаем polling
    """
    setup_logging()

    storage: RedisStorage = RedisStorage.from_url(url='redis://localhost:6379/0',
                                                  key_builder=DefaultKeyBuilder(with_bot_id=True))

    env = Env()
    env.read_env()

    await create_tables()

    bot: Bot = Bot(token=bot_config.bot_token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    await set_main_menu(bot)

    dp.message.middleware(RegisterCheck())
    dp.callback_query.middleware(RegisterCheck())

    dp.include_routers(*routers_list)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Stopping bot')
