from robot import RobotCar


def main():

    robot = RobotCar()
    robot.move(0.2, 0.5)





if __name__ == '__main__':     # Program entrance

    try:
        main()

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
