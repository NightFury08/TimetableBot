from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandObject, CommandStart

from data.orm import add_user, select_timetables

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

@router.message(Command(commands=["select_timename"]))
async def nametimeta(message: Message):
    select_timetables(user_id=message.from_user.id)
    await message.answer("названия расписаний", reply_markup=ReplyKeyboardRemove())