from robot import RobotCar


if __name__ == '__main__':     # Program entrance

    try:
        robot = RobotCar()

        distance = robot.forward_distance()
        print(distance)

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
