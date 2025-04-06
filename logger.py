# ============================
# logger.py
# ============================
import datetime
import os

# Define a constant for the timestamp format
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

  
   # Logs a message with a timestamp to watering_log.txt.
   # timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
   # Parameters:
   #    message (str): The message to log. It should be a string describing the event.
    
    #Assumptions:
    #    - The 'logs/' directory exists in the project structure.
    #    - The file 'watering_log.txt' is writable.
    
    # Logs message with timestamp to watering_log.txt.

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
os.makedirs("logs", exist_ok=True)
with open("logs/watering_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - {message}\n")