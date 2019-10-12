from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

from webapp.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True,
                      nullable=False)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)

    def __init__(self, name, surname, password, age):
        self.name = name
        self.surname = surname
        self.password = password
        self.age = age

    def __repr__(self):
        return f"<User('{self.name}', '{self.surname}', '{self.password}', "\
               f"'{self.user_age}')>"


class Values(Base):
    __tablename__ = 'values'
    id = Column(Integer, primary_key=True)
    value = Column(Text)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<Value '{self.id}' '{self.value}'>"


Base.metadata.create_all(engine)


def user_registration():
    user_name = str(input("Enter user's name: ").strip())
    user_surname = str(input("Enter user's surname: ").strip())
    user_password = str(input("Enter user's password: ").strip())
    user_age = abs(int(input("Enter user's age: ").strip()))
    table = Table('users', metadata, autoload=True)
    ins = table.insert().values(name=user_name,
                                surname=user_surname,
                                password=user_password,
                                age=user_age
                                )
    conn = engine.connect()
    conn.execute(ins)


if __name__ == '__main__':
    # user_registration()
    print(Table('users', metadata, autoload=True).columns)
    print(Table('values', metadata, autoload=True).columns)
    for _t in metadata.tables:
        print(f"Table: '{_t}'")
