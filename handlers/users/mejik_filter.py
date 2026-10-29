from aiogram import Router, types, F
rt = Router()
@rt.message(F.photo)
async def mejik_filter(msg: types.Message):
   await msg.answer("siz rasm yubordingiz")

@rt.message(F.animation)
async def mejik_filter(msg: types.Message):
   await msg.answer("siz gif yubordingiz")

@rt.message(F.video)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz video yubordingiz")

@rt.message(F.text)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz text yubordingiz")

@rt.message(F.sticker)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz text yubordingiz")

@rt.message(F.contact)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz contact yubordingiz")

@rt.message(F.dice)
async def mejik_filter(msg: types.Message):
    await msg.answer("siz dice yubordingiz")





