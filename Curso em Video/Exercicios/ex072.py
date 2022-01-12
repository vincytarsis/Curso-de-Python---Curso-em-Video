""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

#Tuplas por extensão de 0 a 20
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseis', 'dessete', 'dezoito', 'dezenove', 'vinte')

#Ler numero de 0 a 20
n = int(input('Digite de 0 a 20:'))
while n < 0 or n > 20:
    n = int(input('Digite novamente:'))
#Mostrar por extenso
print(f'O número digitado foi: {extenso[n]}')