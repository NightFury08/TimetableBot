import sqlalchemy as db
from sqlalchemy import (
    Table, Column, MetaData, Integer, String, ForeignKey, text)
from sqlalchemy.orm import Mapped, mapped_column
from data.database import Base
import datetime
from typing import Annotated



intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("CURRENT_TIMESTAMP"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("CURRENT_TIMESTAMP"),
          onupdate=datetime.datetime.utcnow,)]

class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str]


class NotesOrm(Base):
    __tablename__ = 'notes'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'))
    name: Mapped[str | None]
    content: Mapped[str | None]
    created_at: Mapped[created_at | None]
    updated_at: Mapped[updated_at | None]



class TimetablesOrm(Base):
    __tablename__ = 'timetables'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'))
    name: Mapped[str]


class EventsOrm(Base):
    __tablename__ = 'events'

    id: Mapped[intpk]
    weekday: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'))
    timetable_id: Mapped[int] = mapped_column(
        ForeignKey('timetables.id', ondelete='CASCADE'))
    body: Mapped[str | None]
    time_start: Mapped[datetime.time | None] = mapped_column(db.Time)
    time_end: Mapped[datetime.time | None] = mapped_column(db.Time)


# class TuesdayOrm(Base):
#     __tablename__ = 'tuesday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)


# class WednesdayOrm(Base):
#     __tablename__ = 'wednesday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)

# class ThursdayOrm(Base):
#     __tablename__ = 'thursday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)

# class FridayOrm(Base):
#     __tablename__ = 'friday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)

# class SaturdayOrm(Base):
#     __tablename__ = 'saturday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)

# class SundayOrm(Base):
#     __tablename__ = 'sunday'

#     id: Mapped[intpk]
#     timetable_id: Mapped[int] = mapped_column(
#         ForeignKey('timetables.id', ondelete='CASCADE'))
#     name: Mapped[str | None]
#     time_start: Mapped[datetime.time] = mapped_column(db.Time)
#     time_end: Mapped[datetime.time] = mapped_column(db.Time)




metadata = MetaData()



users_table = Table('users', metadata, 
  Column('id', Integer, primary_key=True, unique=True),
  Column('username', String)
)

notes = Table('notes', metadata, 
  Column('id', Integer, primary_key=True),
  Column('user_id', Integer, db.ForeignKey('users.id')),
  Column('name', String),
  Column('content', String),
  Column('created_at', db.TIMESTAMP),
  Column('updated_at', db.TIMESTAMP)
)

timetables_table = Table('timetables', metadata, 
  Column('id', Integer, primary_key=True),
  Column('user_id', Integer, db.ForeignKey('users.id')),
  Column('timetable_name', String)
)

monday = Table('monday', metadata, 
  Column('id', Integer, primary_key=True),
  Column('timetable_id', Integer, db.ForeignKey('timetables.id')),
  Column('name', String),
  Column('time_start', db.Time),
  Column('time_end', db.Time)
)

tuesday = db.Table('tuesday', metadata, 
  db.Column('id', Integer, primary_key=True),
  db.Column('timetable_id', Integer, db.ForeignKey('timetables.id')),
  db.Column('name', String),
  db.Column('time_start', db.Time),
  db.Column('time_end', db.Time)
)

wednesday = db.Table('wednesday', metadata, 
  db.Column('id', Integer, primary_key=True),
  db.Column('timetable_id', Integer, db.ForeignKey('timetables.id')),
  db.Column('name', String),
  db.Column('time_start', db.Time),
  db.Column('time_end', db.Time)
)




'''
metadata.create_all(engine)

insertion_query = users.insert().values([
  {'id':Message.from_user.id, 'username':'Message.from_user.username'}
])
conn.execute(insertion_query)
conn.commit()

insertion_query = timetables.insert().values([
  {'user_id':'1', 'timetable_name':'Message.text'}
])
conn.execute(insertion_query)
conn.commit()
insertion_query = monday.insert().values([
  {'timetable_id':'1', 'name':'Message.text', 
  'time_start':time(12,30), 'time_end':time(13,30)}
])
conn.execute(insertion_query)

conn.commit()


select_all_query = db.select(users) 
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())

select_all_query = db.select(notes) 
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())

select_all_query = db.select(timetables) 
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())

select_all_query = db.select(monday) 
select_all_results = conn.execute(select_all_query)
print(select_all_results.fetchall())

'''