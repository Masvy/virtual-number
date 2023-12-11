from aiogram.types import CallbackQuery
from aiogram import Router, F

from lexicon.user_lexicon import write_profile
from keyboards.user_keboards import profile_kb

profile_router = Router()


@profile_router.callback_query(F.data == 'profile_pressed')
async def show_profile(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.message.edit_text(text=write_profile(user_id))
    await callback.message.edit_reply_markup(reply_markup=profile_kb)
