# Escreva um programa que leia um valor em metros e o exiba convertido em
# centimetros e milimetros.

n = float(input('Valor em metros: '))

cm = n * 100
mm = n * 1000

print('\033[7mCentimetros:{}cm\033[m\n\033[7mMilimetros:{}mm\033[m'.format(cm,mm))