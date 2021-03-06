import csv
from datetime import datetime

from webapp import create_app
from webapp.model import db, weather_data_history

flask_app = create_app()
flask_app.app_context().push()

def save_weather_old_db(data, temp_max, temp_min, temp, pressure, wet):
    weather_data_exists = weather_data_history.query.filter(weather_data_history.data == data).count()
    print(weather_data_exists)
    if not weather_data_exists:
        new_weather = weather_data_history(data = data, temp_max = temp_max, temp_min =temp_min, temp = temp, pressure =pressure, wet = wet)
        db.session.add(new_weather)
        db.session.commit()

with open("moscow_old.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=';')
    for line in reader:
        data = datetime.strptime(line["data"], '%d.%m.%Y')
        temp_max = line["temp_max"]
        temp_min = line["temp_min"]
        temp = line["temp"]
        pressure = line["pressure"]
        wet = line["wet"]
        print(data, temp_max, temp_min, temp, pressure, wet)
        save_weather_old_db(data, temp_max, temp_min, temp, pressure, wet)
