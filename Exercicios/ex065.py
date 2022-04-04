""" Crie um programa que leia vários números inteiros pelo teclado, mostre a média entre todos os valores
 e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
 a digitar valores. """

n = 1
resp = 'S'

cont = soma = 0

maior = menor = n

while resp in 'Ss':
    n = int(input('Digite um valor:').strip()[0])

    cont += 1
    soma += n

    if maior < n:
        maior = n

    if menor > n:
        menor = n

    resp = str(input('Quer PARAR [S/N]:'))

print('Total de números {}\nMedia entre  os valores {:.2f}'.format(cont, soma / (cont-1)))
print('Maior número {}\nMenor número {}'.format(maior, menor))
