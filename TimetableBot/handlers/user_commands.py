from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandObject, CommandStart

from data.orm import add_user, select_timetable, select_timetables, add_event

from keyboards import reply

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я твой бот для расписания и заметок", 
                         reply_markup=reply.main)
    add_user(id=message.from_user.id, username=message.from_user.username)


@router.message(Command(commands=["remove_buttons"]))
async def revbttns(message: Message):
    await message.answer("Кнопки убраны", reply_markup=ReplyKeyboardRemove())

@router.message(Command(commands=["addevent"]))
async def nametimeta(message: Message):
    message_text = str(message.text).lstrip("/addevent ")
    split_text = message_text.split()
    timetable_id = split_text[0]
    weekday = split_text[1]
    body = message_text.lstrip(f"{split_text[0]} {split_text[1]}")
    if int(select_timetable(timetable_id=timetable_id)[0][2]) == int(message.from_user.id):
        add_event(weekday=weekday, user_id=message.from_user.id, timetable_id=timetable_id, body=body)
        await message.answer("Событие добавлено", reply_markup=reply.main)