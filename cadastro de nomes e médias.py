print('-' * 30)
print('- CADASTRO DE NOMES E MÉDIAS -')
print('-' * 30)
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar: [S/N]' ))
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 20)
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (0 p/ finalizar): '))
    if opc == 0:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}')
print('<<<  VOLTE SEMPRE!  >>>')