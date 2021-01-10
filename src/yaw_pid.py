import math

MIN_MOTOR_CONTROL = 0.5
MAX_MOTOR_CONTROL = 1


class YawControl:

    def __init__(self, kp, ki, kd):


        self.last_error = 0.0
        self.integral = 0.0

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def reset(self):
        self.int_val = 0.0



    def step(self, error, sample_time):
        self.integral = self.integral + error * sample_time;
        derivative = (error - self.last_error) / sample_time;

        control = self.kp * error + self.ki * self.integral + self.kd * derivative;
        if abs(control) < MIN_MOTOR_CONTROL:
            control = math.copysign(control, MIN_MOTOR_CONTROL)

        if abs(control) > MAX_MOTOR_CONTROL:
            control = math.copysign(control, MAX_MOTOR_CONTROL)

        self.last_error = error

        return(control)
