#from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

def get_html(url):
    #проверим на валидность cтраницу и исключим ошибки
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("сетевая ошибка")
        return False

def get_python_weather(month, year):
    print(f"Скачиваю: http://www.meteo-tv.ru/weather/archive/?month={month}&year={year}")
    html = get_html(f"http://www.meteo-tv.ru/weather/archive/?month={month}&year={year}")
    
    monthly_weather = []
    result_weather = {}

    if html:
        soup = BeautifulSoup(html, 'lxml')
        #all_weather = soup.find('div', class_="archive__cnt jsTableContent")

        all_weather = soup.find_all('table', class_="archive-table")[1].find_all('tr')

        monthly_weather = []

        for weather in all_weather:
            result_weather = {}
            wind = weather.find('td', class_="archive-table__wind").text
            wet = weather.find('td', class_="archive-table__wet").text
            pressure = weather.find('td', class_="archive-table__pressure").text
            temp = weather.find('td', class_="archive-table__temp").text
            
            data = weather.find('td', class_="archive-table__date").text
            
            wind_dark = weather.find('td', class_="archive-table__wind dark").text
            wet_dark = weather.find('td', class_="archive-table__wet dark").text
            pressure_dark = weather.find('td', class_="archive-table__pressure dark").text
            temp_dark = weather.find('td', class_="archive-table__temp dark").text

            #print(data,wind,wet,pressure,temp,wind_dark,wet_dark,pressure_dark,temp_dark)
           
            result_weather['data'] = data.strip()[0:10]
            result_weather['wind'] = wind.strip()
            result_weather['wet'] = wet.strip()
            result_weather['pressure'] = pressure.strip()
            result_weather['temp'] = temp.strip()
            result_weather['wind_dark'] = wind_dark.strip()
            result_weather['wet_dark'] = wet_dark.strip()
            result_weather['pressure_dark'] = pressure_dark.strip()
            result_weather['temp_dark'] = temp_dark.strip()

            monthly_weather.append(result_weather)

    return monthly_weather

result_weather_list = []
date_now = 2009


while date_now <= 2019:
        for i in range(1, 13, 1):
            result_weather_list.append(get_python_weather(i, date_now))
        date_now += 1

with open('wundergroupCSV.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(result_weather_list)


#print(result_weather_list[5]['data'])   

#def save_news(title, url, published):
#    news_exists = News.query.filter(News.url == url).count()
#    print(news_exists)
#    if not news_exists:
#        new_news = News(title=title, url=url, published=published)
#        db.session.add(new_news)
#        db.session.commit()
