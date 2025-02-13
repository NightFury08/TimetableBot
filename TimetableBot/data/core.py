from sqlalchemy import insert, select, update
from data.models import metadata, users_table, timetables_table
from data.database import engine



def create_tables():
    engine.echo=False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo=True

def add_user(id: int, username: str):
    with engine.connect() as conn:
        stmt = insert(users_table).values([{'id':id, 'username':username}])
        conn.execute(stmt)
        conn.commit()

def select_user():
    with engine.connect() as conn:
        query = select(users_table)
        result = conn.execute(query)
        users = result.all()
        print(f"{users=}")

def update_user(id: int, new_username: str):
    with engine.connect() as conn:
        stmt = (
            update(users_table)
            .values(username=new_username)
            .filter_by(id=id)
        )
        conn.execute(stmt)
        conn.commit()

def select_timetables():
    with engine.connect() as conn:
        query = select(timetables_table)
        result = conn.execute(query)
        timetables = result.all()
        print(f"{timetables=}")