import time
import pyautogui
import keyboard


time.sleep(5)

while True:
    time.sleep(1)
    try:
        pyautogui.moveTo(x=1627, y=660)
        time.sleep(2)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        pyautogui.moveTo(x=1709, y=209)
        time.sleep(1)
        pyautogui.click(button='left', clicks=1)
        time.sleep(2)
        pyautogui.moveTo(x=1607, y=340)
        time.sleep(1)
        pyautogui.click(button='right', clicks=1)
        time.sleep(1)

    except FileNotFoundError as e:
        print(f"Erro: {e}")
        break
    # if keyboard.read_event():
    #     break
    # else:
    #     continue

