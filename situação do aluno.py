print('-' * 30)
print('    < situação do aluno >')
print('-' * 30)
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
print('-=' * 22)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
