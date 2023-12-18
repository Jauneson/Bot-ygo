import pyautogui
import random
import time
from pynput.keyboard import Key, Controller


screenWidth, screenHeight = pyautogui.size()
print("Screen Width: " + str(screenWidth))
print("Screen Height: " + str(screenHeight))

print("start waiting.....")
time.sleep(3)
print("stop waiting")

time.sleep(4)

keyboard = Controller()

for i in range(20):
    print("loop " + str(i+1))
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(1)

    keyboard.press('y')
    time.sleep(0.5)
    keyboard.release('y')

    time.sleep(1)

    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(7)

    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(3)

    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(35)

    pyautogui.moveTo(1030, 500)
    time.sleep(0.5)

    for j in range(2):
        keyboard.press(Key.enter)
        time.sleep(0.5)
        keyboard.release(Key.enter)
        time.sleep(0.5)

    keyboard.press(Key.left)
    time.sleep(0.5)
    keyboard.release(Key.left)

    time.sleep(0.5)

    for k in range(5):
        keyboard.press(Key.enter)
        time.sleep(0.5)
        keyboard.release(Key.enter)
        time.sleep(0.5)

    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(1)

print("ending script")