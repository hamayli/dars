from aiogram import Router, types
rt = Router()
@rt.message()
async def test(msg: types.Message):
    print(msg.from_user.id)
    await msg.forward(7790243693)
    await msg.copy_to(8744975719)
