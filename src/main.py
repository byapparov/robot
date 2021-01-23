from robot import RobotCar
from time import sleep

def main():

    robot = RobotCar()
    while True:

        forward_space = robot.forward_distance()
        if forward_space > 1:
            robot.move(0.5, 0)
        elif forward_space > 0.4:
            robot.move(forward_space - 0.45, 0)
        else:
            robot.move(-0.1, 0.1)


if __name__ == '__main__':     # Program entrance

    try:
        main()

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
