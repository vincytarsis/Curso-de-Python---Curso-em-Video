""" Faça um programa que ajude um jogador da MEGA SENA a cria palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta."""

from random import randint
from time import sleep

print('-'*30)
print('  Jogos das Mega Sena   ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie?:'))


jogos = []
lista = []
cont = 0
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*5, f'Sorteando {quant} Jogos', '-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'Boa Sorte!', '=-'*5)

