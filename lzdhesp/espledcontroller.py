import neopixel
from machine import Pin
from time import sleep


pixel = 12
np = neopixel.NeoPixel(Pin(5), pixel)

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()


def cockcrow():
    sunrise = 64,35,0
    for i in range(4 * n):
        for j in range(n):
            np[j] = (sunrise)
        np.write()


def cockshut():
    sunset = 128,88,0
    for i in range(4 * n):
        for j in range(n):
            np[j] = (sunset)
        np.write()


def overnight():
    night = 15,0,45
    for i in range(4 * n):
        for j in range(n):
            np[j] = (night)
        np.write()

