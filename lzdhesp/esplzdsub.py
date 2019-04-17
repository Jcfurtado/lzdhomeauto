# ------- Iluminação ------- #
# ESP8266 NodeMCU com MicroPython
''' Requisitos
        Lampadas: 1 - lampada quente noite (se Temp < 23°C)
                  1 - lampada quente dia (se Temp < 23°C)
                  1 - lampada UV (das 7 as 10hs)
                  1 - lampada UVA-B (das 12 as 14hs)
                  1 - LED RBG noite (se Temp >= 23°C)
'''
from neopixel import NeoPixel
from machine import Pin


rgbled = NeoPixel(Pin(5), 12)  # (D1) overnight RGB LED
lpduv = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UV light
lpduva = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UVA-B light
lpdday = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) day heat lamp
lpdnight = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) night heat lamp
tempmin = 23

# --- rgb led --- #
# the number 12 is number of leds

def clear():
  for i in range(12):
    rgbled[i] = (0, 0, 0)
    rgbled.write()


def cockcrow():
    sunrise = 64,35,0
    for i in range(4 * 12):
        for j in range(12):
            rgbled[j] = (sunrise)
        rgbled.write()


def cockshut():
    sunset = 128,88,0
    for i in range(4 * 12):
        for j in range(12):
            rgbled[j] = (sunset)
        rgbled.write()


def overnight():
    night = 15,0,45
    for i in range(4 * 12):
        for j in range(12):
            rgbled[j] = (night)
        rgbled.write()


# --- controller --- #
def esplightctrl():
    if KEY == 'cockcrow':  # wawr LED
        morning()
    elif KEY == 'day':  # day lights
        day_controller()
    elif KEY == 'cockshut':  # cockshut LED
        cockshut()
    elif KEY == 'overnight':  # night lights
        night_controller()
    else:
        print('error... esp_light_controller')
        
        
def morning():
    cockcrow()    
    print("\n Cockcrow!! ON!")
    sleep(300)
    clear()
    print("\n Cockcrow!!! OFF!")


def espdayctrl():  # controller day lamps
    if lpd_hot_day == 'cold_day' :  # day heat lamp
        lpdday.on()
        return print("\n Heat lamp, ON!")
    elif lpd_hot_day == 'hot_day':
        lpdday.off()
        return print("\n Heat lamp, OFF!")
    elif uv_on == 'rooster':  # UV light
        lpduv.on()
        return print("\n UV, ON!")
    elif uv_off == 'rooster':
        lpduv.off()
        return print("\n UV, OFF!")
    elif uva_on == 'rooster':  # UVA-B light
        lpduva.on()
        return print("\n UVA-B, ON!")
    elif uva_off == 'rooster':
        lpduva.off()
        return print("\n UVA-B, OFF!")
    else:
        print('error... esp_day_controller')


def night_controller():  # controller overnight lights
    # dht / temp min
    temp = 25
    tempmin = 22
    # controller
    if hot_night == 'cold_night':  # heat lamp night
        lpdnight.on()
        return print("\n Overnight heat lamp, ON!")
    elif hot_night == 'hot_night':
        lpdnight.off()
        print("\n Overnight heat lamp, OFF!") 
        overnight()  # overnight LED
        print("\n Overnight LED light, ON!")
    else:
        clear()
        print("\n Overnight LED light, OFF!")


def evening():
    cockshut()
    print("\n Cockshut, ON!")
    sleep(300)
    clear()
    print("\n Cockshut, OFF!")

