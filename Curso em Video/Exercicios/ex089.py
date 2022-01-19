""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente. """

lista = []
#Ler as notas
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))

    #Media
    media = (nota1 + nota2) / 2

    #Guarda em uma lista
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

#Mostrando as notas
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

#Opções de notas
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (Digite 999 para sair):'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('Volte sempre!!!')
