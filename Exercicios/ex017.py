# Faça um programa que leia comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('\033[35mCateto oposto:\033[m'))
ca = float(input('\033[36mCateto adjacente:\033[m'))

hi = hypot(co, ca)

print('\033[4;31mA hipotenusa vai medir:{:.2f}\033[m'.format(hi))
