""" Crie um programa que leia vários números inteiros pelo teclado, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
 a digitar valores. """

n = 1
resp = 's'

cont = 0
soma = 0

maior = n
menor = n

while resp in 'Ss':
    n = int(input('Digite um valor:'))

    cont += 1
    soma += n

    if maior < n:
        maior = n

    if menor > n:
        menor = n

    resp = str(input('Quer PARAR [S/N]:'))

print('Total de números {}\nMedia entre  os valores {}'.format(cont - 1, soma / (cont-1)))
print('Maior número {}\nMenor número {}'.format(maior, menor))
