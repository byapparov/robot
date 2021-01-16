from gpiozero import Robot
import time
from gyro import Gyroscope
from yaw_pid import YawControl
from ranging import UltrasonicSensor
import math

class RobotCar:

    def __init__(self):


        self.gpio_robot = Robot(right=(4, 14), left=(17, 18))
        self.yaw_control = YawControl(
            kp = 0.1,
            ki = 0.00001,
            kd = 0.002
        )
        self.gyroscope = Gyroscope()
        self.distance_sensor = UltrasonicSensor()

    def move(self, x, y):

        radians = math.atan2(y, x)
        degrees = math.degrees(radians)
        self.turn(degrees)



    def forward(self, x):

        robot_speed = 0.2
        time_to_sleep = x / 0.2

        self.gpio_robot.forward()
        sleep(time_to_sleep)

        robot.stop()


    def turn(self, degrees):

        error = degrees

        self.gyroscope.reset()
        sample_time = 0.05

        while(abs(error) > 1):

            angles = self.gyroscope.update(sample_time)

            print(angles)
            error = degrees - angles['z']

            print("Error value: {e}".format(e = error))

            c = self.yaw_control.step(
                error,
                sample_time
            )

            print("Control value: {c}".format(c = c))

            if c > 0:
                self.gpio_robot.left(c)
            else:
                self.gpio_robot.right(-c)
            time.sleep(sample_time)

    def forward_distance(self):
        self.distance_sensor.distance()
