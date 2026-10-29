
from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("aniqla"))
async def aniqla(msg: types.Message):
   holat = ""
   if msg.chat.type == "private":
      holat += "siz lichkamga yozyapsiz!\n"
   else:
      holat += f"siz guruhdasiz! :{msg.chat.title}!  \n"
   n = "sizning barcha ma'lumotlaringiz!\n"
   n += holat
   n += f"ism: {msg.chat.first_name}!\n"
   n += f"id: {msg.chat.id}!\n"
   f = ""
   if msg.chat.last_name:
      f += f"{msg.chat.last_name}!"
   else:
      f += "mavjud emas!"
   n += f"familya: {f}!\n"

   await msg.answer(n)