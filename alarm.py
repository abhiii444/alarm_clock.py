import datetime
import time
import os

# Function to play alarm sound
def play_alarm():
    try:
        # For Windows (plays default beep sound)
        duration = 1000  # milliseconds
        freq = 440  # Hz
        import winsound
        winsound.Beep(freq, duration)
    except:
        # Linux / MacOS fallback
        os.system("say 'Alarm ringing!'")  # macOS voice alert
        print("\a")  # Console beep

# Take alarm time input
alarm_time = input("Enter alarm time (HH:MM:SS AM/PM): ")

# Convert string to datetime format
try:
    alarm_datetime = datetime.datetime.strptime(alarm_time, "%I:%M:%S %p")
    print("Alarm set for", alarm_datetime.time())
except ValueError:
    print("Invalid format! Use HH:MM:SS AM/PM")
    exit()

# Check time continuously
while True:
    now = datetime.datetime.now().time().strftime("%I:%M:%S %p")
    if now == alarm_time:
        print("Wake up! Alarm ringing!")
        # Play sound multiple times
        for i in range(5):
            play_alarm()
            time.sleep(1)
        break

    time.sleep(1)
