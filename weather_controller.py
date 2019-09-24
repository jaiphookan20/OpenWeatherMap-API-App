import requests
import weather_model
from weather_view import show_welcome
from weather_view import viewMenu

def avg_temp(data):
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print('Current Temperature : {} degree celsius'.format(temp))
    print('Description : {}'.format(description))


def minmax_temp(data):
    mintemp = data['main']['temp_min']
    maxtemp = data['main']['temp_max']
    print('Minimum Temperature : {} degree celsius'.format(mintemp))
    print('Maximum Temperature : {} degree celsius'.format(maxtemp))


def misc_weatherdata(data):
    windspeed=data['wind']['speed']
    cloudiness=data['clouds']['all']
    humid=data['main']['humidity']
    print('Wind Speed : {} meters per second'.format(windspeed))
    print('Cloudiness : {}'.format(cloudiness))
    print('Humidity : {} %'.format(humid))



def quit():
    print("Restarting Weather Application")
    show_welcome()
    main()

def main():
    show_welcome()
    
    choice = input('Enter your choice : ')
    
    if choice == '1':
        viewMenu()
        
        choose=input("Enter an option to retrieve the respective weather data: ")
        
        if choose=="1":
            data=weather_model.search_city()
            avg_temp(data)
        
        elif choose =='2':
            data=weather_model.search_city()
            minmax_temp(data)

        elif choose =='3':
            data=weather_model.search_city()
            misc_weatherdata(data)

    elif choice=="2":
        quit()

    else:
        print("Enter a valid choice")
        show_welcome
        main()
 
if __name__ == '__main__':
    main()