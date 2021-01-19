from robot import RobotCar


def main():

    robot = RobotCar()
    while True:

        print("Distance: {d}m".format(d = robot.forward_distance()))
        sleep(1)





if __name__ == '__main__':     # Program entrance

    try:
        main()

    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
