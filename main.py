import asyncio
import os
from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    await message.reply(message.text)


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
