from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("reply"))
async def reply(msg: types.Message):
    await msg.reply("mana reply yozdim")
    await msg.answer("sizning chatinggiz reply boldi")