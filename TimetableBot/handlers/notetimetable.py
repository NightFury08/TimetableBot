from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import wait_timetable_name, wait_note_name, wait_note_content
from keyboards import fabrics

from data.orm import add_timetable, add_note


router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["createnote"])))
async def create_note(call: CallbackQuery, callback_data: fabrics.Pagination, state: FSMContext):
    await state.set_state(wait_note_name.waiting_note_name)
    await call.message.edit_text("Введите заметку:")
    await call.message.edit_reply_markup(reply_markup=fabrics.create_note(user_id=callback_data.user_id))

@router.message(wait_note_name.waiting_note_name)
async def note_name(message: Message, state: FSMContext):
    print(message.text)
    await state.clear()
    add_note(user_id=message.from_user.id, content=message.text)
    await message.answer("Выберите заметку:", reply_markup=fabrics.notes(user_id=message.from_user.id))



# @router.message(wait_note_content.waiting_note_content)
# async def note_name(message: Message, state: FSMContext):
#     print(message.text)
#     await state.clear()
#     add_note(user_id=message.from_user.id, name="Fastnote", content=message.text)
#     await message.answer("Выберите заметку:", reply_markup=fabrics.notes(user_id=message.from_user.id))


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["createtimetable"])))
async def create_timetable(call: CallbackQuery, callback_data: fabrics.Pagination, state: FSMContext):
    await state.set_state(wait_timetable_name.waiting_timetable_name)
    await call.message.edit_text("Введите название расписания:")
    await call.message.edit_reply_markup(reply_markup=fabrics.create_timetable(user_id=callback_data.user_id))

@router.message(wait_timetable_name.waiting_timetable_name)
async def timetable_name(message: Message, state: FSMContext):
    print(message.text)
    await state.clear()
    add_timetable(user_id=message.from_user.id, name=message.text)
    await message.answer("Выберите расписание:", reply_markup=fabrics.timetables(user_id=message.from_user.id))


# @router.message(Command("add_timetable"))
# async def add_timetable(message: Message, state: FSMContext):
#     await state.set_state(wait_timetable_name.waiting_timetable_name)
#     await message.answer(
#         "Введите название расписания:",
#         reply_markup=fabrics.create_timetable()
#     )