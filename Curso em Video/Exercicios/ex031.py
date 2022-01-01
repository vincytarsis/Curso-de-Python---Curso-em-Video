"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

km = float(input('Quantos Km: '))

if km <= 200:
    print('Preço a pagar:R${}{:.2f}{}'.format('\033[4;32m',km * 0.50,'\033[m'))
else:
    print('Preço a pagar:R${}{:.2f}{}'.format('\033[4;33m',km * 0.45,'\033[m'))