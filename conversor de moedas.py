print('  >> CONVERSOR DE MOEDAS <<')
print('-' * 30)
real = float(input('Quanto você quer converter? R$'))
dolar = real / 5.13
euro = real / 5.31
libra = real / 6.17
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2F} e £{:.2f}'.format(real, dolar, euro, libra))
