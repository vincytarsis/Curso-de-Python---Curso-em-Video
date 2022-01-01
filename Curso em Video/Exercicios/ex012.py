# Faça um algoritmo que leia o preço de um produto e mostre  seu novo
# preço, com 5% de desconto.

p1 = float(input('\033[31mPreço cheio:R$\033[m'))

p2 = p1 - (p1 * 0.05)

print('Preço com 5% desconto:\033[1;32mR${:.2f}'.format(p2))

