from machine import Pin
import neopixel
from time import sleep

n = 12

np = neopixel.NeoPixel(Pin(5), n)

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
    
 
def alvorada():
    sunrise = 255,255,255  # rgb color
    for j in range(n):
        np[j] = (sunrise)
    np.write()
    sleep(3)
    clear()


# saida
alvorada()
