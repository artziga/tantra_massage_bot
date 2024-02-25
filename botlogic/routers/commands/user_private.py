import aiohttp
from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InputFile, BufferedInputFile

from botlogic.routers.fun_fandlers import get_specialists_info
from botlogic.serializer import SpecialistPagedSerializer
from keyboards.inline_kbds import kb
from keyboards.reply_kbds import article_keyboard

router = Router(name=__name__)


@router.message(F.text == "Смотреть мастеров")
async def specialists_list_handler(message: types.Message):
    specialist_paged_data = SpecialistPagedSerializer(get_specialists_info()).serialize()
    specialist = specialist_paged_data.specialist
    text = (f"{specialist.first_name} {specialist.last_name}\nСтраница {specialist_paged_data.current_page} из"
            f" {specialist_paged_data.total_pages}")
    image_url = specialist.images
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            result_bytes = await response.read()
    await message.answer_photo(photo=BufferedInputFile(result_bytes, filename=''), caption=text, reply_markup=kb)


@router.message(F.text == "Смотреть анонсы")
async def events_list_handler(message: types.Message):
    await message.answer('Вот список анонсов:')


@router.message(F.text == "Читать статьи")
async def articles_list_handler(message: types.Message):
    await message.answer('Выберите что вы хотите:', reply_markup=article_keyboard)
