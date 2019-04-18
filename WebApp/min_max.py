from datetime import datetime

from WebApp.model import db, weather_data_history

#from WebApp import create_app
#flask_app = create_app()
#flask_app.app_context().push()

def max(data_search):
    max_temp = {}
    date_now_day = data_search.strftime("%d")
    date_now_month = data_search.strftime("%m")

    for i in range(1936, 2019):
        data_a = f'{date_now_day}.{date_now_month}.{i}'
        data_a = datetime.strptime(data_a, '%d.%m.%Y')
        for temp in weather_data_history.query.filter(weather_data_history.data == data_a):

            #поверка исключения на наличие ","
            try:
                a = temp.temp_max.replace(',', '.')
            except AttributeError:
                a = temp.temp_max
            #print(a, b)
            # замена , на . и на float
                max_temp[i] = int(float(a))
        i += 1
    #print(min(min_temp), max(max_temp))
    maximum_temp = sorted(max_temp.items(), key = lambda item:item[1], reverse = True)[0] [1]
    maximum_year = sorted(max_temp.items(), key = lambda item:item[1], reverse = True)[0] [0]

    return f"{maximum_year} году [{maximum_temp}"

def min(data_search):
    min_temp = {}
    date_now_day = data_search.strftime("%d")
    date_now_month = data_search.strftime("%m")
    
    for i in range(1936, 2019):
        data_a = f'{date_now_day}.{date_now_month}.{i}'
        data_a = datetime.strptime(data_a, '%d.%m.%Y')
        for temp in weather_data_history.query.filter(weather_data_history.data == data_a):
            #поверка исключения на наличие ","
            try:
                b = temp.temp_min.replace(',', '.')
            except AttributeError:
                b = temp.temp_min
            # замена , на . и на float
                min_temp[i] = int(float(b))
        i += 1
    minimum_temp = sorted(min_temp.items(), key = lambda item:item[1], reverse = False)[0] [1]
    minimum_year = sorted(min_temp.items(), key = lambda item:item[1], reverse = False)[0] [0]
    
    return f"{minimum_year} году [{minimum_temp}"
