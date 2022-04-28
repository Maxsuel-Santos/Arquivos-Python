try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados!')
except ZeroDivisionError:
    print('Não foi possível a divisão por zero!')
except KeyboardInterrupt:
    print('O usuário não preencheu o(s) dado(s).')
else:
    print(f'Resultado: {r:.2f}')
finally:
    print('FIM! Volte sempre!!')
