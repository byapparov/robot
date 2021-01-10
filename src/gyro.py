
from mpu6050 import mpu6050

class Gyroscope:

    def __init__(self):


        # This is our mpu6050 instance
        self.sensor = mpu6050(0x68)

        # These estimates come from summary output of
        # /accelerometer/gyro_calibration.py
        self.gyro_correction = {
            'x': 16.292,
            'y': 1.77,
            'z': -0.205
        }
        self.z_angle = 0.0


    def reset(self):
        self.z_angle = 0.0


    def update(self, sample_time):

        dt = sample_time

        gyro_data = self.sensor.get_gyro_data()

        gyro_values = {
            'x': gyro_data['x'] + self.gyro_correction['x'],
            'y': gyro_data['y'] + self.gyro_correction['y'],
            'z': gyro_data['z'] + self.gyro_correction['z']
        }

        gyro_angles['x'] += gyro_values['x'] * dt
        gyro_angles['y'] += gyro_values['y'] * dt
        gyro_angles['z'] += gyro_values ['z'] * dt

        return gyro_angles['x']
