from flask import flash, Flask, render_template, redirect, request, url_for
from flask_login import current_user, LoginManager
from flask_migrate import Migrate

from webapp.admin.views import blueprint as admin_bluerprint
from webapp.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from webapp.db import engine, Session, Base
from webapp.data.forms import DataForm
from webapp.data.models import Data
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


session = Session()


def create_app():
    app = Flask(__name__)
    app.config.update(dict(SECRET_KEY=SECRET_KEY,
                           WTF_CSRF_SECRET_KEY=SECRET_KEY,
                           SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI
                           )
                      )
    Base.metadata.create_all(engine)
    migrate = Migrate(app, Base)

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
        if current_user.is_authenticated:
            cur_user_id = current_user.get_id()
            user = session.query(User).filter_by(id=cur_user_id).first()
            data_form = DataForm(user_id=cur_user_id)
            return render_template('index.html',
                                   page_title=page_title,
                                   user=user,
                                   data_form=data_form
                                   )
        else:
            return render_template('index.html',
                                   page_title=page_title,
                                   user=None
                                   )

    @app.route('/measurement', methods=['POST'])
    def add_measurement():
        form = DataForm()
        if form.validate_on_submit():
            if session.query(User).filter_by(id=form.user_id.data).first():
                measurement = Data(user_id=form.user_id.data,
                                   sys_pressure=form.systolic_pressure.data,
                                   dias_pressure=form.diastolic_pressure.data,
                                   )

                measurement.blood_pressure_category(
                    form.systolic_pressure.data,
                    form.diastolic_pressure.data
                    )

                session.add(measurement)
                session.commit()
                flash('You entered measurement successfuly!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Error in "{getattr(form, field).label.text}": \
                        {error}')
        return redirect(request.referrer)

    return app
