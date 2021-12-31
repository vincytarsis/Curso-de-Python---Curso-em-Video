"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo."""

r1 = float(input('r1:'))
r2 = float(input('r2:'))
r3 = float(input('r3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 > r2:
    print('Triangulo on')
else:
    print('Triangulo off')
