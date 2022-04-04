""" Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela: -O primeiro valor
 é maior; -O segundo valor é maior; -Não existe valor maior, os dois são iguais. """

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))

if n1 > n2:
    print('\033[31mO primeiro valor é\033[m \033[34mmaior\033[m')
elif n2 > n1:
    print('\033[31mO segundo valor é\033[m \033[34mmaior\033[m')
else:
    print('\033[31mNão existe\033[m valor maior, os dois são iguais')
