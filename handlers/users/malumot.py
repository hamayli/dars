from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("Malumot"))
async def test(msg: types.Message):
   await msg.answer(str(msg.from_user.first_name))
