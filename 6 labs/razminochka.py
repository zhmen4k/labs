import pyautogui
import webbrowser
import time
import pyscreeze

webbrowser.open_new('https://eq.hsc.gov.ua/site/step')
time.sleep(3)

pyautogui.click(986, 668)

time.sleep(1)

pyautogui.click(881, 280)

time.sleep(1)

pyautogui.click(842, 500)

time.sleep(1)

pyautogui.click(870, 590)

time.sleep(1)

pyautogui.click(870, 590)

time.sleep(1)

pyautogui.click(870, 590)

def click():
    for i in range(15):
        time.sleep(0.2)
        pyautogui.click(782, 257)
    for i in range(15):
        time.sleep(0.2)
        pyautogui.click(782, 257)

def captcha():
    if pyautogui.pixel(674, 402) == (31, 63, 174):
        return True
    else:
        return False
    # print(px)
    # px = pyautogui.pixel(674, 402)

# captcha()
click()