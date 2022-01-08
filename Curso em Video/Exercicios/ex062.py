""" Melhore o DESAFIO 061, pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos. """

ini = int(input('Inicio:'))
razao = int(input('Razão PA:'))

termo = ini
cont = 1

while cont <= 0:
    print('{}'.format(termo), end=' → ')
    termo += razao
    cont += 1

print('Acabou')
