#внешний импорт
from flask import Flask, render_template
from datetime import datetime
import os
from flask import request
#внутрений импорт
from WebApp.weather_now import weather_by_city
from WebApp.model import db, weather_data, weather_data_history
from WebApp.min_max import min, max
from WebApp.forms import GetDateForms
from WebApp.mean import average
#from tasks import cat_reminder

data_now = datetime.today()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/', methods=['GET', 'POST']) 
    def index():
        forecast_form = GetDateForms()
        title = "WeatherStatistics"
        max_now = max(data_now)
        min_now = min(data_now)
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        if int(weather_text['temp_C']) > 0:
            weather_nows = f'+{weather_text["temp_C"]}'
        if int(weather_text['temp_C']) <= -30:
            weather_nows_text = f'На моей мега-современной метеостанции термометр лопнул от холода. Сиди дома у печки!'
        elif int(weather_text['temp_C']) <= -15:
            weather_nows_text = f'Капитан подштанник! Сегодня ваш день!'
        elif int(weather_text['temp_C']) <= -1:
            weather_nows_text = f'Вот сейчас тебе самое время просить погодное убежище в Испании!'
        elif int(weather_text['temp_C']) <= 8:
            weather_nows_text = f'Ну, такое себе погода… Но на пробежку выйти тем не менее можно… Но в калошах.'
        elif int(weather_text['temp_C']) <= 19:
            weather_nows_text = f'Радость-то какая! Уже можно гулять в расстёгнутом пуховике (как тогда, в июне 2017го).'
        elif int(weather_text['temp_C']) <= 40:
            weather_nows_text = f'Вроде потеплело :) Но это не точно:( Рекомендую шубу и валенки далеко не убирать.'
        #показать все данные из таблицы
        #weather_table = weatherquery.all()

        date = request.args.get('date')
        month = request.args.get('month')
        average_temp = average(date, month)
        
        #reminder = cat_reminder()

        return render_template('index.html', average_temp=average_temp, page_title=title, weather_nows=weather_nows, weather_nows_text=weather_nows_text, max_now=max_now, min_now=min_now, form=forecast_form)

    return app

