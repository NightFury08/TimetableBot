from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from data.orm import select_timetables, select_notes

class Pagination(CallbackData, prefix="pag"):
    action: str
    user_id: int


class Time_table(CallbackData, prefix="Time_table"):
    id: int
    user_id: int

class Time_day(CallbackData, prefix="Day"):
    user_id: int
    timetable_id: int
    dayweek: str


class Note(CallbackData, prefix="Note"):
    get: str
    id: int
    user_id: int

class Table(CallbackData, prefix="Table"):
    get: str
    id: int
    user_id: int
    

# class GetNoteTimetable(CallbackData, prefix="getnotetimetable"):
#     get: str
#     id: int
#     user_id: int



def timetable(user_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Расписания", callback_data=Pagination(
            action="timetables", user_id=user_id).pack()),
        InlineKeyboardButton(text="Создать", callback_data=Pagination(
            action="createtimetable", user_id=user_id).pack()),
        InlineKeyboardButton(text="События сегодня", callback_data=Pagination(
            action="eventstoday", user_id=user_id).pack())
    )
    builder.adjust(1,1,1)
    return builder.as_markup()


def create_timetable(user_id):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(
            action="backtotimetable", user_id=user_id).pack())
    )
    builder.adjust(1)
    return builder.as_markup()

def create_note(user_id):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(
            action="backtonote", user_id=user_id).pack())
    )
    builder.adjust(1)
    return builder.as_markup()


def timetables(user_id: int):
    timetables = select_timetables(user_id=user_id)
    builder = InlineKeyboardBuilder()
    [builder.add(InlineKeyboardButton(text=timetable[1], callback_data=Table(get="gettimetable", id=int(timetable[0]), user_id=user_id).pack())) for timetable in select_timetables(user_id=user_id)]
    builder.add(InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(action="backtotimetable", user_id=user_id).pack()))
    builder.adjust(*[1]*len(timetables))
    return builder.as_markup(resize_keyboard=True)


def totimetable(user_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Показать всё расписание", 
                             callback_data=Pagination(action="showtimetable",
                                                      user_id=user_id).pack()),
        InlineKeyboardButton(text="Показать конкретный день", 
                             callback_data=Pagination(action="showday", 
                                                      user_id=user_id).pack()),
        InlineKeyboardButton(text="Внести изменения", 
                             callback_data=Pagination(action="edittimetable",
                                                      user_id=user_id).pack()),
        InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(
            action="backtotimetables", user_id=user_id).pack())
    )
    builder.adjust(*[1]*5, 2,1)
    return builder.as_markup()


def showday(user_id: int, timetable_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Понедельник", callback_data=Time_day(user_id=user_id,
            dayweek="1", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Вторник", callback_data=Time_day(user_id=user_id,
            dayweek="2", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Среда", callback_data=Time_day(user_id=user_id,
            dayweek="3", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Четверг", callback_data=Time_day(user_id=user_id,
            dayweek="4", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Пятница", callback_data=Time_day(user_id=user_id,
            dayweek="5", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Суббота", callback_data=Time_day(user_id=user_id,
            dayweek="6", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="Воскресенье", callback_data=Time_day(user_id=user_id,
            dayweek="7", timetable_id=timetable_id).pack()),
        InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(
            action="timetables", user_id=user_id).pack())
    )
    builder.adjust(*[1]*5, 2,1)
    return builder.as_markup()


def tonotes(user_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Заметки", callback_data=Pagination(
            action="notes", user_id=user_id).pack()),
        InlineKeyboardButton(text="Создать", callback_data=Pagination(
            action="createnote", user_id=user_id).pack()),
        InlineKeyboardButton(text="Удалить", callback_data=Pagination(
            action="removenote", user_id=user_id).pack())
    )
    builder.adjust(1,1)
    return builder.as_markup()

def notes(user_id: int):
    notes = select_notes(user_id=user_id)
    builder = InlineKeyboardBuilder()
    [builder.add(InlineKeyboardButton(text=note[1], callback_data=Note(get="getnote", id=int(note[0]), user_id=user_id).pack())) for note in select_notes(user_id=user_id)]
    builder.add(InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(action="backtonote", user_id=user_id).pack()))
    builder.adjust(*[1]*len(notes))
    return builder.as_markup(resize_keyboard=True)

def notes_remove(user_id: int):
    notes = select_notes(user_id=user_id)
    builder = InlineKeyboardBuilder()
    [builder.add(InlineKeyboardButton(text=f"{note[1]} ❌", callback_data=Note(get="delnote", id=int(note[0]), user_id=user_id).pack())) for note in select_notes(user_id=user_id)]
    builder.add(InlineKeyboardButton(text="⬅️Назад", callback_data=Pagination(action="backtonote", user_id=user_id).pack()))
    builder.adjust(*[1]*len(notes))
    return builder.as_markup(resize_keyboard=True)