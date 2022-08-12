from random import randint
print('-=' * 20)
print('      <<< PAR OU ÍMPAR GAME >>>')
print('-=' * 20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU! 🏆')
            v += 1
        else:
            print('Você PERDEU! 🚫')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU! 🏆')
            v += 1
        else:
            print('Você PERDEU! 🚫')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você Perdeu {v} vezes.')