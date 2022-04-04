""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número:'))

mult = 0

for cont in range(2, num):
    if num % cont == 0:
        mult += 1

if mult == 0:
    print('É primo')
else:
    print('Não é primo')
