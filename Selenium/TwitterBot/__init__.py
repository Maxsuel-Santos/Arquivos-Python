import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Definindo o layout da interface
layout = [
    [sg.Text('E-mail ou nome de usuário:')],
    [sg.InputText(key='username')],
    [sg.Text('Senha:')],
    [sg.InputText(key='password', password_char='*')],
    [sg.Button('Login')]
]

# Criando a janela
window = sg.Window('Twitter Login', layout)

# Lendo os valores digitados pelo usuário
event, values = window.read()

# Fechando a janela
window.close()

# Pegando as informações do usuário
username = values['username']
password = values['password']

# Iniciando o webdriver
driver = webdriver.Chrome()

# Acessando a página de login do Twitter
driver.get('https://twitter.com/login')

# Esperando 5 segundos para a página carregar
time.sleep(5)

# Preenchendo o campo de e-mail ou nome de usuário
username_input = driver.find_element_by_name('text')
username_input.send_keys(username)

# Preenchendo o campo de senha
password_input = driver.find_element_by_name('session[password]')
password_input.send_keys(password)

# Clicando no botão de login
login_button = driver.find_element_by_xpath('//div[@data-testid="LoginForm_Login_Button"]/div')
login_button.click()

# Esperando 10 segundos para o login ser concluído
time.sleep(10)

# Fechando o webdriver
driver.quit()