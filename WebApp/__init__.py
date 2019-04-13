#внешний импорт
from flask import Flask, render_template

#внутрений импорт
from WebApp.weather_now import weather_by_city
#from WebApp.model import db, weather_data


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "WeatherStatistics"
        weather_text = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        
        #показать все данные из таблицы
        #weather_table = weatherquery.all()

        return render_template('index.html', page_title=title, weather_nows=weather_text)
    
    return app
