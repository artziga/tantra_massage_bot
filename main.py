import asyncio

from aiogram import Dispatcher

from botlogic.routers import router
from botlogic.routers.fun_fandlers import echo
from botlogic.settings import bot

dp = Dispatcher()

dp.include_router(router)


async def main() -> None:

    # dp.message.register(echo)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
