# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digi-
# tos separados. Ex:Digite um número:1834 - unidade:4, dezena:3, centena:9, milhar:1.

n = str(input('Digite um número de 0 a 9999: '))

print('Unidade:{}'.format(n[3]))
print('Dezena:{}'.format(n[2]))
print('Centena:{}'.format(n[1]))
print('Milhar:{}'.format(n[0]))
