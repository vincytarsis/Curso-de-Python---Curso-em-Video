# Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Dobro:\033[1;32m{}\033[m\nTripo:\033[1;32m{}\033[m\nRaiz quadrada:\033[1;32m{:.2f}\033[m'.format(d,t,r))
