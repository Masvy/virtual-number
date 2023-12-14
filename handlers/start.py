from aiogram.filters import CommandStart
from aiogram import Router, F, types
from aiogram.types import Message

from keyboards.user_keboards import main_kb
from lexicon.user_lexicon import USERS

start_router = Router()


@start_router.message(CommandStart())
@start_router.callback_query(F.data == 'back_pressed_1')
async def start_bot(update: types.Update):
    if isinstance(update, types.Message):
        await update.answer(text=USERS['greetings'],
                            reply_markup=main_kb)
    else:
        await update.message.edit_text(USERS['greetings'])
        await update.message.edit_reply_markup(reply_markup=main_kb)
