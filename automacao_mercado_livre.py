import pyautogui
import time

pyautogui.PAUSE =(1)

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://www.mercadolivre.com.br/")

pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=441, y=186)

pyautogui.write("celulares sansung")

pyautogui.press("enter")
