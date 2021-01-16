from robot import RobotCar


if __name__ == '__main__':     # Program entrance

    try:
        robot = RobotCar()


        robot.move(1 , 1)

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
