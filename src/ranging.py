from gpiozero import DistanceSensor

class UltrasonicSensor:

    def __init__(self, trigger_pin = 16, echo_pin = 18):
        sensor = DistanceSensor(23, 24)

    def distance():     # get the measurement results of ultrasonic module,with unit: cm
        sensor.distance
