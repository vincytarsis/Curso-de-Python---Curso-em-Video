# Faça um programa que leia uma frase pelo teclado e mostre:
#-Quantas vezes aparece a letra 'A'.
#-Em que posição ela aparece a primeira vez.
#-Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).upper().strip()



enc = f.count('A')
fris = f.find('A') + 1
las = f.rfind('A') + 1

print('\033[37mQuantas vezes aparece a letra "A": {}\033[m'.format(enc))
print('\033[36mEm qual posição ela aparece a primeira vez? {}\033[m'.format(fris))
print('\033[34mEm que posição ela aparece a última vez? {}\033[m'.format(las))
