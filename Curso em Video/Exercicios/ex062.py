""" Melhore o DESAFIO 061, pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos. """

ini = int(input('Inicio:'))
razao = int(input('Razão PA:'))

cont = 0
a_mais = 10  # P.A. começa mostrando dos 10 primeiros termos
total = 0  # Variável de controle
calculo_PA = ini  # Estética do código

while a_mais != 0:  # 0 ele encerra o loop
    total = total + a_mais  # 10 termos que já tem e vai continuar a P.A. depois se o usuário quiser

    while cont < total:  # Ira mostra so termos da P.A.
        print('{} --> '.format(calculo_PA), end='')
        calculo_PA = calculo_PA + razao  # Calcula a P.A.
        cont = cont + 1  # Variável de controle

    print('Stop')
    a_mais = int(input('Deseja continuar? '))

print('Fim')

