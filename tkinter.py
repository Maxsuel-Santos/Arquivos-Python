import tkinter as tk

# Define a função que será chamada quando o botão for pressionado
def buscar_hashtag():
    hashtag = entrada.get() # obtém o texto digitado pelo usuário na entrada
    print("Hashtag digitada:", hashtag) # exibe a hashtag na tela para verificar

# Cria a janela principal
janela = tk.Tk()
janela.title("Busca de Hashtag")

# Cria um rótulo para a pergunta
pergunta = tk.Label(janela, text="Digite a hashtag a ser buscada no Twitter:")
pergunta.pack()

# Cria uma entrada de texto para o usuário digitar a hashtag
entrada = tk.Entry(janela)
entrada.pack()

# Cria um botão para o usuário confirmar a busca
botao_busca = tk.Button(janela, text="Buscar", command=buscar_hashtag)
botao_busca.pack()

# Inicia o loop principal da janela
janela.mainloop()
