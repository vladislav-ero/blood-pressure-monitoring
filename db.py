from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://localhost/blood_pressure')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    age = Column(Integer)

    def __init__(self, name, fullname, password, age):
        self.name = name
        self.fullname = fullname
        self.password = password
        self.age = age

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.name,
                                                  self.fullname,
                                                  self.password,
                                                  self.age
                                                  )


class Values(Base):
    __tablename__ = 'values'
    id = Column(Integer, primary_key=True)
    value = Column(Text)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.id} {self.value}"


Base.metadata.create_all(engine)
