"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('Digite 3 números:\n'))
n2 = int(input())
n3 = int(input())

ma = n1
me = n1
#Verificando o maior
if n2 > ma:
    ma = n2
if n3 > ma:
    ma = n3
#Verificando o menor
if n2 < me:
    me = n2
if n3 < me:
    me = n3

print('Maior:{}\nMenor:{}'.format(ma,me))

