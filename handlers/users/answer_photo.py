from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("answer_photo"))
async def answer(msg: types.Message):
    await msg.answer_photo("https://www.imdb.com/title/tt0948470/mediaindex/", caption="bu o'rgimchak odam rasmi")
    await msg.answer("photo")
