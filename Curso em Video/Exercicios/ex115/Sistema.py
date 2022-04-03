from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        #Opção para leitura de arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
