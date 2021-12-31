"""Faça um progrma que leia um ano qualquer e mostre se ele é 'BISSEXTO'."""
from datetime import date

a = int(input('Digite um ano ou coloque 0 para analisar o ano atual:'))

if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} Bissexto'.format(a))
else:
    print('{} Normal'.format(a))

