from aiogram.types import CallbackQuery
from aiogram import Router, F

from keyboards.user_keboards import information_kb
from lexicon.user_lexicon import USERS

information_router = Router()


@information_router.callback_query(F.data == 'information_pressed')
async def show_information(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['information'])
    await callback.message.edit_reply_markup(reply_markup=information_kb)
