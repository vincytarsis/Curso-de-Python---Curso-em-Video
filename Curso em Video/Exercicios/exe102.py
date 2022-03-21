""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, quase será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cáclulo
do fatoral. """


def fatorial(n, show=False):
  """
  -> Calcula o Fatoral de um número.
  :param n: O númeor a ser calculado.
  :param show: (opcinal) Mostrar ou não a conta. 
  :return: O valor do Fatorial de um número n.
  
  """
  
  f = 1
  for c in range(n , 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print('x ', end='')
       else:
        print(' = ', end='')
     f *= c
   return f

    
#Programa principal
print(fatorial(5, show=False))
#help(fatorial)
