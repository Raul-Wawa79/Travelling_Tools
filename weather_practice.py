import requests

def get_weather(city, units= 'metric', api_key= '822a0e14a3c380f8c63ef19eec3fb7c8'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    for item in content['list']:
        print(item['dt_txt'], item['main']['temp'], item['weather'][0]['description'])


   #return content
print(get_weather(city= 'mataró'))

