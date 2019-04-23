from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired

# сделать проверку на исключение даты if form.validate():
class GetDateForms(FlaskForm):
    """date = TextField('День')
    month = TextField('Месяц')"""
    submit = SubmitField('+Получи прогноз+', render_kw={"class": "btn btn-primary"})
 


