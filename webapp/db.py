from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

database_url = 'postgresql://localhost/blood_pressure'
engine = create_engine(database_url)
metadata = MetaData(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    password = Column(String)
    age = Column(Integer)

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

print(Table('users', metadata, autoload=True).columns)
print(Table('values', metadata, autoload=True).columns)
for _t in metadata.tables:
    print(f"Table: '{_t}'")


def UserRegistration():
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


# if __name__ == '__main__':
#     UserRegistration()
