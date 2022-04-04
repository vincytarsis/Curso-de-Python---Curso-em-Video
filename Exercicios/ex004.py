# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

n = input('Digite qualquer coisa: ')

print('\033[34mÉ numerico?',(n.isnumeric()))
print('É alpha numerico? ',n.isalnum())
print('É alpha? ',n.isalpha())
print('É da tabela ascii',n.isascii())
print('É digito',n.isdigit())
print('É decimal',n.isdecimal())
print('Todas as letras são maiusculas?', n.isupper())