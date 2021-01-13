from flask_wtf import FlaskForm
from wtforms.fields import (StringField,
                    DateField,
                    TimeField,
                    TextAreaField,
                    BooleanField,
                    SubmitField)
from wtforms.validators import DataRequired, Length
from wtforms.widgets.html5 import DateInput, TimeInput

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start Date", [DataRequired()], widget=DateInput())
    start_time = DateField("Start Time", [DataRequired()], widget=TimeInput())
    end_date = DateField("End Date", [DataRequired()], widget=DateInput())
    end_time = DateField("End Time", [DataRequired()], widget=TimeInput())
    description = TextAreaField('Description', validators=[DataRequired()])
    private = BooleanField('Private')
    submit = SubmitField("Create an appointment")
