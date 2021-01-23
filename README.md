# robot
2 Motor Robot with Raspberry Pi - Named Olie

<img alt = "Olie Robot" src="img/robot-front.JPG" width="50%" />

## Controlling the Robot

### Turn

`turn` function takes degrees to turn the robot.

For example to make a full turn clockwise:

<table>
  <tr>
    <th>Code</th><th>Demo</th>
  </tr>
  <tr>
    <td>

    ```python
    # main.py
    from robot import RobotCar
    robot = RobotCar()
    robot.turn(-360)
    ```

    </td>
    <td>
      <img alt = "Turning in action" src="https://user-images.githubusercontent.com/1449277/104133150-9de34e80-5379-11eb-98ca-2cf45671be51.gif" />
    </td>
  </tr>
</table>
