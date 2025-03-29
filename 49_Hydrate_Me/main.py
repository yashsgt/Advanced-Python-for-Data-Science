# Write a python program which reminds you of drinking water every hour. Your program can either beep or send 
# desktop notification for a specific operating system like (Windows)

import time
import win32com.client
from plyer import notification

repeat_interval = 3600

def remind_to_drink_water():
     speaker = win32com.client.Dispatch("SAPI.SpVoice")
     while True:
        
        speaker.Speak("Hydrate yourself, It's time to drink water")
        speaker.Speak("Kripya jalpaaan kijiye")
        
        # Display a desktop notification
        notification.notify(
            title="💧 Time to Drink Water!",
            message="Stay hydrated! Drink a glass of water to maintain good health.",
            timeout=10  # Notification stays for 10 seconds
            
        )
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        time.sleep(repeat_interval)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    remind_to_drink_water()
    
    




    



