from sqlalchemy import Column, BigInteger, String

from app.models import OrmBase


class ExampleTodo(OrmBase):
    __tablename__ = 'example_todo'

    id = Column(BigInteger, primary_key=True)
    description = Column(String)
