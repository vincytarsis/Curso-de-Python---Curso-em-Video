""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre
a listagem de números gerados e também indique a menor e o maior valor que estão na tupla."""

#Gerar 5 números aleatórios
from random import randint
#numeros = tuple(randint(i + 1, 10) for i in range(0, 5))
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))

#Mostra os números gerados
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
#Menor valor
print(f'\nMaior valor sorteado foi {(sorted(numeros)[-1])}')# pode se usar (max(numeros))
#Maior valor
print(f'Menor valor sorteado foi {(sorted(numeros)[0])}') # podese usar (min(numeros))
