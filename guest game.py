from random import randint
print('-=' * 20)
print('        - JOGO DE ADVINHAÇÃO -')
print('-=' * 20)
computador = randint(0, 15)
print('Vou pensar em um número entre 0 e 15. Tente advinhar...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))  