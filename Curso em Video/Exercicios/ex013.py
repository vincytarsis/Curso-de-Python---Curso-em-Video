# Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.

s1 = float(input('Salário antigo:R$'))

s2 = s1 + (s1 * 0.15)

print('Seu novo salário com 15% de aumento:R${:.2f}'.format(s2))