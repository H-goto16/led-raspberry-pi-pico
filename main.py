import machine
import utime

led = machine.Pin(14, machine.Pin.OUT)

while True:
   led.value(1)
   print(1)
   utime.sleep(5)
   led.value(0)
   print(0)
   utime.sleep(5)
