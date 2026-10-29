import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.help import rt as help
from handlers.users.test import rt as test
from handlers.users.ism import rt as ismlar
from handlers.users.car import rt as cars
from handlers.users.meva import rt as furits
from handlers.users.shop import rt as shops
from handlers.users.delete import rt as delete
from handlers.users.answer import rt as  answer
from handlers.users.answer_photo import rt as answer_photo
from handlers.users.answer_dice import rt as answer_dice
from handlers.users.repli import rt as reply
from handlers.users.aniqla import rt as aniqla
from handlers.users.salom import rt as salom
from handlers.users.tayme import rt as tayme
from handlers.users. data import rt as data
from handlers.users. media import rt as media
from handlers.users. mejik_filter import rt as mejik_filter
from handlers.users. f_date import rt as f_date
from handlers.users.test import rt as mushuk




dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)

    dp.include_router(start)
    dp.include_router(help)
    dp.include_router(ismlar)
    dp.include_router(cars)
    dp.include_router(furits)
    dp.include_router(shops)
    dp.include_router(delete)
    dp.include_router(answer)
    dp.include_router(answer_photo)
    dp.include_router(answer_dice)
    dp.include_router(reply)
    dp.include_router(aniqla)
    dp.include_router(salom)
    dp.include_router(tayme)
    dp.include_router(data)
    dp.include_router(media)
    dp.include_router(f_date)
    dp.include_router(mejik_filter)
    dp.include_router(mushuk)
    dp.include_router(test)





    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
