import asyncio
from aiogram.dispatcher import FSMContext

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_message(
            chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!"
        )
        await asyncio.sleep(0.05)


@dp.message_handler(text="/count", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[1]
        await message.reply(user_id)
        await asyncio.sleep(0.05)
    # await message.reply(users)

@dp.message_handler(text="/drop", user_id=ADMINS)
async def drop_table(message: types.Message):
    await db.drop_users()
    await message.answer("Jadval o'chirildi!")

