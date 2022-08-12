print('-' * 24)
print('>>> TABELA DE TIMES <<<')
print('-' * 24)
times = []
for t in range(0, 21):
    times.append(str(input('Digite um time: ')))
print('~' * 20)
print(f'Lista de times do brasileirão: {times}')
print('~' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('~' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('~' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
