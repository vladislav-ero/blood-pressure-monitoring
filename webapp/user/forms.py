from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User
from webapp.db import Session

session = Session()


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()],
                           render_kw={"class": "form-control"}
                           )
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw={"class": "form-control"}
                             )
    remember_me = BooleanField('Remember me',
                               default=True,
                               render_kw={"class": "form-check-input"}
                               )
    submit = SubmitField('Submit',
                         render_kw={"class": "btn btn-lg btn-primary \
                                              btn-block text-uppercase"
                                    }
                         )


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()],
                           render_kw={"class": "form-control"}
                           )
    email = StringField('Email',
                        validators=[DataRequired(), Email()],
                        render_kw={"class": "form-control"}
                        )
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw={"class": "form-control"}
                             )
    password2 = PasswordField('Repeat password',
                              validators=[DataRequired(), EqualTo('password')],
                              render_kw={"class": "form-control"}
                              )
    submit = SubmitField('Submit',
                         render_kw={"class": "btn btn-lg btn-primary \
                                              btn-block text-uppercase"
                                    }
                         )

    def validate_username(self, username):
        if (session.query(User).filter_by(username=username.data).count()):
            raise ValidationError('User with same name already exists')

    def validate_email(self, email):
        if (session.query(User).filter_by(email=email.data).count()):
            raise ValidationError('User with same email already exists')
