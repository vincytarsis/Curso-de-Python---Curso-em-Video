""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual delas é o maior."""


def maior(*num):
    for c in range(len(num)):
        n = num[c]
        c += 1
        if n > num:
            n = num
        for v in num:
            print(num, end=' ')
            print(f'Foram informados {len(num)} ')


maior(2, 9, 4, 5, 7, 1)
