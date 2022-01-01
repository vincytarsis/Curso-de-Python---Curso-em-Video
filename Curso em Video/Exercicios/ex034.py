"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou
 iguais, o aumento é de 15%."""

sal = float(input('Digite o seu salario R$:'))

if sal >= 1250:
    print('Você ganhou 10% de aumento:\033[34mR${:.2f} reais\033[m'.format(sal + (sal * 0.1)))
else:
    print('Você ganhou 15% de aumento:\033[36mR${:.2f} reais'.format(sal + (sal * 0.15)))
