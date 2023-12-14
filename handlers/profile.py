from aiogram.types import CallbackQuery
from aiogram.filters import or_f
from aiogram import Router, F

from keyboards.user_keboards import profile_kb, payment_method_kb
from lexicon.user_lexicon import write_profile, USERS
from db.users import read_users

profile_router = Router()


@profile_router.callback_query(or_f(F.data == 'profile_pressed',
                                    F.data == 'back_pressed_2'))
async def show_profile(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await read_users(user_id)
    user_res = user[0][0]
    registration_at = user_res.registration_at
    status = user_res.status
    partners = user_res.partners
    bots = user_res.bots
    await callback.message.edit_text(text=write_profile(user_id,
                                                        registration_at,
                                                        status,
                                                        partners,
                                                        bots))
    await callback.message.edit_reply_markup(reply_markup=profile_kb)


@profile_router.callback_query(F.data == 'replenish_pressed')
async def show_payment_method(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['payment_method'])
    await callback.message.edit_reply_markup(reply_markup=payment_method_kb)
