# boot.py -- run on boot-up
import pycom

pycom.heartbeat(False)
pycom.rgbled(0x000500)
