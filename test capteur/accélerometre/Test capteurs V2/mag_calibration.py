from machine import I2C, Pin
from mpu9250 import MPU9250
from ak8963 import AK8963

i2c = I2C(0)

ak8963 = AK8963(i2c)
offset, scale = ak8963.calibrate(count=256, delay=200)

sensor = MPU9250(i2c, ak8963=ak8963)
