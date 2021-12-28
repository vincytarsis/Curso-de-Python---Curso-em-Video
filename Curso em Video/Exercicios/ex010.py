# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compra. (Considere US$1,00 = R$3,27).

r = float(input('Quantos reais você possui?R$ '))

d = r / 3.27

print('Você pode compra:U$ {:.2f}'.format(d))
