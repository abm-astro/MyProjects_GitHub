teams = ('Fortaleza', 'Ceará SC', 'Athletico-PR', 'Bragantino-SP', 'Grêmio', 'Atlético-GO', 'Palmeiras', 'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba', 'Fluminense', 'Flamengo', 'Atlético-MG', 'Sport Recife', 'Corinthians', 'Internacional', 'Botafogo', 'Goiás', 'São Paulo')
print(20*'==')
print(f'Lista ded times do Brasileirão: {teams}')
print(20*'==')
print(f'Os 5 primeiros colocados são: {teams[0:5]}')
print(20*'==')
print(f'Os últimos 4 colocados são: {teams[-4:]}')
print(20*'==')
print(f'Times em ordem alfabética: {sorted(teams)}')
print(20*'==')
print(f'O Flamengo está na {teams.index("Flamengo")+1}° posição.')