import RPi.GPIO as GPIO
import time
import signal
import sys
import os
import json

# Configuration
FAN_PIN = 18            # BCM pin used to drive PWM fan
WAIT_TIME = 10          # [s] Time to wait between each refresh
PWM_FREQ = 25           # [kHz] 25kHz for Noctua PWM control

# Configurable fan speed
FAN_LOW = 40
FAN_HIGH = 100
FAN_OFF = 0
FAN_MAX = 100

# Set fan speed
def setFanSpeed(speed):
    fan.start(speed)
    return()

# Handle fan speed
def handleFanSpeed():
    with open('fanConf.json') as f:
        data = json.load(f)
        userspeed = data["FAN_SPEED"]
    #userspeed = open("demofile.conf", "r")
    #temp = float(getCpuTemperature())
    # Turn off the fan if temperature is below MIN_TEMP
    if userspeed == 0:
        setFanSpeed(FAN_OFF)
        print("Fan OFF") # Uncomment for testing
    # Set fan speed to MAXIMUM if the temperature is above MAX_TEMP
    if userspeed <= FAN_LOW:
        setFanSpeed(FAN_LOW)
        print("Fan LOW") # Uncomment for testing
    # Set fan speed to MAXIMUM if the temperature is above MAX_TEMP
    if FAN_LOW < userspeed <= FAN_MAX:
        setFanSpeed(userspeed)
        print("userspeed") # Uncomment for testing
    # Set fan speed to userspeed if the temperature is above MAX_TEMP
    elif userspeed > FAN_MAX:
        setFanSpeed(FAN_MAX)
        print("Fan MAX") # Uncomment for testing
    # Caculate dynamic fan speed

    return ()

try:
    # Setup GPIO pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
    fan = GPIO.PWM(FAN_PIN,PWM_FREQ)
    setFanSpeed(FAN_OFF)
    # Handle fan speed every WAIT_TIME sec
    while True:
        handleFanSpeed()
        time.sleep(WAIT_TIME)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    setFanSpeed(FAN_HIGH)
    #GPIO.cleanup() # resets all GPIO ports used by this function