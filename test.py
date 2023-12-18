import pyautogui
import random
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(4)
pyautogui.moveTo(1030, 500)

   
for j in range(2):
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    time.sleep(0.5)