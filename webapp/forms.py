from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={"class": "form-control"}
                           )
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"class": "form-control"}
                             )
    submit = SubmitField('Submit',
                         render_kw={"class": "btn btn-lg btn-primary \
                                              btn-block text-uppercase"
                                    }
                         )
