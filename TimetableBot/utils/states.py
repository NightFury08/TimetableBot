from aiogram.fsm.state import StatesGroup, State


class wait_note_name(StatesGroup):
    waiting_note_name = State()

class wait_note_content(StatesGroup):
    waiting_note_content = State()

class wait_timetable_name(StatesGroup):
    waiting_timetable_name = State()