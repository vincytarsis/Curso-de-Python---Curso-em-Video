# Faça um programa que leia a largura e a altura de uma parede em metros,calcule
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta, pinta uma área de 2m^2.

l = float(input('Largura: '))
a = float(input('Altura: '))

ar = l * a

print('Para pintar a parede, tu vai gastar:\033[4;33m{}\033[m litros de tintas'.format(ar/2))