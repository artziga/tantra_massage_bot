import os

from aiogram import Bot

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)

