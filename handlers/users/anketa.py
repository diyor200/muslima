from datetime import datetime
import asyncpg
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from loader import dp, db, bot
from states.userData import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.start_keyboard import contact

data = []


# registration form
@dp.message_handler(text="Batafsil ma'lumot")
async def inform(message: types.Message):
    await message.answer("Bunda ma'lumot beriladi")


@dp.message_handler(text="Ro'yhatdan o'tish")
async def enter_fullname(message: types.Message):
    await message.answer("Ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    await UserData.ism.set()


@dp.message_handler(state=UserData.ism)
async def enter_number(message: types.Message, state: FSMContext):
    name = message.text
    data.append(name)
    await message.answer("Kontaktingizni yuboring:", reply_markup=contact)
    await UserData.next()


@dp.message_handler(state=UserData.tel, content_types='contact')
async def enter_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    data.append(phone_number)
    await state.finish()
    try:
        await db.update_user(
            telegram_id=message.from_user.id,
            fullname=data[0],
            tel_nomer=data[1]

        )
    except asyncpg.UniqueViolationError:
        await bot.send_message(chat_id=ADMINS[0], text="xatolik")
    await message.reply(text=f"raxmat! Ma'lumotlaringiz qabul qilindi. Tez orada siz bilan aloqaga chiqamiz", reply_markup=ReplyKeyboardRemove())
    user = message.from_user.get_mention(name=data[0], as_html=True)
    registration_info = f"Yangi ariza!\n" \
                        f"Foydalanuvchi {user}\n" \
                        f"nomer: {data[1]}\n" \
                        f"sana: {datetime.fromtimestamp(1887639468)}"
    await bot.send_message(chat_id=ADMINS[0], text=registration_info)
    data.clear()


