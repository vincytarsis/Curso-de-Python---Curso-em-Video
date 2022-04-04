""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

jogador = {}
gols_partida = []

# Ler o nome do Jogador
jogador['nome'] = str(input('Nome do Jogador:'))

# Número de partidas jogadas
partida = (int(input(f'Quantas partidas {jogador["nome"]} jogou?')))

# Quantidade de gols marcados por partida
for cont in range(partida):
    gols_partida.append(int(input(f'    Quantos gols na partida {cont + 1}?')))

jogador['gols'] = gols_partida
jogador['total'] = sum(gols_partida)

# Mostre de 3 formas diferentes
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partida} partidas.')
for cont in range(partida):
    print(f' => Na partida {cont+1}, fez {gols_partida[cont]} gols.')
print(f'Foi um total de {sum(gols_partida)} gols')
