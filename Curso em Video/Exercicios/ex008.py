# Escreva um programa que leia um valor em metros e o exiba convertido em
# centimetros e milimetros.

n = float(input('Valor em metros: '))

cm = n * 100
mm = n * 1000

print('Centimetros:{}cm\nMilimetros:{}mm'.format(cm,mm))