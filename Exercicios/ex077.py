"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
desse mostrar, para cada palavra, quais são suas vogais. """

palavras = ('aprender', 'programa', 'linguagem', 'python'
            , 'curso', 'gratis', 'estudar', 'praticas',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')


