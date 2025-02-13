from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase


engine = create_engine(
    url='sqlite:///BotDatabase.db',
    echo=True,
    #pool_size=5,
    #max_overflow=10,
)


session_factory = sessionmaker(engine)

class Base(DeclarativeBase):
    pass