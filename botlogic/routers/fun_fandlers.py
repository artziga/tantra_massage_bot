from aiogram import types

import requests

API_URL = "http://localhost:8000/"


def get_specialists_info():
    response = requests.get(API_URL + f"specialists/api/v1/specialists/")
    if response:
        print(type(response.json()))
        return response.json()
    return None


def format_specialist_info(data: dict=None) -> str:
    if data is None:
        info = get_specialists_info()



async def echo(message: types.Message):
    await message.reply(f'Привет {message.from_user.first_name}, тебе тоже {message.text}')


async def get_specialists(message: types.Message):
    reviews = get_specialists_info().get('results')

    specialists_names = []
    if reviews:
        specialists_names = [
            f"{review['author']['first_name']} {review['author']['last_name']}, поставил оценку {review['score']} и написал {review['text']}"
            for review in reviews]

    await message.reply(', '.join(specialists_names))
