from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import requests


def get_html(url):
    #проверим на валидность траницу и исключим ошибки
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("сетевая ошибка")
        return False

def get_python_weather(data_histori):
    data_histori = data_histori.strftime('%Y-%m-%d')
    #print(f"https://www.wunderground.com/history/daily/ru/moscow/UUWW/date/{data_histori}")
    print("https://www.wunderground.com/history/daily/ru/moscow/UUWW/date/" + data_histori)
    html = get_html("https://www.wunderground.com/history/daily/ru/moscow/UUWW/date/" + data_histori)

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        all_weather = soup.find_all('div', class_="summary-table")
        #.findAll('tr')
        print(all_weather) 
        print(result_weather)
        for weather in all_weather:
            title = weather.find('th').text
            znach = weather.find('td').text
            result_weather.append(data_histori, title, znach)
            print(data_histori, title, znach)
        return result_weather

result_weather = []

d = timedelta(days=1)
date_now = datetime.now() 
date_string = '2019-01-01 00:00:00.000000'
date_old = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')
#date_old = datetime.datetime(2000, 1, 1, 00, 00, 00, 000000)

'''2000-01-01 00:00:00.000000'''


while date_now >= date_old:
    get_python_weather(date_now)
    date_now -= d
    print(date_now)





#def save_news(title, url, published):
#    weather_exists = weather.query.filter(News.url == url).count()
#    print(weather_exists)
#    if not news_exists:
#        new_weather = weather(title=title, url=url, published=published)
#        db.session.add(new_news)
#        db.session.commit()


