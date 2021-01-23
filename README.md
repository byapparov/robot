# robot
2 Motor Robot with Raspberry Pi - Named Olie


![Olie image](img/robot-front.JPG)

## Controlling the Robot

### Turn

`turn` function takes degrees to turn the robot.

For example to make a full turn clockwise do:

```python
# ...
from robot import RobotCar
robot = RobotCar()
robot.turn(-360)
```

Full sample of the code is in the `src/robot.py` file.
