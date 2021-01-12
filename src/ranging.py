import RPi.GPIO as GPIO
import time

MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
UNLTRASONIC_TIMEOUT = MAX_DISTANCE * 60   # calculate timeout according to the maximum measuring distance

class UltrasonicSensor:

    def __init__(self, trigger_pin = 16, echo_pin = 18):
        GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
        GPIO.setup(trigger_pin, GPIO.OUT)   # set trigPin to OUTPUT mode
        GPIO.setup(echo_pin, GPIO.IN)    # set echoPin to INPUT mode
        self.trigger_pin = 16
        self.echo_pin = 18

    def pulse_in(pin,level, UNLTRASONIC_TIMEOUT): # obtain pulse time of a pin under timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > UNLTRASONIC_TIMEOUT * 0.000001):
                return 0;
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > UNLTRASONIC_TIMEOUT * 0.000001):
                return 0;
        pulseTime = (time.time() - t0) * 1000000
        return pulseTime

    def distance():     # get the measurement results of ultrasonic module,with unit: cm
        GPIO.output(self.trigger_pin, GPIO.HIGH)      # make trigPin output 10us HIGH level
        time.sleep(0.00001)     # 10us
        GPIO.output(self.trigger_pin, GPIO.LOW) # make trigPin output LOW level
        ping_time = pulse_in(self.echo_pin, GPIO.HIGH, UNLTRASONIC_TIMEOUT)   # read plus time of echoPin
        distance = ping_time * 340.0 / 2.0 / 100.0     # calculate distance with sound speed 340m/s
        return distance
