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
                                 callback_data='profile_pressed')
        ],
        [InlineKeyboardButton(text=KEYBOARDS['referral'],
                              callback_data='referral_pressed')]
    ]
)
