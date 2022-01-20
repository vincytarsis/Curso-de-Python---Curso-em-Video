""" Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

#Ler nome e média de um aluno
aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input('Média:'))

if aluno['média'] >= 6 and aluno['média'] <= 10:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 4 and aluno['média'] <= 5.9:
    aluno['situação'] = 'Recuperação'
elif 4 > aluno['média'] > 0:
    aluno['situação'] = 'Reprovado'
else:
    print('Valor digitado incorreto!!!\n Tente novamente:')
    aluno['média'] = float(input('Média: '))

for k, v in aluno.items():
    print(f'{k} do(a) aluno(a):{v}')
