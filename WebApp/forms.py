from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 

# сдулать проверку на исключкник даты if form.validate():
class GetDateForms(FlaskForm):
    date = TextField('День:', validators=[validators.required()])
    month = TextField('Месяц:', validators=[validators.required()])
    submit = SubmitField('покажи прогноз')
 


