""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A: Quantas vezes apareceu o valor 9; B: Em que posição foi digitado o primeiro valor 3; C: Quais foram os
números pares. """

# Ler 4 valores
valores =(int(input('Digite um valor:')), int(input('Digite outro valor:')),
           int(input('Digite mais um valor:')), int(input('Digite o ultimo valor:')))
# Guardar em uma tupla
# Quantas vezes aparece o valor 9
print(f'Quantas veze o 9 apareceu: {valores.count(9)} vezes')
# Posição do primeiro valor 3
if 3 in valores:
    print(f'Posição do primeiro valor 3: {valores.index(3)+1} position')
else:
    print('O valor 3 não foi digitado')
# Números pares
print('Números pares digitados: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
