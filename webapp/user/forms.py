from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


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
