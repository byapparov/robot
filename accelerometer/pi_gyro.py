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

gyro_correction = {'x': 16.292, 'y': 1.77, 'z': -0.205}

def loop():

    dt = 0.1
    while(True):
        accelerometer_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()

        gyro_values = {
            'x': gyro_data['x'] + gyro_correction['x'],
            'y': gyro_data['y'] + gyro_correction['y'],
            'z': gyro_data['z'] + gyro_correction['z']
        }

        print("X: {0}, Y: {1}, Z: {2}".format(
            gyro_data['x'],
            gyro_data['y'],
            gyro_data['z']
        ))

        gyro_angles['x'] += gyro_values['x'] * dt
        gyro_angles['y'] += gyro_values['y'] * dt
        gyro_angles['z'] += gyro_values ['z'] * dt

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
