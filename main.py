import requests
from datetime import datetime
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")


def weather_data():
    api_key = "4856d05830439e769a7291914a8c2206"
    # user_api = os.environs['current_weather_data']
    # geolocator = Nominatim(user_agent="MyApp")
    location_i = input("Enter city name:")
    print(location_i)
    # location = geolocator.geocode(f"{location_i}")
    api_link = "https://api.openweathermap.org/data/2.5/weather?q="+f"{location_i}"+"&appid="+api_key

    # weather_params = {
    #
    #
    #     "appid": api_key,
    #     "exclude": "current,minutely,daily"
    # }
    response = requests.get(api_link)
    response.raise_for_status()
    data = response.json()
    print(data)
    temp = ((data['main']['temp'])-273.15)
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    condition_code = int(data["weather"][0]['id'])
    def rain():
        if condition_code < 700:
            return "it will rain today"
        else:
            return "It will not rain today"
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    print("-----------------------------------------------")
    print("Weather stats for -{} || ".format(location_i.upper()))
    print("-----------------------------------------------")
    print("Current temperature is: {:.2f} deg C".format(temp))
    print("Current weather description  is:", weather_description)
    print("Current humidity is:", humidity,"%")
    print("Current wind speed is:", wind_speed,"kmph")
    print(f"{rain()}")
weather_data()