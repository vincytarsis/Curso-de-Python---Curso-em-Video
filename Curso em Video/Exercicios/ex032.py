"""Faça um progrma que leia um ano qualquer e mostre se ele é 'BISSEXTO'."""
from datetime import date

a = int(input('Digite um ano ou coloque 0 para analisar o ano atual:'))

cor = {'azul': '\033[34m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m'}

if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{}{} Bissexto'.format(a, cor['amarelo'], a))
else:
    print('{}{}Normal'.format(a, cor['vermelho'], a))

