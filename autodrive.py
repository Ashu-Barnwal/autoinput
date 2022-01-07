import importlib
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)


def pressKey(keyval, delay):
    keyboard.press(keyval)
    time.sleep(delay)
    keyboard.release(keyval)


for x in range(200):
    print(x)
    pressKey("w", 32)
    time.sleep(15)

    pressKey("x", 0)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(9)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(8)

# for x in range(200):
#     print(x)
#     keyboard.press('w')
#     time.sleep(32)
#     keyboard.release('w')
#     time.sleep(15)

#     keyboard.press('x')
#     keyboard.release('x')
#     time.sleep(1)
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     time.sleep(9)

#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     time.sleep(8)
