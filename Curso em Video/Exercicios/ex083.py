""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. """

#Digite uma expressão
n = input('Digite sua expressão:')
cont = 0
for c in n:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
    if cont < 0:
        break
#Expressão certa ou errada
'''if cont == 0:
    print('Expressão válida')
else:
    print('Expressão invalida')
    
#Guanabara

expr = str(int(input('Digite a expressão:')))
pilha =[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')'''
