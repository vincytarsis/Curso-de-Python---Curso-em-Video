""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
 em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
 no dado. """

# 4 jogares recebem números aleatorios
from random import randint
from time import sleep
from operator import itemgetter

programa = {'jogador_1': randint(1, 6),
            'jogador_2': randint(1, 6),
            'jogador_3': randint(1, 6),
            'jogador_4': randint(1, 6)
            }

ranking = []

for k, v in programa.items():
    print(f'{k} saiu com {v}', )
    sleep(1)

# Colocar o dicionário em ordem
ranking = sorted(programa.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)

# O vencedor tira o maior número
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar {v[0]} com {v[1]}.')
    sleep(1)
