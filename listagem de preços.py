listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Agenda', 12,
            'Compasso', 9.99,
            'Mochila', 120.55,
            'Canetas', 22.30,
            'Livro', 35.90,
            'Marcador', 5.75)
print('-' * 43)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 43)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 43)