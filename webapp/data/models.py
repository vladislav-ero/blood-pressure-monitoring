from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from webapp.db import Base
from webapp.user.models import User


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,
                     ForeignKey('users.id', ondelete='CASCADE'),
                     index=True
                     )
    created = Column(DateTime, nullable=False, default=datetime.now())
    sys_pressure = Column(Integer, nullable=False)
    dias_pressure = Column(Integer, nullable=False)

    user = relationship('User', backref='data')

    def __repr__(self):
        return f"<Value '{self.id}' user '{self.user_id}' \
            '{self.sys_pressure}/{self.dias_pressure}'>"
