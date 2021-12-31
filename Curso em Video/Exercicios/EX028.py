"""Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
deverá escrever na tela se o usúario acertou ou perdeu."""
import random
from time import sleep
n = random.randint(0, 5)

u = int(input('Tente adivinhar o número do computador: '))

if u == n:
    print('Processando...')
    sleep(2)
    print('Acertou! {}'.format(n))
else:
    print('Processando...')
    sleep(2)
    print('Perdeu! {}'.format(n))
