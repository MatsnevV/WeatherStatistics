#внешний импорт
from flask import Flask, render_template
from datetime import datetime
import os

#внутрений импортpip 
from WebApp.weather_now import weather_by_city
from WebApp.model import db, weather_data
from WebApp.min_max import min
from WebApp.min_max import max
from WebApp.forms import GetDateForms

data_now = datetime.today()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        #form = GetDateForms()
        title = "WeatherStatistics"
        max_now = max(data_now)
        min_now = min(data_now)
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        if int(weather_text['temp_C']) > 0:
            weather_text = f'+{weather_text["temp_C"]}'
        #показать все данные из таблицы
        #weather_table = weatherquery.all()
        return render_template('index.html', page_title=title, weather_nows=weather_text, max_now=max_now, min_now=min_now)
    
    @app.route('/forecast')
    def forecast():
        title = "WeatherStatistics"
        max_now = max(data_now)
        min_now = min(data_now)
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        if int(weather_text['temp_C']) > 0:
            weather_text = f'+{weather_text["temp_C"]}'
        forecast_form = GetDateForms()
        return render_template('forecast.html', page_title=title, weather_nows=weather_text, max_now=max_now, min_now=min_now, form=forecast_form)

    return app
