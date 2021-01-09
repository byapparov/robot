# This is an experiment with pi libraray for accelerometer
# https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050

sensor = mpu6050(0x68)

accelerometer_data = sensor.get_accel_data()


print("X: {0}, Y: {1}, Z: {2}".format(
    accelerometer_data[0],
    accelerometer_data[1],
    accelerometer_data[2]
))
