import pyautogui
import time

# aqui vamos dar uma pausa para todos os códigos pyautogui.
pyautogui.PAUSE = 1.3

# aqui vamos pressionar a tecla windos de forma automática.
pyautogui.press("win")

# aqui vamos escrever qual o navedador vamos utilizar.
pyautogui.write("chrome")

# aqui vamos entrar no navegador.
pyautogui.press("enter")

# aqui vamos escrever o site(link) desejado.
pyautogui. write("https://www.cifraclub.com.br/")

# aqui vamos dar uma time sleep para dar tempo do navegador abrir
time.sleep(1)

# aqui vamos pressionar a tecla enter para entrar no site
pyautogui.press("enter")

# aqui estamos pegando a posição correta do mouse na tela.
pyautogui.click(x=450, y=169)

# aqui vamos escrever o nome no campo pesquisa.
pyautogui.write("pericles")

# aqui vai deixar essa posição selecionada
pyautogui.click(x=450, y=169)
# aqui vai clicar nessa posição e entrar na pasta do artista escolido.
pyautogui.click(x=503, y=207)












