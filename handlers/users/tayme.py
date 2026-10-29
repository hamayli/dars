from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("tayme"))
async def tayme(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
      f" {sana.hour} : {sana.minute} : {sana.second}\n"

   )