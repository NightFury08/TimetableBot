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
    name: Mapped[str | None]
    time_start: Mapped[datetime.time] = mapped_column(db.Time)
    time_end: Mapped[datetime.time] = mapped_column(db.Time)

metadata = MetaData()

