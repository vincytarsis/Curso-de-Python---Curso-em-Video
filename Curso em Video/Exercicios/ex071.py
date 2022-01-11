""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues. OBS: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1."""



res = 0
# Valor a ser sacado
print('+'*15)
print('Banco Tarsis')
print('+'*15)
while True:
    valor = float(input('Qual o valor a ser sacado:'))
# Quantidade de cedulas de cada valor a ser entregue

    float.valor1 = valor / 50
    valor2 = float.valor1[1] % 50

    print(f'Notas de 50:{valor1:.0f} notas')
    print(valor2)
