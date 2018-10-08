from flask import current_app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        self._engine = None
        self._sessionmaker = None

    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(current_app.config['DATABASE_URI'])
        return self._engine

    @property
    def sessionmaker(self):
        if self._sessionmaker is None:
            self._sessionmaker = sessionmaker()
            self._sessionmaker.configure(bind=self.engine)
        return self._sessionmaker


db = DB()


class DBSession:
    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = db.sessionmaker()
        return self.session

    def __exit__(self, type, value, tb):
        if tb is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()


def reset_db():
    from app.models import metadata
    from app.models.example_todo import ExampleTodo

    metadata.drop_all(bind=db.engine)
    metadata.create_all(bind=db.engine)

    # pour default records in
    todos = [
        'Book flights',
        'Buy power adapter',
    ]

    with DBSession() as session:
        for todo_desc in todos:
            todo = ExampleTodo(description=todo_desc)
            session.add(todo)
