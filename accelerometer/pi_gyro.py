# This is an experiment with pi libraray for accelerometer
# https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050

sensor = mpu6050(0x68)

accelerometer_data = sensor.get_accel_data()
gyro_data = sensor.get_gyro_data()



print("X: {0}, Y: {1}, Z: {2}".format(
    gyro_data['x'],
    gyro_data['y'],
    gyro_data['z']
))
