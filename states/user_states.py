from aiogram.fsm.state import State, StatesGroup


class Aaio(StatesGroup):
    amount = State()


class CryptoBot(StatesGroup):
    amount = State()
    crypto = State()


class Ton(StatesGroup):
    amount = State()


class YooMoney(StatesGroup):
    amount = State()


class Status(StatesGroup):
    price = State()
    agreement = State()
