"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

km = float(input('Quantos Km: '))

if km <= 200:
    print('Preço a pagar:R${:.2f}'.format(km * 0.50))
else:
    print('Preço a pagar:R${:.2f}'.format(km * 0.45))