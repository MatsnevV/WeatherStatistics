#from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests
#import csv
#from datetime import datetime
#from time import sleep
from datetime import datetime, date
from WebApp import create_app

#from WebApp.model import db, weather_data
from WebApp.model import db, weather_data

flask_app = create_app()
flask_app.app_context().push()

def get_html(url):
    #проверим на валидность cтраницу и исключим ошибки
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("сетевая ошибка")
        return False

def get_walid_int(st_rgs):
    try:
        return int(st_rgs.strip())
    except ValueError:
        return 0



def get_python_weather(month, year):
    print(f"Скачиваю: http://www.meteo-tv.ru/weather/archive/?month={month}&year={year}")
    html = get_html(f"http://www.meteo-tv.ru/weather/archive/?month={month}&year={year}")
    
    #monthly_weather = []
    #result_weather = {}

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        #all_weather = soup.find('div', class_="archive__cnt jsTableContent")

        all_weather = soup.find_all('table', class_="archive-table")[1].find_all('tr')
        #print(all_weather)
        #monthly_weather = []

        for weather in all_weather:
            #result_weather = {}
            wind = weather.find('td', class_="archive-table__wind").text
            wet = weather.find('td', class_="archive-table__wet").text
            pressure = weather.find('td', class_="archive-table__pressure").text
            temp = weather.find('td', class_="archive-table__temp").text
            
            data = weather.find('td', class_="archive-table__date").text
            #изменяем формат времени
            data = data.strip()[0:10]
            
            #print(data)
            wind_dark = weather.find('td', class_="archive-table__wind dark").text
            wet_dark = weather.find('td', class_="archive-table__wet dark").text
            pressure_dark = weather.find('td', class_="archive-table__pressure dark").text
            temp_dark = weather.find('td', class_="archive-table__temp dark").text

            #print(data,wind,wet,pressure,temp,wind_dark,wet_dark,pressure_dark,temp_dark)
            #изменил формат
            data = datetime.strptime(data, '%d.%m.%Y')
            # проверка существовании даты если нет то стоп
            if data >= datetime.now():
                print('выход')
                #print(f'{data} {datetime.now()}')
                break
            #print(f'{data} {datetime.now()}')
            #print(type(wind_dark))
            #print(wind_dark)
            wind = get_walid_int(wind)
            wet = get_walid_int(wet.strip())
            pressure = get_walid_int(pressure.strip())
            temp = get_walid_int(temp.strip())
            wind_dark = get_walid_int(wind_dark.strip())
            wet_dark = get_walid_int(wet_dark.strip())
            pressure_dark = get_walid_int(pressure_dark.strip())
            temp_dark = get_walid_int(temp_dark.strip())

            save_weather_db(data, wind, wet, pressure, temp, wind_dark, wet_dark, pressure_dark, temp_dark)
            #monthly_weather.append(result_weather)

    #return monthly_weather


def save_weather_db(data, wind, wet, pressure, temp, wind_dark, wet_dark, pressure_dark, temp_dark):
    """
    data -дата
    wind- скорость ветра м/с
    wet -валжность %
    pressure- давление мм рт.ст.
    temp -температура С*
    """
    weather_data_exists = weather_data.query.filter(weather_data.data == data).count()
    #print(weather_data_exists)
    if not weather_data_exists:
        new_weather = weather_data(data=data, wind=wind, wet=wet, pressure=pressure, temp=temp, wind_dark=wind_dark, wet_dark=wet_dark, pressure_dark=pressure_dark, temp_dark=temp_dark)
        db.session.add(new_weather)
        db.session.commit()

#result_weather_list = []
#для проверки изменить год минимальный год это 2009
date_old_year = 2009
date_now_year = int(datetime.today().year)
date_now_month = int(datetime.today().month)
#print(date_now_year)

#сделать функцию вызываемую из под init
while date_old_year <= date_now_year:
        for i in range(1, 13, 1):
            get_python_weather(i, date_old_year)
            if date_old_year >= date_now_year and i == date_now_month:
                print('выход')
                #print(f'{date_old_year} == {date_now_year} == {date_now_month}')
                break
            #result_weather_list.append()
        date_old_year += 1

"""
#запись в *.csv
with open('wundergroupCSV.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(result_weather_list)
"""

#пропадает дерево 
