from gpiozero import DistanceSensor

class UltrasonicSensor:

    def __init__(self, echo_pin = 23, trigger_pin = 24):
        self.sensor = DistanceSensor(echo_pin, trigger_pin)

    def distance(self):     # get the measurement results of ultrasonic module,with unit: cm
        self.sensor.distance
