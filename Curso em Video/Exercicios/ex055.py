""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
 e o menor peso lidos. """

maior_p = 0
menor_p = 0

for i in range(1, 6):
    peso = float(input('Peso da pessoa {}:'.format(i)))

    if i == 1:
        maior_p = peso
        menor_p = peso
    else:
        if peso > maior_p:
            maior_p = peso
        elif peso < menor_p:
            menor_p = peso

print('Maior peso {}\nMenor peso {}'.format(maior_p, menor_p))