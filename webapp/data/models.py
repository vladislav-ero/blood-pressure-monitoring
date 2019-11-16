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
    pressure_category = Column(Integer, nullable=True)

    user = relationship('User', backref='data')

    def blood_pressure_category(self, systolic_pressure, diastolic_pressure):
        if systolic_pressure <= 120 and diastolic_pressure <= 80:
            self.pressure_category = 0  # Normal
            return
        elif 120 < systolic_pressure <= 129 and diastolic_pressure < 80:
            self.pressure_category = 1  # Elevated
            return
        elif 130 <= systolic_pressure <= 139 or 80 <= diastolic_pressure <= 89:
            self.pressure_category = 2  # High blood pressure (stage 1)
            return
        elif systolic_pressure >= 190 or diastolic_pressure >= 120:
            self.pressure_category = 4  # Hypertensive crisis
            return
        elif 140 <= systolic_pressure < 190 or 90 <= diastolic_pressure < 120:
            self.pressure_category = 3  # High blood pressure (stage 2)
            return

    def __repr__(self):
        return f"<Value '{self.id}' user '{self.user_id}' \
            '{self.sys_pressure}/{self.dias_pressure}'>"
