""" Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre os (com
 idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
 contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """

from datetime import datetime

# Ler nome
pessoa = {'nome': str(input('Nome:'))}
ano_nascimento = int(input('Ano de Nascimento:'))
ano_atual = datetime.now().year
pessoa['idade'] = ano_atual - ano_nascimento

# Ler carteira de trabalho
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] == 0:
    print('=-' * 30)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')

# Ano de contratação
else:
    pessoa['ano_cont'] = int(input('Ano de Contratação:'))
    # Salario
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (((pessoa['ano_cont'] + 35) - ano_atual) + pessoa['idade'])
    # Mostre idade e o ano de aposentadoria
    for k, v in pessoa.items():
        print(f'-{k} tem o valor {v}')
