#!/usr/bin/env python3
########################################################################
# Filename    : MPU6050RAW.py
# Description : Read data of MPU6050.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import MPU6050
import time

mpu = MPU6050.MPU6050(
    a_xGOff=16,
    a_yGOff=1,
    a_zGOff=-0)     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3                # define an arry to store gyroscope data
def setup():
    mpu.dmp_initialize()    # initialize MPU6050

def single_measurement():
    accel = mpu.get_acceleration()
    gyro = mpu.get_rotation()

    print("Gyroscope reading:")
    print("X: {0}, Y: {1}, Z: {2}".format(
        gyro[0]/131.0,
        gyro[1]/131.0,
        gyro[2]/131.0
    ))

gyro_angles = {
    "x": 0,
    "y": 0,
    "z": 0
}
def loop():

    dt = 0.1
    while(True):

        accel = mpu.get_acceleration()      # get accelerometer data
        gyro = mpu.get_rotation()           # get gyroscope data
        # print("a/g:%d\t%d\t%d\t%d\t%d\t%d "%(accel[0],accel[1],accel[2],gyro[0],gyro[1],gyro[2]))
        #print("a/g:%.2f g\t%.2f g\t%.2f g\t%.2f d/s\t%.2f d/s\t%.2f d/s"%(accel[0]/16384.0,accel[1]/16384.0,
        #    accel[2]/16384.0,gyro[0]/131.0,gyro[1]/131.0,gyro[2]/131.0))
        print("X: {0}, Y: {1}, Z: {2}".format(
            gyro[0]/131.0,
            gyro[1]/131.0,
            gyro[2]/131.0
        ))

        gyro_angles["x"] += gyro[0]/131.0 * dt
        gyro_angles["y"] += gyro[1]/131.0 * dt
        gyro_angles["z"] += gyro[2]/131.0 * dt

        print("total X: {0}, Y: {1}, Z: {2}".format(
            gyro_angles["x"],
            gyro_angles["y"],
            gyro_angles["z"]
        ))

        time.sleep(dt)

if __name__ == '__main__':     # Program entrance
    print("Program is starting ... ")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
