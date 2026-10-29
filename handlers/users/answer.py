from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("answer"))
async def answer(msg: types.Message):
    await msg.answer("odiy javob")
    await msg.answer("sizng botinggiz answer bo'ladi")
