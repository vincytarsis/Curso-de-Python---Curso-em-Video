# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digi-
# tos separados. Ex:Digite um número:1834 - unidade:4, dezena:3, centena:9, milhar:1.

n = int(input('Digite um número de 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('\033[31mUnidade:{}\033[m'.format(u))
print('\033[32mDezena :{}\033[m'.format(d))
print('\033[33mCentena:{}\033[m'.format(c))
print('\033[34mMilhar :{}\033[m'.format(m))
