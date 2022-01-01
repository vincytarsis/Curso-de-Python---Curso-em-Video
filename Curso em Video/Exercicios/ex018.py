# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

n = float(input('\033[41mEntre com um angulo qualquer:\033[m'))

co = cos(radians(n))
se = sin(radians(n))
tn = tan(radians(n))

print('\033[7;41mValores em Cosseno:{:.2f}\033[m\n\033[7;42mSeno:{:.2f}\033[m\n\033[43mTangente:{:.2f}\033[m'.format(co,se,tn))