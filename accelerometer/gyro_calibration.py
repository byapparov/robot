# This is an experiment with pi libraray for accelerometer
# https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050
import time
import numpy as np

sensor = mpu6050(0x68)


def loop():

    N = 1000 # This is the size of the sample for calibration

    coordinates = ['x', 'y', 'z']
    gyro_values = {
        'x': np.zeros(N),
        'y': np.zeros(N),
        'z': np.zeros(N)
    }
    dt = 0.001
    for i in range(N):
        accelerometer_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()

        for d in coordinates:
            gyro_values[d][i] = gyro_data[d]
        time.sleep(dt)

    for d in coordinates:
        print('Mean {d}: {value}'.format(d = d, value = gyro_values[d].mean()))


if __name__ == '__main__':     # Program entrance

    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
