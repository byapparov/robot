from gpiozero import Robot
from time import sleep

robot = Robot(left=(14, 4), right=(17, 18))

for i in range(4):
    robot.forward()
    sleep(3)
    robot.right()
    sleep(0.5)
    robot.backward()
    sleep(3)
    robot.left()
    sleep(1)
    
