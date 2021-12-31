# Faça um programa que leia uma frase pelo teclado e mostre:
#-Quantas vezes aparece a letra 'A'.
#-Em que posição ela aparece a primeira vez.
#-Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: '))

M = f.upper()

enc = M.count('A')
fris = M.find('A')
las = M.rfind('A')

print('Quantas vezes aparece a letra "A": {}'.format(enc))
print('Em qual posição ela aparece a primeira vez? {}'.format(fris))
print('Em que posição ela aparece a última vez? {}'.format(las))
