from gpiozero import Robot
import time
from gyro import Gyroscope
from yaw_pid import YawControl
from ranging import UltrasonicSensor

class Robot:

    def __init__():


        self.gpio_robot = Robot(right=(4, 14), left=(17, 18))
        self.yaw_control = YawControl(
            kp = 0.1,
            ki = 0.00001,
            kd = 0.002
        )
        self.gyroscope = Gyroscope()
        self.untra_sonic_forward_sensor = UltrasonicSensor()

    def turn(degrees):

        error = degrees

        gyroscope.reset()
        sample_time = 0.05

        while(abs(error) > 1):

            angles = self.gyroscope.update(sample_time)

            print(angles)
            error = degrees - angles['z']

            print("Error value: {e}".format(e = error))

            c = yaw_control.step(
                error,
                sample_time
            )

            print("Control value: {c}".format(c = c))

            if c > 0:
                robot.left(c)
            else:
                robot.right(-c)
            time.sleep(sample_time)

    def forward_distance():

        untra_sonic_forward_sensor.distance()
