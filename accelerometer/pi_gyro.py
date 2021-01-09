# This is an experiment with pi libraray for accelerometer
# https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)



gyro_angles = {
    'x': 0,
    'y': 0,
    'z': 0
}

def loop():

    dt = 0.1
    while(True):
        accelerometer_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()

        print("X: {0}, Y: {1}, Z: {2}".format(
            gyro_data['x'],
            gyro_data['y'],
            gyro_data['z']
        ))

        gyro_angles['x'] += gyro_data['x'] * dt
        gyro_angles['y'] += gyro_data['y'] * dt
        gyro_angles['z'] += gyro_data['z'] * dt

        print("total X: {0}, Y: {1}, Z: {2}".format(
            gyro_angles['x'],
            gyro_angles['y'],
            gyro_angles['z']
        ))
        time.sleep(dt)

if __name__ == '__main__':     # Program entrance

    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
