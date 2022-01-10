from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from filters import IsPrivate
from loader import dp



@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Start",
            "/help - Help")
    
    await message.answer("\n".join(text))
