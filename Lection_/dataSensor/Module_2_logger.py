from datetime import datetime as dt
from time import time

path = "/Users/user/Desktop/Разработчик/Python/Lection_/dataSensor"

def temperature_logger(data):
    
    time = dt.now().strftime('%H:%M')
    with  open(f'{path}/log.csv', 'a') as file:
        file.write('{}; temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with  open(f'{path}/log.csv', 'a') as file:
        file.write('{}; pressure;{}\n'
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with  open(f'{path}/log.csv', 'a') as file:
        file.write('{}; wind_speed;{}\n'
                    .format(time, data))