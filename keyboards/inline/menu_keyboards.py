from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        InlineKeyboardButton(text="ro'yhatdan o'tish", callback_data='register'),
        InlineKeyboardButton(text="Batafsil ma'lumot", callback_data='full_information'),
    ]
)
