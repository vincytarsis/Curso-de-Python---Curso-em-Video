"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
acima do limite."""

vc = float(input('Velocidade do carro: ')) #Velocidade do carro

if vc > 80:
    print('\033[1;31;40mFoi multado, excedeu o limite de 80kh, multa à pagar:R${:.2f} reais\033[m'.format((vc - 80)*7))
else:
    print('\033[1;42mLivre de multa\033[m')