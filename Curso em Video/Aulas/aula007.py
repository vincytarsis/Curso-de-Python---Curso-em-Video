n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\nO produto é {} e a divisã é {:.3f}'.format(s,m,d), end=' ')
print('\nDivisão inteira {} e potência {}'.format(di,e))

