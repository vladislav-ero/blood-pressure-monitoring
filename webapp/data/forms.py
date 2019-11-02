from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    systolic_pressure = StringField('Username',
                                    validators=[DataRequired()],
                                    render_kw={"class": "form-control"}
                                    )
    dyastolic_pressure = StringField('Username',
                                     validators=[DataRequired()],
                                     render_kw={"class": "form-control"}
                                     )
    submit = SubmitField('Submit',
                         render_kw={"class": "btn btn-lg btn-primary \
                                              btn-block text-uppercase"
                                    }
                         )
