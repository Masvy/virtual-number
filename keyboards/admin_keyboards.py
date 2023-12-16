from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.admin_lexicon import KEYBOARDS

admin_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=KEYBOARDS['show_users'],
                                 callback_data='show_users_pressed')
        ]
    ]
)
