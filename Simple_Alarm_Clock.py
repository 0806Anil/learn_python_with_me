# Simple Alarm Clock

import time

alarm_time = input("Enter the time for the alarm in 'HH:MM' format: ")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("Time to wake up!")
        break
    time.sleep(60)  # Check every minute