from sqlalchemy import insert, select
from data.models import metadata, UsersOrm, NotesOrm, TimetablesOrm, EventsOrm
from data.database import engine, session_factory, Base
from datetime import time


def create_tables():
    engine.echo=False
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # engine.echo=True


def add_user(id: int, username: str):
    user = UsersOrm(username = username, id = id)
    with session_factory() as session:
        session.add(user)
        session.flush()
        session.commit()

def update_user(id: int, new_username: str):
    with session_factory() as session:
        user = session.get(UsersOrm, id)
        user.username = new_username
        session.commit()

def select_users():
    with session_factory() as session:
        query = select(UsersOrm)
        result = session.execute(query)
        users = result.scalars().all()
        
        # ФормируемReadable Output
        users_output = [f"ID: {user.id}, Username: {user.username}" for user in users]
        print("Пользователи:\n" + "\n".join(users_output))


def add_note(user_id: int, content: str):
    user = NotesOrm(user_id = user_id, name = content.split()[0], content = content)
    with session_factory() as session:
        session.add(user)
        session.commit()

# def update_note(id: int, new_content: str):
#     with session_factory() as session:
#         note = session.get(NotesOrm, id)
#         note.content = new_content
#         session.commit()

def select_notes(user_id: int):
    with session_factory() as session:
        query = select(NotesOrm).where(NotesOrm.user_id == user_id)
        results = session.execute(query).scalars().all()
        notes = [[note.id, note.name, note.content, note.created_at, note.updated_at] for note in results]
        print(notes)
        return notes
    
def select_note(note_id: int):
    with session_factory() as session:
        query = select(NotesOrm).where(NotesOrm.id == note_id)
        results = session.execute(query).scalars().all()
        notes = [[note.id, note.name, note.content, note.created_at, note.updated_at] for note in results]
        print(notes)
        return notes
    
def delete_note(note_id: int):
    with session_factory() as session:
        session.query(NotesOrm).where(NotesOrm.id == note_id).delete()
        session.commit()


def add_timetable(user_id: int, name: str):
    timetable = TimetablesOrm(user_id = user_id, name = name)
    with session_factory() as session:
        session.add(timetable)
        session.commit()

def select_timetables(user_id: int):
    with session_factory() as session:
        query = select(TimetablesOrm).where(TimetablesOrm.user_id == user_id)
        results = session.execute(query).scalars().all()
        timetables = [[timetable.id, timetable.name] for timetable in results]
        print(timetables)
        return timetables
    
def select_timetable(timetable_id: int):
    with session_factory() as session:
        query = select(TimetablesOrm).where(TimetablesOrm.id == timetable_id)
        results = session.execute(query).scalars().all()
        timetable = [[timetable.id, timetable.name] for timetable in results]
        print(timetable)
        return timetable
    
def delete_timetable(timetable_id: int):
    with session_factory() as session:
        session.query(TimetablesOrm).where(TimetablesOrm.id == timetable_id).delete()
        session.commit()


def add_event(weekday:int, user_id:int, timetable_id: int, name: str, time_start: time, time_end: time):
    day = EventsOrm(weekday=weekday, user_id=user_id, timetable_id = timetable_id, name = name, time_start=time_start, time_end=time_end)

    with session_factory() as session:
        session.add(day)
        session.commit()


def select_events(user_id: int, weekday: int, timetable_id: int):
    with session_factory() as session:
        query = select(EventsOrm).where(EventsOrm.weekday == weekday, EventsOrm.timetable_id == timetable_id)

        results = session.execute(query).scalars().all()
        day_events = [[day.id, day.name, day.time_start, day.time_end] for day in results]
        print(day_events)
        return day_events
 