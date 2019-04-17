# --- Control --- #
# esp8266 NodeMCU com MicroPython
# esplzdpublishdata.py

# --- Connection --- #
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.connect('Trojan.exe', 'Monalisa10')
        print('Connect: ', sta_if.isconnected())
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


# --- Lights --- #
def statelamp():
    from machine import Pin
    lpduv = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UV light
    lpduva = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UVA-B light
    ledrgb = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) RGB LED overnight
    lpdhday = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) day heat lamp
    lpdnight = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) night heat lamp
    
    lamps = ("UV", "UVA", "LED", "Heat Day", "Heat Night")
    state = (lpduv.value(), lpduva.value(), ledrgb.value(), lpdhday.value(), lpdnight.value())
    lampstate = zip(lamps, state)
    return lampstate


# --- DHT --- #
def dhtone():  # (D2 Sensor DHT lado quente)
    import dht
    from machine import Pin
    sensor = dht.DHT22(Pin(4, Pin.IN, Pin.PULL_UP))
    sensor.measure()
    temp1 = sensor.temperature()  # eg. 30.6 (°C)
    humid1 = sensor.humidity()  # eg. 25.3 (% RH)
    return temp1, humid1


def dhttwo():  # ( Sensor DHT lado frio)
    import dht
    from machine import Pin
    sensor = dht.DHT22(Pin(4, Pin.IN, Pin.PULL_UP))
    sensor.measure()
    temp2 = sensor.temperature()  # eg. 30.6 (°C)
    humid2 = sensor.humidity()  # eg. 25.3 (% RH)
    return temp2, humid2


def main(server="192.168.0.102"):
    from time import sleep
    from umqtt.simple import MQTTClient
    c = MQTTClient("umqtt_client", server)
    c.connect()
    # lado quente
    temp1, humid1 = dhtone()
    #lado frio
    temp2, humid2 = dhttwo()
    # Measurements
    all_measurements = [temp1, humid1, temp2, humid2]
    while True:
        for measurement in all_measurements:
            c.publish(b"tempone", "Temp: {}°C\nHumid: {}%\n".format(*all_measurements).encode("utf-8"))
            c.publish(b"tempone", "Light: {}".format(list(statelamp())).encode("utf-8"))
            sleep(2)
    c.disconnect()


if __name__ == "__main__":
    main()
