def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é {a}m².')


print('           Controle de Terrenos')
print('-' * 40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)