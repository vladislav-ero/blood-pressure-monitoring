from flask import Flask, render_template
from flask_login import LoginManager

from webapp.config import SECRET_KEY
from webapp.db import Session
from webapp.admin.views import blueprint as admin_bluerprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


session = Session()


def create_app():
    app = Flask(__name__)
    app.config.update(dict(SECRET_KEY=SECRET_KEY,
                           WTF_CSRF_SECRET_KEY=SECRET_KEY
                           )
                      )

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_bluerprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).filter_by(id=user_id).first()

    @app.route('/')
    def index():
        page_title = 'Blood pressure'
        return render_template('index.html', page_title=page_title)

    return app
