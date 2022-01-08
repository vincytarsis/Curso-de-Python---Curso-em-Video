""" Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
os espaços. Ex: APOS A SOPA; A SACADA DA CASA... """

frase = str(input('Digite uma frase:').strip().upper())

plvr = frase.split()
junto = ''.join(plvr)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == junto:
    print('Forma um palíndromo')
else:
    print('Não forma um palíndromo')
