# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com
# o nome "SANTO".

n = str(input('Digite o nome da sua cidade: ')).upper().strip()

cs = n.split()[0]

ss = 'SANTO' in cs
print('Sua cidade começa com Santo?:\033[1;41m{}\033[m'.format(ss))