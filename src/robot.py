import gpiozero
import time
import gyro


from yaw_pid import YawControl


robot = Robot(right=(4, 14), left=(17, 18))
yaw_control = YawControl(
    kp = 0.1,
    ki = 0,
    kd = 10
)
gyroscope = Gyroscope()

def turn(degrees):

    error = degrees

    gyroscope.reset()
    sample_time = 0.1

    while(abs(error) > 1):

        angles = gyroscope.update(sample_time)

        error = degrees - angles['z']

        c = yaw_control.step(
            error,
            sample_time
        )
        if c > 0:
            robot.left(c)
        else:
            robot.right(-c)
        time.sleep(sample_time)


def loop():
    while(True):


if __name__ == '__main__':     # Program entrance

    try:
        turn(360)
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
