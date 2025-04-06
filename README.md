# 🌱 Smart Plant Watering System (Raspberry Pi)

This project is a DIY IoT system that automatically waters your plant (e.g. bonsai) when the soil is too dry. It uses a Raspberry Pi, GPIO pins, a soil moisture sensor, and a water pump via relay.

## 🔧 Hardware Required
- Raspberry Pi (any model with GPIO)
- Soil Moisture Sensor (capacitive preferred)
- Relay Module (to control pump safely)
- Water Pump (5V or 12V depending on setup)
- Jumper Wires
- Power Supply (separate for pump if needed)
- Optional: Water reservoir

## 🗂️ Folder Structure
```
smart-watering-system/
├── config.py
├── moisture_sensor.py
├── pump_control.py
├── scheduler.py
├── main.py
├── logger.py
├── requirements.txt
├── README.md
└── logs/
    └── watering_log.txt
```

## ⚙️ Installation
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip3 install -r requirements.txt
```

## 🧪 Running the System
```bash
python3 main.py
```
This script checks moisture every 15 mins and activates the pump if needed.

## 🔁 Auto-start on Boot (Optional)
```bash
crontab -e
```
Add:
```
@reboot python3 /home/pi/smart-watering-system/main.py &
```

## 📦 GitHub Usage
- Clone this repo to your Raspberry Pi.
- Modify `config.py` to match your sensor pins and timing.
- Commit your watering logs or improvements!

---




---

## 🧠 Project Overview
Goal: Automatically water a plant (e.g. bonsai) based on soil moisture data using a moisture sensor, Raspberry Pi GPIO pins, and a water pump.

## 🗂️ Project File Structure
Here’s a clean and scalable structure:
```
smart-watering-system/
├── main.py                   # Main execution script
├── config.py                 # Configuration file (GPIO pins, thresholds)
├── moisture_sensor.py        # Handles sensor readings
├── pump_control.py           # Controls the pump via relay
├── scheduler.py              # Handles watering schedule/timing
├── logger.py                 # Logs data for monitoring
├── requirements.txt          # List of dependencies
├── utils/
│   └── gpio_helper.py        # GPIO setup/reset utilities
├── logs/
│   └── watering_log.txt      # Log file for actions
└── README.md                 # Documentation
```

## 🐍 Python Files Needed

### `config.py`
```python
MOISTURE_THRESHOLD = 300  # Adjust as needed
MOISTURE_SENSOR_PIN = 17
RELAY_PIN = 27
CHECK_INTERVAL = 60 * 15  # Every 15 minutes
WATER_DURATION = 5  # seconds
```

### `moisture_sensor.py`
```python
import RPi.GPIO as GPIO
import time
import config

def read_moisture():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.MOISTURE_SENSOR_PIN, GPIO.IN)
    value = GPIO.input(config.MOISTURE_SENSOR_PIN)
    GPIO.cleanup()
    return value
```

### `pump_control.py`
```python
import RPi.GPIO as GPIO
import time
import config

def activate_pump(duration=config.WATER_DURATION):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.RELAY_PIN, GPIO.OUT)
    GPIO.output(config.RELAY_PIN, GPIO.LOW)  # Relay ON
    time.sleep(duration)
    GPIO.output(config.RELAY_PIN, GPIO.HIGH)  # Relay OFF
    GPIO.cleanup()
```

### `scheduler.py`
```python
import time
import moisture_sensor
import pump_control
import config
from logger import log_event

def run_scheduler():
    while True:
        moisture = moisture_sensor.read_moisture()
        if moisture < config.MOISTURE_THRESHOLD:
            log_event(f"Moisture low ({moisture}). Watering plant.")
            pump_control.activate_pump()
        else:
            log_event(f"Moisture sufficient ({moisture}). No watering.")
        time.sleep(config.CHECK_INTERVAL)
```

### `logger.py`
```python
import datetime

def log_event(message):
    with open("logs/watering_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - {message}\n")
```

### `main.py`
```python
from scheduler import run_scheduler

if __name__ == "__main__":
    run_scheduler()
```

### `requirements.txt`
```
RPi.GPIO
```

## ✅ Tips:
- Use crontab to run main.py on boot.
- Add alert system later (e.g., Telegram or email).
- Test the moisture sensor manually to calibrate the threshold value.
- Use try/except in GPIO code to prevent locking up pins.

## ✅ Installation & Setup Instructions

### 1. Update & Install Python GPIO Library
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip3 install RPi.GPIO
```
RPi.GPIO comes pre-installed on most Raspberry Pi OS, but we’re ensuring it’s there.

### 2. Clone/Copy Your Project Folder
Create a folder for the project:
```bash
mkdir ~/smart-watering-system && cd ~/smart-watering-system
```
Add these files:
- main.py
- config.py
- moisture_sensor.py
- pump_control.py
- scheduler.py
- logger.py
- requirements.txt

Also, create a logs folder:
```bash
mkdir logs
touch logs/watering_log.txt
```

### 3. Wiring Guide (BCM Mode)
**Moisture Sensor:**
- VCC → 3.3V or 5V
- GND → GND
- DATA → GPIO17

**Relay + Pump:**
- Relay IN → GPIO27
- Relay VCC → 5V
- Relay GND → GND
- Relay NO → One wire of the pump
- Pump other wire → Power supply

⚠️ Important: Use external power for pumps drawing >200mA. Never power them directly from Pi!

## 🚀 How to Run the Code

### ➤ Step 1: Run it Manually (for testing)
```bash
python3 main.py
```
This script starts an infinite loop:
- Checks moisture every X minutes (config.CHECK_INTERVAL)
- Logs data
- Waters plant if needed

### 🔁 Auto-Start on Boot (Optional)
If you want the system to start automatically:
Edit crontab:
```bash
crontab -e
```
Add at the bottom:
```bash
@reboot python3 /home/pi/smart-watering-system/main.py &
```

## 🧪 Tips for First Test
- Run main.py with print()s added temporarily in each module if you want live feedback.
- Watch the moisture reading by modifying moisture_sensor.py to print the value.

---
Made with ❤️ for nature.
