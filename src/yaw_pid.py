

MIN_MOTOR_CONTROL = 0.5



class YawControl:

    def __init__(self, kp, ki, kd):

        self.int_val = 0.0
        self.last_error = 0.0
        self.integral = 0.0

        self.kp = kp
        self.ki = ki
        self.kd = kd

    def reset(self):
        self.int_val = 0.0



    def step(self, error, sample_time):
        self.integral = self.int_val + error * sample_time;
        derivative = (error - self.last_error) / sample_time;

        control = self.kp * error + self.ki * integral + self.kd * derivative;
        if abs(control) < MIN_MOTOR_CONTROL:
            control = math.copysign(control, MIN_MOTOR_CONTROL)
        self.last_error = error

        return(control)
