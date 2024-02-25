from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from keyboards.reply_kbds import start_keyboard

router = Router(name=__name__)


@router.message(F.text == 'В начало 🔙')
@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer('Thank you for using', reply_markup=start_keyboard)


@router.message(Command('help'))
async def command_start_handler(message: types.Message) -> None:
    await message.answer('Вот, что я умею:')
