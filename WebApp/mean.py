from datetime import datetime
import locale
import platform
from WebApp.model import db, weather_data_history

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

def average(date, month):
    average_dict = []

    for i in range(1936, 2019):
        data_x = f'{date}.{month}.{i}'
        try:
            data_x = datetime.strptime(data_x, '%d.%B.%Y')
        except ValueError:
            pass
        for temp in weather_data_history.query.filter(weather_data_history.data == data_x):

            #проверка исключения на наличие ","
            try:
                x = temp.temp.replace(',', '.')
            except AttributeError:
                x = temp.temp
            # замена , на . и на float
            average_dict.append(float(x))
        i += 1

    try:
        average_tempp = int(sum(average_dict) / len(average_dict))
        if average_tempp > 0:
            return f"На {date} {month} средняя температура за период наблюдений с 1936го года составляет [+{average_tempp}"
        if average_tempp <= 0:
            return f"На {date} {month} средняя температура за период наблюдений с 1936го года составляет [{average_tempp}"
    except ZeroDivisionError:
        print("Дата пока не выбрана. Выберите дату")
        