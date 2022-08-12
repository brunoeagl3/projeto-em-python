from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 36)
print('          JOGO DA MEGA SENA        ')
print('-' * 36)
quant = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('~' * 6, f'SORTEANDO {quant} JOGOS ', '~' * 6)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-' * 8, '< BOA SORTE! >', '-' * 8)