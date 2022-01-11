'''cont = 0
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')'''

n = s = cont = 0

while n != 999:
    n = int(input('digite um numero:'))
    cont += 1

    if n == 999:
        break

    s += n

print(f'Acabou {s}')
