""" Desenvolva um programa que leia o primero termo e a razão de uma PA. No final, mosrte
 os 10 primeiros termos dessa progressão."""

ini = int(input('Inicio:'))
ate = int(input('Até:'))
pul = int(input('Pulando de:'))

for i in range(ini, ate+1, pul):
    print(i)
