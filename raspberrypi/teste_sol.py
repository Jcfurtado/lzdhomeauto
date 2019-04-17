from time import sleep, localtime

# --- light phases controller
def dayphases():
    from openweathermap import apisunrise, apisunset
    from funtime import current_time, time_converter
    sunrise = time_converter(apisunrise())
    sunset = time_converter(apisunset())
    yet = current_time()
    # today
    if yet == sunrise:
        morn = 'cockcrow'
        return morn
    elif yet > sunrise and yet < sunset:
        day = 'day'
        return day
    elif yet == sunset:
        dusk = 'cockshut'
        return dusk
    elif yet > sunset:
        night = 'overnight'
        return night
    else:
        print('error... dayphases')
    

def morning():
    led_rgb = 'on'
    print("\n Cockcrow!! ON!")
    sleep(300)
    led_rgb = 'off'
    print("\n Cockcrow!!! OFF!")
    return led_rgb


def day_controller():  # controller day lamps
    lt = localtime()
    rooster = lt.tm_hour
    uv_on = 7
    uv_off = 10
    uva_on = 12
    uva_off = 14
    # dht / temp min
    temp = 0
    tempmin = 23
    # controller
    if temp < tempmin:  # day heat lamp
        lpd_hot_day = 'on'
        print("\n Heat lamp, ON!")
        return lpd_hot_day
    elif temp > tempmin:
        lpd_hot_day = 'off'
        print("\n Heat lamp, OFF!")
        return lpd_hot_day
    elif uv_on == rooster:  # UV light
        lpd_uv = 'on'
        print("\n UV, ON!")
        return lpd_uv
    elif uv_off == rooster:
        lpd_uv = 'off'
        print("\n UV, OFF!")
        return lpd_uv
    elif uva_on == rooster:  # UVA-B light
        lpd_uva = 'on'
        print("\n UVA-B, ON!")
        return lpd_uva
    elif uva_off == rooster:
        lpd_uva = 'off'
        print("\n UVA-B, OFF!")
        return lpd_uva
    else:
        print('error... day_controller')


def night_controller():  # controller overnight lights
    # dht / temp min
    temp = 25
    tempmin = float(22)
    # controller
    if temp < tempmin:  # heat lamp night
        hot_night = 'on'
        print("\n Overnight heat lamp, ON!")
        return hot_night
    elif temp >= tempmin:
        hot_night = 'off'
        print("\n Overnight heat lamp, OFF!") 
        led_rgb = 'on'  # overnight LED
        print("\n Overnight LED light, ON!")
        return hot_night, led_rgb
    else:
        led_rgb = 'off'
        print("\n Overnight LED light, OFF!")
        return led_rgb


def evening():
    led_rgb = 'on'
    print("\n Cockshut, ON!")
    sleep(300)
    led_rgb = 'off'
    print("\n Cockshut, OFF!")
    return led_rgb


def light_controller():
    if dayphases() == 'cockcrow':  # wawr LED
        morning()
    elif dayphases() == 'day':  # day lights
        day_controller()
    elif dayphases() == 'cockshut':  # cockshut LED
        cockshut()
    elif dayphases() == 'overnight':  # night lights
        night_controller()
    else:
        print('error... light_controller')
        

light_controller()
