""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

#Tuplas por extensão de 0 a 20
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vincy')
#Ler numero de 0 a 20
while True:
    res = ' '
    n = int(input('Digite de 0 a 20:'))
    while n < 0 or n > 20:
        n = int(input('Digite novamente:'))
#Mostrar por extenso
    print(f'O número digitado foi: {extenso[n]}')
    while res not in 'SN':
        res = str(input('Deseja continuar:[S/N]')).strip().upper()
    if res == 'N':
        break
print('Até a próxima!')
#Outro jeito de fazer

#while True:
#    n = int(input('Digite um número entre 0 e 20: '))
#    if 0 <= n <= 20:
#        break
#    print('Tente novamente', end='')
