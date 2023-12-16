from datetime import datetime

from aiogram.types import CallbackQuery, Message
from aiocryptopay import AioCryptoPay, Networks
from aiogram.filters import or_f, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from keyboards.user_keboards import (profile_kb,
                                     payment_method_kb,
                                     proof_payment_kb,
                                     statuses_kb,
                                     agreement_kb,
                                     back_menu_kb)
from lexicon.user_lexicon import (write_profile,
                                  USERS,
                                  write_invoice)
from db.users import (read_users,
                      update_account,
                      read_account,
                      subtract_money)
from states.user_states import CryptoBot, Status
from config.config import bot_config

profile_router = Router()


@profile_router.callback_query(or_f(F.data == 'profile_pressed',
                                    F.data == 'back_pressed_2',
                                    F.data == 'no_pressed'))
async def show_profile(callback: CallbackQuery,
                       state: FSMContext):
    user_id = callback.from_user.id
    user = await read_users(user_id)
    user_res = user[0][0]
    registration_at = user_res.registration_at
    days_on_bot = (datetime.now() - registration_at).days
    status = user_res.status
    partners = user_res.partners
    bots = user_res.bots
    account = user_res.account
    completed = user_res.completed
    discarded = user_res.discarded
    await callback.message.edit_text(text=write_profile(user_id,
                                                        days_on_bot,
                                                        status,
                                                        partners,
                                                        bots,
                                                        account,
                                                        completed,
                                                        discarded))
    await callback.message.edit_reply_markup(reply_markup=profile_kb)
    await state.clear()


@profile_router.callback_query(F.data == 'replenish_pressed')
async def show_payment_method(callback: CallbackQuery):
    await callback.message.edit_text(text=USERS['payment_method'])
    await callback.message.edit_reply_markup(reply_markup=payment_method_kb)


@profile_router.callback_query(F.data == 'crypto_bot_pressed',
                               StateFilter(default_state))
async def request_amount(callback: CallbackQuery,
                         state: FSMContext):
    await callback.message.answer(text=USERS['request_amount'])
    await state.set_state(CryptoBot.amount)


@profile_router.message(StateFilter(CryptoBot.amount))
async def request_crypto(message: Message,
                         state: FSMContext):
    await state.update_data(amount=message.text)
    await message.answer(text=USERS['request_crypto'])
    await state.set_state(CryptoBot.crypto)


@profile_router.message(StateFilter(CryptoBot.crypto))
async def create_invoice(message: Message,
                         state: FSMContext):
    await state.update_data(crypto=message.text)
    data = await state.get_data()
    crypto = AioCryptoPay(token=bot_config.crypto_bot_token,
                          network=Networks.MAIN_NET)
    amount = await crypto.get_amount_by_fiat(summ=int(data['amount']),
                                             asset=data['crypto'].upper(),
                                             target='RUB')
    invoice = await crypto.create_invoice(asset=data['crypto'],
                                          amount=amount)
    await state.update_data(invoice_id=invoice.invoice_id)
    await message.answer(text=write_invoice(invoice.bot_invoice_url),
                         reply_markup=proof_payment_kb)


@profile_router.callback_query(F.data == 'proof_payment_pressed')
async def check_payment(callback: CallbackQuery,
                        state: FSMContext):
    user_id = callback.from_user.id
    crypto = AioCryptoPay(token=bot_config.crypto_bot_token,
                          network=Networks.MAIN_NET)
    data = await state.get_data()
    old_invoice = await crypto.get_invoices(invoice_ids=int(data['invoice_id']))
    if old_invoice.status == 'active':
        await callback.message.answer(text=USERS['payment_failed'])
    else:
        await callback.message.answer(text=USERS['payment_completed'])
        await update_account(user_id, int(data['amount']))
    await state.clear()


@profile_router.callback_query(F.data == 'status_pressed',
                               StateFilter(default_state))
async def show_statuses(callback: CallbackQuery,
                        state: FSMContext):
    await callback.message.edit_text(text=USERS['statuses'])
    await callback.message.edit_reply_markup(reply_markup=statuses_kb)
    await state.set_state(Status.price)


@profile_router.callback_query(or_f(F.data == 'for_month_pressed',
                                    F.data == 'for_3month_pressed',
                                    F.data == 'for_6month_pressed'),
                               StateFilter(Status.price))
async def request_agreement(callback: CallbackQuery,
                            state: FSMContext):
    if callback.data == 'for_month_pressed':
        await state.update_data(price=250)
    elif callback.data == 'for_3month_pressed':
        await state.update_data(price=650)
    else:
        await state.update_data(price=999)
    await callback.message.edit_text(text=USERS['agreement'])
    await callback.message.edit_reply_markup(reply_markup=agreement_kb)


@profile_router.callback_query(F.data == 'yes_pressed')
async def buy_status(callback: CallbackQuery,
                     state: FSMContext):
    data = await state.get_data()
    print(f'er23423412{data["price"]}')
    user_id = callback.from_user.id
    account = await read_account(user_id)
    if account > data['price']:
        if data['price'] == 250:
            await subtract_money(user_id=user_id,
                                 amount=250)
        elif data['price'] == 650:
            await subtract_money(user_id=user_id,
                                 amount=650)
        else:
            await subtract_money(user_id=user_id,
                                 amount=999)
        await callback.message.edit_text(text=USERS['congratulation'])
        await callback.message.edit_reply_markup(reply_markup=back_menu_kb)
    else:
        await callback.message.edit_text(text=USERS['insufficient_funds'])
        await callback.message.edit_reply_markup(reply_markup=back_menu_kb)
