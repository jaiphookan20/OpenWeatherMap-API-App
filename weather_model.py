import requests


def search_city():
    city=input("Enter the name of the city you wish to retrieve data for: ")
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=3003e00e266ffe045397605ddf1092d6&units=metric'.format(city)
    res=requests.get(url)
    data=res.json()
    return data






