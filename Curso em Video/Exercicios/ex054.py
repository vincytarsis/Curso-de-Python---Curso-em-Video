""" Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores. """
import datetime
from datetime import date

ano_atual = date.today().year

menor = 0
maior = 0

for i in range(1, 8):
    ano_nasc = int(input('Ano de nascimento da pessoa {}:'.format(i)))
    idade = ano_atual - ano_nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('='*40 ,'\nPessoas que ainda não são maiores de idade:{}'.format(menor))
print('Pessoas que são maiores de idade:{}'.format(maior))

