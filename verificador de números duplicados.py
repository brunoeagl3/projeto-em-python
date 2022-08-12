print('-' * 37)
print('- VERIFICADOR DE NÚMEROS DUPLICADOS -')
print('-' * 37)
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-' * 35)
números.sort()
print(f'Você digitou os valores {números}')
print('Fim do Programa...')