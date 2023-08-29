import func
from formating_strings import Color

cities = [
    'Москва',
    'Красноярск',
    'Новосибирск',
    'Томск'
]

for city in cities:
    print(f'''Погода в городе {Color.BOLD + Color.CYAN + city + Color.END}: 
{func.what_weather(city)}''')
