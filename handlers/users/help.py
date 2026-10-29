from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def helpw(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman")
    n = "mendagi barcha kamandalar:\n"
    n += "/cars\n"
    n += "/shops\n"
    n += "/ismlar\n"
    n += "/fruits\n"
    n += "/delete\n"
    n += "/reply\n"
    n += "/answer\n"
    n += "/answer_photo\n"
    n += "/answer_dice\n"
    n += "/aniqla\n"
    n += "/salom\n"
    n += "/tayme\n"
    n += "/data\n"
    n += "/photo\n"
    n += "/animation\n"
    n += "/video\n"
    n += "/text\n"
    n += "/sticker\n"
    n += "/contact\n"
    n += "/dice\n"
    await msg.answer(n)
