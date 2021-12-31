# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

n = str(input('DIGITE SEU NOME EM LETRAS MIÚSCULAS: '))

ss = 'SILVA' in n

print('Você tem SILVA no nome? {}'.format(ss))