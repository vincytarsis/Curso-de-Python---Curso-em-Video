""" Faça um programa que calcule a soma entre todos os números impares que são de múltiplos
de três a que se encontram no intervalo de 1 a 500."""

soma = 0
qtd = 0

for num_imp in range(1, 500+1, 2):
    if num_imp % 3 == 0:
        soma += num_imp
        qtd += 1

print('Quantidade somada:{}'.format(soma))
print('Quantidade de numeros:{}'.format(qtd))
