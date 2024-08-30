import pyautogui # serve para usar o pyautogui e fazer as automações.
import time

pyautogui.PAUSE = 1.3 # serva/p dar uma pausa na hora de digitar o link, esse tempo de meio segundo vai ajudar.
pyautogui.press("win")#  esse comando serve p/ pressionar a tecla windos do meu teclado.
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://app.ligaeducacional.com.br")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=516, y=559)
pyautogui.hotkey("ctrl", "a")

pyautogui.write("")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=516, y=559)
pyautogui.write("")
pyautogui.press("enter")
