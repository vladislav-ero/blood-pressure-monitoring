from sqlalchemy import Column, Integer, Text

from webapp.db import Base


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Text, nullable=False)
    time = Column(Text, nullable=False)
    sys_pressure = Column(Integer, nullable=False)
    dias_pressure = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Value '{self.id}' \
            '{self.sys_pressure}/{self.dias_pressure}'>"
