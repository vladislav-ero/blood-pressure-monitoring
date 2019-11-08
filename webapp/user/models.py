from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import Base


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    email = Column(String, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"<User '{self.username}' id{self.id}"
