# ============================
# scheduler.py
# ============================
import time
import moisture_sensor  # Ensure this module has a `read_moisture` function
import pump_control  # Ensure this module has an `activate_pump` function
import config  # Ensure this module defines `MOISTURE_THRESHOLD` and `CHECK_INTERVAL`
from logger import log_event

def run_scheduler():
    '''Scheduler that checks moisture and waters plant if dry.'''
    while True:
        try:
            moisture_level = moisture_sensor.read_moisture()
            if moisture_level < config.MOISTURE_THRESHOLD:
                log_event(f"Moisture low ({moisture_level}). Watering plant.")
                pump_control.activate_pump()
            else:
                log_event(f"Moisture sufficient ({moisture_level}). No watering.")
            time.sleep(config.CHECK_INTERVAL)
        except Exception as e:
            log_event(f"Error occurred: {e}")
            time.sleep(config.CHECK_INTERVAL)
