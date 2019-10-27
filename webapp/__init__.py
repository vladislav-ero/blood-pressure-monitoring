from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, \
                        login_user, logout_user

from webapp.config import SECRET_KEY
from webapp.model import Session, User
from webapp.forms import LoginForm

session = Session()


def create_app():
    app = Flask(__name__)
    app.config.update(dict(SECRET_KEY=SECRET_KEY,
                           WTF_CSRF_SECRET_KEY=SECRET_KEY
                           )
                      )

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).filter_by(id=user_id).first()

    @app.route('/')
    def index():
        page_title = 'Blood pressure'
        return render_template('index.html', page_title=page_title)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        page_title = 'Authorization'
        login_form = LoginForm()
        return render_template('login.html',
                               page_title=page_title,
                               form=login_form
                               )

    @app.route('/process-login', methods=['POST'])
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
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You logged out successfuly')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Hello admin"
        else:
            return "You are not admin"

    return app
