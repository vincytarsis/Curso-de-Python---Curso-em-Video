# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode compra. (Considere US$1,00 = R$3,27).

r = float(input('Quantos reais você possui? '))

d = r / 3.27
print('Você pode compra:{:.2f} dolares'.format(d))