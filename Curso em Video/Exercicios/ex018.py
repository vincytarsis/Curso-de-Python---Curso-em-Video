# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

n = float(input('Entre com um angulo qualquer:'))

co = cos(radians(n))
se = sin(radians(n))
tn = tan(radians(n))

print('Valores em Cosseno:{:.2f}\nSeno:{:.2f}\nTangente:{:.2f}'.format(co,se,tn))