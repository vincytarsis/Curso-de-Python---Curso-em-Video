# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

n = int(input('Valor em metros: '))

c = n * 100
m = n * 1000

print('Centimetros:{}\nMilimetros:{}'.format(c,m))