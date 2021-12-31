# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente. Ex:Ana Maria de Souza
#-primeiro: Ana
#-último: Souza

n = str(input('Digite seu nome completo: ')).strip()

div = n.split()

print('Primeiro:{}'.format(div[0]))
print('Ultimo:{}'.format(div[-1]))
