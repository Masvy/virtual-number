from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from keyboards.user_keboards import main_kb
from lexicon.user_lexicon import USERS

start_router = Router()


@start_router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(text=USERS['greetings'],
                         reply_markup=main_kb)
