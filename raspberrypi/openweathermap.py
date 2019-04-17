# Python program to find current  
# weather details of any city 
# using openweathermap api


def api_url():
    #Entre com sua API key
    api_key = "04e1541a44923bd07c915b83d6735b48"
    # base_url variavel para url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # ID da cidade
    city_id = 3449701
    # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    unit = "metric"
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "id=" + str(city_id) + "&mode=json&units=" + unit + "&appid=" + api_key
    return complete_url


def apidata():
    import requests
    from funtime import time_converter
    # get method of requests module 
    r = requests.get(api_url())  # return response object      
    # json method of response object
    # convert json format data into
    # python format data
    data = r.json() # Now data contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if data["cod"] != "404":
        # store the value of "main"
        idx_main = data["main"]
        # store the value corresponding
        # to the "temp" key of idx_main 
        current_temperature = idx_main["temp"]
        current_temp_max = idx_main["temp_max"]
        current_temp_min = idx_main["temp_min"]
        # store the value corresponding
        # to the "humidity" key of idx_main
        current_humidity = idx_main["humidity"]
        # store the value of "weather"
        # key in variable idx_weather
        idx_weather = data["weather"] 
        # store the value corresponding
        # to the "description" key at
        # the 0th index of idx_weather
        weather_description = idx_weather[0]["description"]
        # store the value of "dt"
        idx_dt = data["dt"]
        # store the value of "sys"
        idx_sys = data["sys"]
        current_sunrise = idx_sys["sunrise"]
        current_sunset = idx_sys["sunset"]
        # store the value of "name"
        idx_name = data["name"]
        # print following values
        print(' Cidade: ', str(idx_name),
              '\n Temperature: ', str(current_temperature),'°C',
              '\n Description = ', str(weather_description),
              '\n Humidity: ', str(current_humidity), '%',
              '\n Max: ', str(current_temp_max), '°C',
              '\n Min: ', str(current_temp_min), '°C',
              '\n Sunrise: ', time_converter(current_sunrise),
              '\n Sunset: ', time_converter(current_sunset),
              '\n Last update from the server: ', time_converter(idx_dt))
    else:
        print(' City Not Found ')
    return idx_name, current_temperature, weather_description, current_temp_max, current_temp_min, current_humidity, time_converter(current_sunrise), time_converter(current_sunset), time_converter(idx_dt)


def apisunrise():
    import requests
    url = api_url()
    r = requests.get(url)
    data = r.json()
    if data["cod"] != "404":
        idx_sys = data["sys"]
        current_sunrise = idx_sys["sunrise"]
    else:
        print('City Not Found')
    return current_sunrise


def apisunset():
    import requests
    url = api_url()
    r = requests.get(url)
    data = r.json()
    if data["cod"] != "404":
        idx_sys = data["sys"]
        current_sunset = idx_sys["sunset"]
    else:
        print('City Not Found')
    return current_sunset
