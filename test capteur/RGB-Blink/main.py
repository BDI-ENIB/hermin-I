import pycom
import time
import machine

pycom.heartbeat(False)

print('Main start')

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0xC555C5)  # Blue
    time.sleep(1)
