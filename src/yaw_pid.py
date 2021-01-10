import math

# DC motor will not turn at all at low values
MIN_MOTOR_CONTROL = 0.5
# gpiozero library only supports values between 0 and 1 for movement
MAX_MOTOR_CONTROL = 1


class YawControl:
    """This is a PID controller for yaw of the robot"""

    def __init__(self, kp, ki, kd):
        self.last_error = 0.0
        self.integral = 0.0

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def reset(self):
        self.last_error = 0.0
        self.integral = 0.0


    def step(self, error, sample_time):
        """Calculates control required to minimise the error"""
        self.integral = self.integral + error * sample_time;
        derivative = (error - self.last_error) / sample_time;

        control = self.kp * error + self.ki * self.integral + self.kd * derivative;
        if abs(control) < MIN_MOTOR_CONTROL:
            control = math.copysign(MIN_MOTOR_CONTROL, control)

        if abs(control) > MAX_MOTOR_CONTROL:
            control = math.copysign(MAX_MOTOR_CONTROL, control)

        self.last_error = error

        return(control)
