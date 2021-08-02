from pynput.keyboard import Key, Controller
import keyboard
import time

keyb = Controller()

time.sleep(5)

while True:
    keyb.press('f')
    keyb.release('f')
    time.sleep(0.1)
    
    if keyboard.is_pressed(';'):
        break
