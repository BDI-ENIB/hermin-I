from machine import SD
import os

sd = SD()
os.mount(sd, '/sd')

# check the content
os.listdir('/sd')
