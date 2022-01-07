import importlib
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)


def pressKey(keyval):
    keyboard.press(keyval)
    keyboard.release(keyval)


def specKey(keyval):
    if keyval == 'enter':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    if keyval == 'esc':
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
    if keyval == 'back':
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)


for x in range(2):
    time.sleep(1)
    specKey("enter")
    time.sleep(2)
    specKey("back")
    time.sleep(2)
    loop("w", 5)
    loop("d", 3)
    specKey("enter")
    time.sleep(1)
    loop("d", 5)
    time.sleep(0.4)
    pressKey("s")
    time.sleep(0.4)
    specKey("enter")
    time.sleep(2)
    specKey("enter")
    time.sleep(4)
    specKey("enter")
    time.sleep(3)
    specKey("enter")
    time.sleep(0.5)
    specKey("enter")
    time.sleep(25)
    specKey("esc")
    time.sleep(1)
    print(x)
