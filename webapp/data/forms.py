from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    user_id = HiddenField('User ID',
                          validators=[DataRequired()],
                          )
    systolic_pressure = IntegerField('Systolic pressure',
                                     validators=[DataRequired()],
                                     render_kw={"class": "form-control"}
                                     )
    diastolic_pressure = IntegerField('Diastolic pressure',
                                      validators=[DataRequired()],
                                      render_kw={"class": "form-control"}
                                      )
    submit = SubmitField('Submit',
                         render_kw={"class": "btn btn-lg btn-primary \
                                              btn-block text-uppercase"
                                    }
                         )
