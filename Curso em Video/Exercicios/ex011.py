# Faça um programa que leia a largura e a altura de uma parede em metros,calcule
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta, pinta uma área de 2m^2.

l = int(input('Largura: '))
a = int(input('Altura: '))

ar = l * a

print('Para pintar a parede, tu vai gastar:{} latas de tintas'.format(ar/2))