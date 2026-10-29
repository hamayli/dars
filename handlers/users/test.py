from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def test(msg: types.Message):
   if msg.text == "aka":
      await msg.answer("uka")
   elif msg.text == "uka":
      await msg.answer("aka")
   else:
      if msg.text == "salom":
         await msg.answer("qalesan")
