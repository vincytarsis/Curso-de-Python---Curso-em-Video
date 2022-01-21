# Funções
def menu():  # Menu principal
    print('--MENU PRINCIPAL--\n'
          '[1] ADICIONAR CONTA\n'
          '[2] ALTERAR SALDO\n'
          '[3] EXCLUIR CONTA\n'
          '[4] RELATÓRIOS GERENCIAIS\n'
          '[5] SAIR')


# Variaveis
conta = {}


# Titulo
print('Controle de contas corrente')
print('' * 30)

# Menu
menu()
op = int(input('Baseado no Menu acima, entre com sua opção: '))
# Opção 1
while op <= 5:
    if op == 1:
        print('--Adicionar conta--')
        conta['nome_sobrenome'] = str(input('Informe o nome e sobrenome: '))
        conta['numero_conta'] = int(input('Informe o nº da conta: '))
        while conta['numero_conta'] in conta['numero_conta']:
            print('número já registrado')

        conta['saldo'] = print('Adicione o saldo em R$:')

    else:
        print('Opção inválida')
        menu()
        op = int(input('Baseado no Menu acima, entre com sua opção:'))




