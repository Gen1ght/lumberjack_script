from PIL import ImageGrab
import pyautogui
import keyboard
import time

import windowsHandling


def goLeft():
    pyautogui.press('left')
    pyautogui.press('left')


def goRight():
    pyautogui.press('right')
    pyautogui.press('right')


window = pyautogui.getWindowsWithTitle("Lumberjack - Google Chrome")[0]
windowsHandling.switchTo(window)
goLeft()
while True:
    if keyboard.is_pressed('esc') == True:
        break
    image = ImageGrab.grab().load()
    pixels = [image[1017, 632], image[1017, 532],
              image[1017, 432], image[1017, 332],
              image[1017, 232], image[1017, 132]]

    for pixel in pixels:
        if pixel[2] < 150:
            goLeft()
        else:
            goRight()

    time.sleep(0.05)

windowsHandling.altTab()
