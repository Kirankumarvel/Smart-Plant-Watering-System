 # ============================
# moisture_sensor.py
# ============================
import RPi.GPIO as GPIO
import time
import config

def initialize_sensor():
    '''Initializes the GPIO pin for the moisture sensor.'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.MOISTURE_SENSOR_PIN, GPIO.IN)

def cleanup_sensor():
    '''Cleans up the GPIO resources.'''
    GPIO.cleanup()

def read_moisture():
    '''Reads moisture level from the GPIO pin. Returns a binary value: 1 if dry, 0 if wet.'''
    value = GPIO.input(config.MOISTURE_SENSOR_PIN)
    return value  # Binary value directly from the GPIO pin

def cleanup_gpio():
    '''Cleans up GPIO settings.'''
    GPIO.cleanup()
