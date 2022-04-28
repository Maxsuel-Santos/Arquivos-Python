print('\033[1;31m-=-\033[m' * 15)
print('=== VALIDAÇÃO DE DADOS ===')
print('\033[1;31m-=-\033[m' * 15)
sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo \033[1;30m{sexo}\033[m registrado. Obrigado!')
