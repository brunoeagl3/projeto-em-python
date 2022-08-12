from datetime import datetime
dados = dict()
print('-' * 31)
print('< CADASTRO PARA APOSENTADORIA >')
print('-' * 31)
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimentos:' ))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Nº Carteira de trabalho (0 não tem: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('~' * 35)
for k, v in dados.items():
    print(f'  - {k} tem o valor = {v}')
print('~' * 35)