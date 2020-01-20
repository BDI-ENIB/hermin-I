import utime
from machine import I2C, Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

'''
#pour les valeurs en g, deg/s and uT
i2c = I2C(0)
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)

print("MPU9250 id: " + hex(sensor.whoami))

'''
#m/s^2, rad/s and uT
i2c = I2C(0)
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print("acc(ms-2):    ", sensor.acceleration)
    print("gyro(rads-1): ", sensor.gyro)
    print("mag(mt):      ", sensor.magnetic)
    print('\n')

    utime.sleep_ms(1000)
