from datetime import datetime

from WebApp.model import db, weather_data_history

from WebApp import create_app

flask_app = create_app()
flask_app.app_context().push()

def min_max(data_search):
    date_now_day = data_search.strftime("%d")
    date_now_month = data_search.strftime("%m")
    #print(date_now_day)
    #print(date_now_month)

    for i in range(1936, 2019):
        data_a = f'{date_now_day}.{date_now_month}.{i}'
        #print(data_a)
        data_a = datetime.strptime(data_a, '%d.%m.%Y')
        #print(data_a)
        #weather_data_temp_max = weather_data_history.query(temp_max).filter(weather_data_history.data == data_a)
        #weather_data_temp_min = weather_data_history.query(temp_min).filter(weather_data_history.data == data_a)
        for temp in weather_data_history.query.filter(weather_data_history.data == data_a):
            print(temp.temp_max, temp.temp_min)

            a = temp.temp_max.replace(',', '.')
            b = temp.temp_min.replace(',', '.')
            print(a, b)
            # замена , на . и на float
            if float(a) > max_temp:
                max_temp = temp.temp_max
            if float(b) < min_temp:
                min_temp = temp.temp_min
        i += 1
    return min_temp, max_temp


min_temp = 0
max_temp = 0
data_now = datetime.today()

min_max(data_now)
print(min_temp, max_temp)
