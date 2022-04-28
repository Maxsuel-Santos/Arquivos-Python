from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastra uma nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
        sleep(1.75)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1.75)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(0.5)
