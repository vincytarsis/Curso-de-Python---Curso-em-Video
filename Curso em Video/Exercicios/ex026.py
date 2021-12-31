# Faça um programa que leia uma frase pelo teclado e mostre:
#-Quantas vezes aparece a letra 'A'.
#-Em que posição ela aparece a primeira vez.
#-Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).upper().strip()



enc = f.count('A')
fris = f.find('A') + 1
las = f.rfind('A') + 1

print('Quantas vezes aparece a letra "A": {}'.format(enc))
print('Em qual posição ela aparece a primeira vez? {}'.format(fris))
print('Em que posição ela aparece a última vez? {}'.format(las))
