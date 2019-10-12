from webapp.forms import LoginForm
from flask import Flask, render_template

from webapp.config import SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.config.update(dict(SECRET_KEY=SECRET_KEY,
                           WTF_CSRF_SECRET_KEY=SECRET_KEY
                           )
                      )

    @app.route('/')
    def index():
        page_title = 'Blood pressure'
        return render_template('index.html', page_title=page_title)

    @app.route('/login')
    def login():
        page_title = 'Authorization'
        login_form = LoginForm()
        return render_template('login.html',
                               page_title=page_title,
                               form=login_form
                               )

    return app
