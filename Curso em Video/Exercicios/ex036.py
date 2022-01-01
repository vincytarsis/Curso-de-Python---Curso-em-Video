""" Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
não pode passar der 30% do salário ou então o empréstimo será negado."""

c = float(input('\033[34mQual o valor da casa:R$\033[m'))
s = float(input('\033[33mSalário do comprador:R$\033[m'))
a = float(input('\033[35mQuantos anos para pagar:\033[m'))

pm = c / (a * 12)

if pm > s - s * 0.3:
    print('\033[1;31mNegado!')
else:
    print('\033[1;32mAprovado!')


