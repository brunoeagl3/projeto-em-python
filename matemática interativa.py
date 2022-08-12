from time import sleep
print('-=' * 25)
print('           << MATEMÁTICA INTERATIVA >>')
print('-=' * 25)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 6:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] subtrair
    [ 5 ] dividir
    [ 6 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} * {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        subtração = n1 - n2
        print('O valor de {} - {} é de {}'.format(n1, n2, subtração))
    elif opção == 5:
        divisão = n1 / n2
        print('O resultado de {} / {} é de {}'.format(n1, n2, divisão))
    print('-' * 30)
    sleep(2)
print('Fim do programa! Volte sempre!')