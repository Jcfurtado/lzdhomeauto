# ------- Iluminação ------- #
# Raspberry Pi control rele on
# esp8266 NodeMCU with MicroPython
''' Requisitos
        Lampadas: 1 - lampada quente noite (se Temp < 22°C)
                  1 - lampada quente dia (se Temp < 22°C)
                  1 - lampada UV (das 7 as 10hs)
                  1 - lampada UVA-B (das 12 as 14hs)
                  1 - LED RBG noite (se Temp >= 22°C)
'''
# --- light phases controller
def dayphases():
    from openweathermap import apisunrise, apisunset
    from funtime import current_time, time_converter
    sunrise = time_converter(apisunrise())
    sunset = time_converter(apisunset())
    yet = current_time()
    # today
    if yet == sunrise:
        morn = 'wawr'
        return morn
    elif yet > sunrise and yet < sunset:
        day = 'day'
        return day
    elif yet == sunset:
        dusk = 'cockshut'
        return dusk
    elif yet > sunset:
        night = 'night'
        return night
    else:
        print('error... dayphases')
    

def rouse():
    from time import sleep
    led_rgb = 'on'
    print("\n LED alvorada laranja, ligado!")
    sleep(300)
    led_rgb = 'off'
    print("\n LED alvorada laranja, desligado!")
    return led_rgb
 

def day_controller():  # controller day lamps
    from time import localtime
    lt = localtime()
    rooster = lt.tm_hour
    uv_on = 7
    uv_off = 10
    uva_on = 12
    uva_off = 14
    # dht / temp min
    temp = 0
    tempmin = float(22)
    # controller
    if temp < tempmin:  # day heat lamp
        lpd_hot_day = 'on'
        print("\n Lâmpada quente diurna, ligada!")
        return lpd_hot_day
    elif temp > tempmin:
        lpd_hot_day = 'off'
        print("\n Lâmpada quente diurna, desligada!")
        return lpd_hot_day
    elif uv_on == rooster:  # UV light
        lpd_uv = 'on'
        print("\n Lâmpada UV, ligada!")
        return lpd_uv
    elif uv_off == rooster:
        lpd_uv = 'off'
        print("\n Lâmpada UV, desligada!")
        return lpd_uv
    elif uva_on == rooster:  # UVA-B light
        lpd_uva = 'on'
        print("\n Lâmpada UVA-B, ligada!")
        return lpd_uva
    elif uva_off == rooster:
        lpd_uva = 'off'
        print("\n Lâmpada UVA-B, desligada!")
        return lpd_uva
    else:
        print('error... day_controller')


def night_controller():  # controller overnight lamps
    # dht / temp min
    temp = 0
    tempmin = float(22)
    # controller
    if temp < tempmin:  # night heat lamp
        hot_night = 'on'
        print("\n Lâmpada quente noturna, ligada!")
        return hot_night
    elif temp > tempmin:
        hot_night = 'off'
        print("\n Lâmpada quente noturna, desligada!")
        return hot_night
    if temp >= tempmin:  # overnight LED
        led_rgb = 'on'
        print("\n LED noturno roxo, ligado!")
        return led_rgb
    else:
        led_rgb = 'off'
        print("\n LED noturno roxo, deligado!")
        return led_rgb


def cockshut():
    from time import sleep
    led_rgb = 'on'
    print("\n LED crepuscular laranja, ligado!")
    sleep(300)
    led_rgb = 'off'
    print("\n LED crepuscular laranja, desligado!")
    return led_rgb


def light_controller():
    if dayphases() == 'wawr':  # wawr LED
        rouse()
    elif dayphases() == 'day':  # day lights
        day_controller()
    elif dayphases() == 'night':  # night lights
        night_controller()
    elif dayphases() == 'cockshut':  # cockshut LED
        cockshut()
    else:
        print('error... light_controller')


light_controller()
