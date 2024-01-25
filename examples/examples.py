import pyautogui
import time

def soltikla():
    pyautogui.click(button='left')
    time.sleep(0.5)
while True:
    for _ in range(16):
        soltikla()
    time.sleep(8)

