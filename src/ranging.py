from gpiozero import DistanceSensor

class UltrasonicSensor:

    def __init__(self, trigger_pin = 23, echo_pin = 24):
        self.sensor = DistanceSensor(trigger_pin, echo_pin)

    def distance(self):     # get the measurement results of ultrasonic module,with unit: cm
        self.sensor.distance
