import neopixel
from machine import Pin
from time import sleep

n = 12

r = 106
g = 90
b = 205
wait = 1

np = neopixel.NeoPixel(Pin(5), n)

def alvorada():
    sunrise = 64,35,0
    for i in range(4 * n):
        for j in range(n):
            np[j] = (sunrise)
        np.write()
        sleep(300)
        clear()


def crepusculo():
    sunset = 128,88,0
    for i in range(4 * n):
        for j in range(n):
            np[j] = (sunset)
        np.write()
        sleep(300)
        clear()


def noite():
    night = 15,0,45
    for i in range(4 * n):
        for j in range(n):
            np[j] = (night)
        np.write()
        sleep(300)
        clear()


def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
    
    
def bounce(r, g, b, wait):
    for i in range(4 * n):
        for j in range(n):
            np[j] = (r, g, b)
        if (i // n) % 2 == 0:
          np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        sleep(wait)
    

def cycle(r, g, b, wait):
  for i in range(4 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    sleep(wait)


def wheel(pos):
#  Input a value 0 to 255 to get a color value.
#  The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)


def rainbow_cycle():
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    sleep(0.1)


clear()