from getpass import getpass
import sys

from webapp import create_app
from webapp.db import Session
from webapp.user.models import User

app = create_app()
session = Session()

with app.app_context():
    username = input('Enter name:')

    if session.query(User).filter_by(username=username).count():
        print('User with same username already exists')
        sys.exit(0)

    password1 = getpass('Enter password')
    password2 = getpass('Re-enter password')

    if not password1 == password2:
        print('Passwords are not same')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    session.add(new_user)
    session.commit()
    print(f'User created with id {new_user.id}')
