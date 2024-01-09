import pyautogui
import subprocess
import time
import pyperclip
import pandas

# Pausa para dar tempo de focar no local correto
time.sleep(1)

# Abre o Google Chrome
subprocess.run(['google-chrome', '--incognito'])

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

time.sleep(2)   
# Pegando a posicao do campo de email
pyautogui.click(x=1781, y=422)

# Digitando o email no campo
pyautogui.write('teste@gmail.com')

# Indo para o próximo campo
pyautogui.press('tab')

# Digitando a senha no campo de senha
pyautogui.write('12345')

# Indo para o botão
pyautogui.press('tab')

# Apertando o botao para acessar o sistema
pyautogui.press('enter')

time.sleep(2)
# importando a base de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1711, y=312)
    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')
    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    # preco_unitario
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    # obs
    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(obs) if not pandas.isna(obs) else '')
    pyautogui.press('tab')
    pyautogui.press('enter')
