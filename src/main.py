from robot import RobotCar


if __name__ == '__main__':     # Program entrance

    try:
        robot = RobotCar()


        robot.move(0.5 , 0.5)

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
