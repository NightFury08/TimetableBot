from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, fabrics

router = Router()

@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    if msg == "меню":
        await message.answer("Меню", reply_markup=reply.main)
    elif msg == "расписание":
        await message.answer("Действия с расписаниями:", 
                             reply_markup=fabrics.timetable(user_id=message.from_user.id))
    elif msg == "заметки":
        await message.answer("Действия с заметками:", 
                             reply_markup=fabrics.tonotes(user_id=message.from_user.id))


