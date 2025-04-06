# ============================
# config.py
# ============================

# Threshold value below which watering is triggered
MOISTURE_THRESHOLD = 300  # Adjust based on testing, considering soil type and environmental conditions

# GPIO pin numbers (BCM mode)
MOISTURE_SENSOR_GPIO_PIN = 17  # GPIO pin connected to the soil moisture sensor
RELAY_GPIO_PIN = 27       # GPIO pin connected to the relay module

# Time configuration
CHECK_INTERVAL = 60 * 15  # Interval for checking soil moisture levels every 15 minutes (in seconds)
WATER_DURATION = 5        # Duration (in seconds) for which the relay will activate the pump to water the plant