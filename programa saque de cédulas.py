print('-' *33)
print('{:^32}'.format('BH BANK'))
print('-' * 33)
valor = int(input('Qual valor você quer sacar? '))
total = valor
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
         print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('-' * 33)
print('BH BANK agradece! Tenha um bom dia!')