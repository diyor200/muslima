from aiogram.dispatcher.filters.state import StatesGroup, State


class UserData(StatesGroup):
    ism = State()
    tel = State()
