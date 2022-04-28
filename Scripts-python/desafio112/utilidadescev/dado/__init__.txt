def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.isalnum() or entrada.isprintable() or entrada == '':
            print(f'\033[1;4;31mERRO: \033[1;4;30m\"{entrada}\"\033[m\033[1;4;31m é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
