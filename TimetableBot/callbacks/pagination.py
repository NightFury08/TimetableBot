from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums import ParseMode
from keyboards import fabrics

from data.orm import select_note, delete_note, select_timetable, select_events

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["timetables", "eventstoday"])))
async def timetable_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    if callback_data.action == "timetables":
        await call.message.edit_text("Выберите расписание:")
        await call.message.edit_reply_markup(reply_markup=fabrics.timetables(user_id=callback_data.user_id))


@router.callback_query(fabrics.Table.filter(F.get.in_(["gettimetable"])))
async def note_handler(call: CallbackQuery, callback_data: fabrics.Table):
    if callback_data.get == "gettimetable":
        await call.message.edit_text(select_timetable(timetable_id=callback_data.id)[0][1])
        await call.message.edit_reply_markup(reply_markup=fabrics.showday(user_id=callback_data.user_id, timetable_id=callback_data.id))

@router.callback_query(fabrics.Time_day.filter(F.dayweek.in_(["1", "2", "3", "4", "5", "6", "7"])))
async def events_handler(call: CallbackQuery, callback_data: fabrics.Time_day):
        await call.message.edit_text(f"{select_events(user_id=callback_data.user_id, timetable_id=callback_data.timetable_id, weekday=callback_data.dayweek)}", parse_mode=ParseMode.MARKDOWN_V2)
        await call.message.edit_reply_markup(reply_markup=fabrics.showday(user_id=callback_data.user_id, timetable_id=callback_data.timetable_id))
        


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["notes", "removenote"])))
async def note_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    if callback_data.action == "notes":
        await call.message.edit_text("Выберите заметку:")
        await call.message.edit_reply_markup(reply_markup=fabrics.notes(user_id=callback_data.user_id))
    elif callback_data.action == "removenote":
        await call.message.edit_text("Выберите заметку:")
        await call.message.edit_reply_markup(reply_markup=fabrics.notes_remove(user_id=callback_data.user_id))


@router.callback_query(fabrics.Note.filter(F.get.in_(["getnote"])))
async def note_handler(call: CallbackQuery, callback_data: fabrics.Note):
    if callback_data.get == "getnote":
        await call.message.edit_text(select_note(note_id=callback_data.id)[0][2])
        await call.message.edit_reply_markup(reply_markup=fabrics.notes(user_id=callback_data.user_id))

@router.callback_query(fabrics.Note.filter(F.get.in_(["delnote"])))
async def note_handler(call: CallbackQuery, callback_data: fabrics.Note):
    if callback_data.get == "delnote":
        delete_note(note_id=callback_data.id)
        # await call.message.edit_text(select_note(note_id=callback_data.id)[0][2])
        await call.message.edit_reply_markup(reply_markup=fabrics.notes_remove(user_id=callback_data.user_id))
    


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["ToTimetable", "backtotimetable"])))
async def timetables_handler(call: CallbackQuery, callback_data: fabrics.Pagination):

    if callback_data.action == "ToTimetable":
        await call.message.edit_text("Действия с расписанием:")
        await call.message.edit_reply_markup(reply_markup=fabrics.totimetable())

    elif callback_data.action == "backtotimetable":
        await call.message.edit_text("Действия с расписаниями:")
        await call.message.edit_reply_markup(reply_markup=fabrics.timetable(user_id=callback_data.user_id))


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["ToNote", "backtonote"])))
async def notes_handler(call: CallbackQuery, callback_data: fabrics.Pagination):

    if callback_data.action == "ToNote":
        await call.message.edit_text("Действия с заметками:")
        await call.message.edit_reply_markup(reply_markup=fabrics.tonotes())

    elif callback_data.action == "backtonote":
        await call.message.edit_text("Действия заметками:")
        await call.message.edit_reply_markup(reply_markup=fabrics.tonotes(user_id=callback_data.user_id))