""" Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
não pode passar der 30% do salário ou então o empréstimo será negado."""

casa = float(input('\033[34mQual o valor da casa:R$\033[m'))
salario = float(input('\033[33mSalário do comprador:R$\033[m'))
anos = float(input('\033[35mQuantos anos para pagar:\033[m'))

p_casa = casa / (anos * 12)

if p_casa >= (salario - salario * 0.3):
    print('\033[1;31mNegado!')
else:
    print('\033[1;32mAprovado!')


