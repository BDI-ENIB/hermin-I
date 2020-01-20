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

value_acc_x = 0
value_acc_y = 0
value_acc_z = 0

while True:

    for i in range(0,9):
        value_acc_x = value_acc_x + sensor.acceleration[0]
        value_acc_y = value_acc_y + sensor.acceleration[1]
        value_acc_z = value_acc_z + sensor.acceleration[2]

        utime.sleep_ms(100)

    value_acc_x = value_acc_x/10
    value_acc_y = value_acc_y/10
    value_acc_z = value_acc_z/10

    print("value_acc_x:   ", value_acc_x)
    print("value_acc_y:   ", value_acc_y)
    print("value_acc_z:   ", value_acc_z)
    print('\n')
