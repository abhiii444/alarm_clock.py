# alarm_clock.py
This project is a Command-Line Alarm Clock Application in Python that allows users to set an alarm using a specific time format (HH:MM:SS AM/PM). The program continuously checks the system time and triggers an alarm sound when the specified time is reached. It supports Windows (beep sound) . 
# ⏰ Alarm Clock in Python

A simple **command-line alarm clock application** built using Python.  
This program allows users to set an alarm at a specific time and triggers a sound alert when the time is reached.

---

## 📌 Features

- ⌚ Set alarm using 12-hour format (HH:MM:SS AM/PM)
- 🔔 Plays alarm sound on trigger
- 💻 Works on Windows, macOS, and Linux
- 🧑‍💻 Beginner-friendly Python code
- 🔁 Continuously checks system time

---

## 📂 Project File

alarm.py


---

## 🛠️ Technologies Used

- Python
- `datetime` module
- `time` module
- `os` module
- `winsound` (Windows)

---

## 🚀 How to Run the Project

1. Make sure Python is installed on your system.
2. Download or clone the repository.
3. Open terminal or command prompt in the project folder.
4. Run the program:

   ```bash
   python alarm.py

---

## ⌨️ Usage Example

   Enter alarm time (HH:MM:SS AM/PM): 07:30:00 AM
   
   Alarm set for 07:30:00
   
   Wake up! Alarm ringing!

---

## 📖 How It Works
- User enters alarm time in 12-hour format.
- The input is converted to a datetime object.
- The program checks the current system time every second.
- When the current time matches the alarm time:
  - An alarm sound plays multiple times
  - Program stops after ringing

---

## Concepts Used
- Date & Time handling
- Loops
- Conditional statements
- Functions
- OS-specific operations

---

