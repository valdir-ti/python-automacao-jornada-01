import pyautogui
import subprocess
import time
import pyperclip

# Pausa para dar tempo de focar no local correto
time.sleep(1)

# Abre o Google Chrome
subprocess.run(['google-chrome'])

# Aguarda o Chrome abrir (ajuste conforme necessário)
time.sleep(1)

# Usa a combinação de teclas Ctrl + L para focar na barra de endereços
pyautogui.hotkey('ctrl', 'l')

# Copia o link para a área de transferência
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyperclip.copy(link)

# Usa a combinação de teclas Ctrl + V para colar o link na barra de endereços
pyautogui.hotkey('ctrl', 'v')

# Pressiona Enter para abrir o link
pyautogui.press('enter')

time.sleep(1)
pyautogui.click(x=1322, y=431)

pyautogui.write('teste@gmail.com')

pyautogui.press('tab')

pyautogui.write('12345')

pyautogui.press('tab')

pyautogui.press('enter')