"""Crie um programa que leia um número inteiro e mostre na tela se ele é 'PAR' ou 'ÍMPAR'."""

n = int(input('Digite um número:'))

if n % 2:
    print('\033[34mÍMPAR\033[m')
else:
    print('\033[33mPAR\033[m')
