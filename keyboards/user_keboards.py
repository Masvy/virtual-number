from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.user_lexicon import KEYBOARDS

main_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=KEYBOARDS['number'],
                              callback_data='number_pressed')],
        [
            InlineKeyboardButton(text=KEYBOARDS['information'],
                                 callback_data='information_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['profile'],
                                 callback_data='profile_pressed'),
        ],
        [InlineKeyboardButton(text=KEYBOARDS['referral'],
                              callback_data='referral_pressed')],
    ]
)

information_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['rules'],
                                 url='https://teletype.in/@toptgdima/e1DtyI3GrCJ'),
            InlineKeyboardButton(text=KEYBOARDS['news'],
                                 url='https://t.me/TopTgDima'),
        ],
        [InlineKeyboardButton(text=KEYBOARDS['admin'],
                              url='https://t.me/TopTgCreator')],
        [InlineKeyboardButton(text=KEYBOARDS['back'],
                              callback_data='back_pressed_1'),]
    ]
)

profile_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text=KEYBOARDS['replenish'],
                                callback_data='replenish_pressed'),
           InlineKeyboardButton(text=KEYBOARDS['status'],
                                callback_data='status_pressed'),
        ],
        [InlineKeyboardButton(text=KEYBOARDS['bot_constructor'],
                              callback_data='bot_constructor_pressed')],
        [InlineKeyboardButton(text=KEYBOARDS['back'],
                              callback_data='back_pressed_1')],
    ],
)

payment_method_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['crypto_bot'],
                                 callback_data='crypto_bot_pressed'),
            InlineKeyboardButton(text=KEYBOARDS['ton'],
                                 callback_data='ton_pressed'),
        ],
        [
            InlineKeyboardButton(text=KEYBOARDS['back'],
                                 callback_data='back_pressed_2'),
            InlineKeyboardButton(text=KEYBOARDS['card'],
                                 callback_data='card_pressed'),
        ],
    ]
)
