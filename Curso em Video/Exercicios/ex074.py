""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre
a listagem de números gerados e também indique a menor e o maior valor que estão na tupla."""

#Gerar 5 números aleatórios
from random import randint
menor = 0
n = tuple(randint(i + 1, 10) for i in range(0, 5))
#Mostra os números gerados
print(n)
#Menor valor
print(f'Maior valor sorteado foi {(sorted(n)[-1])}')
#Maior valor
print(f'Menor valor sorteado foi {(sorted(n)[0])}')
