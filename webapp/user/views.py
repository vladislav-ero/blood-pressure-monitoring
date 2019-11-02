from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.user.forms import LoginForm
from webapp.user.models import User
from webapp.db import Session

blueprint = Blueprint('user', __name__, url_prefix='/users')
session = Session()


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    page_title = 'Authorization'
    login_form = LoginForm()
    return render_template('user/login.html',
                           page_title=page_title,
                           form=login_form
                           )


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = session.query(User).filter_by(
            username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You entered site successfuly')
            return redirect(url_for('index'))
    flash('Incorrect username or password')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You logged out successfuly')
    return redirect(url_for('index'))
