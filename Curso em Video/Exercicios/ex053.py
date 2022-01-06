""" Crie um programa que leia uma frase qualquer e diga se ela é um palindroma, desconsiderando
os espaços. Ex: APOS A SOPA; A SACADA DA CASA... """

aux = str(input('Digite uma frase:').strip().upper())
plvr = aux.strip()
frase = ''.join(plvr)
tamanho = len(frase)-1
inverso = ''

for i in range(tamanho, -1, -1):
    inverso += frase[i]

print('O inverso de {} é {}'.format(frase, inverso))

if frase == inverso:
    print('Forma um palíndromo')
else:
    print('Não forma um palíndromo')
