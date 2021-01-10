import time
from mpu6050 import mpu6050
from timeit import default_timer as timer

class Gyroscope:

    def __init__(self):


        # This is our mpu6050 instance
        self.sensor = mpu6050(0x68, bus = 1)

        # These estimates come from summary output of
        # /accelerometer/gyro_calibration.py
        self.gyro_correction = {
            'x': 16.292,
            'y': 1.77,
            'z': -0.205
        }

        self.gyro_angles = {
            'x': 0,
            'y': 0,
            'z': 0
        }
        self.last_update = timer()

    def reset(self):
        self.gyro_angles = {
            'x': 0,
            'y': 0,
            'z': 0
        }
        self.last_update = timer()



    def update(self, sample_time):

        gyro_data = self.sensor.get_gyro_data()

        gyro_values = {
            'x': gyro_data['x'] + self.gyro_correction['x'],
            'y': gyro_data['y'] + self.gyro_correction['y'],
            'z': gyro_data['z'] + self.gyro_correction['z']
        }

        dt = timer() - self.last_update
        self.gyro_angles['x'] += gyro_values['x'] * dt
        self.gyro_angles['y'] += gyro_values['y'] * dt
        self.gyro_angles['z'] += gyro_values ['z'] * dt

        self.last_update = timer()
        return self.gyro_angles
