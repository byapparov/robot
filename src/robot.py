from gpiozero import Robot
import time
from gyro import Gyroscope


from yaw_pid import YawControl


robot = Robot(right=(4, 14), left=(17, 18))
yaw_control = YawControl(
    kp = 0.75,
    ki = 0.00001,
    kd = 0.2
)
gyroscope = Gyroscope()

def turn(degrees):

    error = degrees

    gyroscope.reset()
    sample_time = 0.01

    while(abs(error) > 1):

        angles = gyroscope.update(sample_time)

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

def forward():

    return False

if __name__ == '__main__':     # Program entrance

    try:
        turn(360.0)
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
