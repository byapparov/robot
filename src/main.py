from robot import RobotCar


if __name__ == '__main__':     # Program entrance

    try:
        robot = RobotCar()


        robot.Turn(90)

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
