# ============================
# pump_control.py
# ============================
import RPi.GPIO as GPIO
import time
import config

def activate_pump(duration=None):
    '''Activates water pump through relay for given duration.

    Args:
        duration (float or int, optional): Duration in seconds for which the pump should remain active. Defaults to None.
    '''
    if not GPIO.getmode():
        GPIO.setmode(GPIO.BCM)
    if not hasattr(config, 'WATER_DURATION') or not isinstance(config.WATER_DURATION, (int, float)) or config.WATER_DURATION <= 0:
        raise ValueError("Invalid or undefined WATER_DURATION in config.")
    if not hasattr(config, 'RELAY_PIN') or not isinstance(config.RELAY_PIN, int):
        raise ValueError("Invalid or undefined RELAY_PIN in config.")
    
    GPIO.setup(config.RELAY_PIN, GPIO.OUT)
    GPIO.output(config.RELAY_PIN, GPIO.LOW)  # Activate relay (ON state)
    if duration:
        time.sleep(duration)
    GPIO.output(config.RELAY_PIN, GPIO.HIGH)  # Deactivate relay (OFF state, depends on wiring setup)
    GPIO.cleanup(config.RELAY_PIN)