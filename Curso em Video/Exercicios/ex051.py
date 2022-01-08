""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
 os 10 primeiros termos dessa progressão."""

ini = int(input('Inicio:'))
raz = int(input('Razão:'))
decimo = ini + (10 - 1) * raz

for i in range(ini, decimo + raz, raz):
    print('{} '.format(i), end='→ ')
print('Acabou!')
