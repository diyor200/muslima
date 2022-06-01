from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ro'yhatdan o'tish"),
            KeyboardButton(text="Batafsil ma'lumot")
        ],
    ],
    resize_keyboard=True,
)

contact = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Kontakt", request_contact=True)
        ],

    ]
)
