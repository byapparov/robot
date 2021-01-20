from gpiozero import DistanceSensor

class UltrasonicSensor:

    def __init__(self, echo_pin = 24, trigger_pin = 23):
        self.sensor = DistanceSensor(echo_pin, trigger_pin)

    def distance(self):     # get the measurement results of ultrasonic module,with unit: cm
        return self.sensor.distance
