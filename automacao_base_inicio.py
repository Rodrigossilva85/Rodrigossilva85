import pyautogui
import time

pyautogui.PAUSE = 1.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://www.youtube.com")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=506, y=171)
pyautogui.write("curso em video gustavo guanabara")
pyautogui.press("enter")