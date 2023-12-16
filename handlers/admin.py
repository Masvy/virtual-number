import os

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import and_f, Command

from utils.excel_file import generate_excel_file
from keyboards.admin_keyboards import admin_kb
from filters.admin_filters import IsAdmin
from config.config import bot_config
from db.users import show_user_ids

admin_router: Router = Router()


@admin_router.message(and_f(Command(commands='admin'), IsAdmin(bot_config.admin_list)))
async def start_admin(message: Message):
    await message.answer(text='Выбери действие:',
                         reply_markup=admin_kb)


@admin_router.callback_query(F.data == 'show_users_pressed')
async def show_users(callback: CallbackQuery,
                     bot: Bot):
    user_ids = await show_user_ids()
    excel_file = await generate_excel_file(user_ids=user_ids)

    temp_file_path = "temp_user_database.xlsx"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(excel_file.read())

    await bot.send_document(callback.from_user.id,
                            document=FSInputFile(temp_file_path))
    os.remove(temp_file_path)
