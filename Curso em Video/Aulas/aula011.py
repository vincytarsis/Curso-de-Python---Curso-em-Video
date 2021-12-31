'''print('\033[7:40mOlá mundo\033[m')'''

nome = 'Vincy'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}
print('Olá mundo!{}{}{}'.format(cores['azul'], nome, cores['azul']))

