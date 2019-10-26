import getpass
import os

while True:
    print("*************************************")
    print("*********Caixa eletrônico************")
    print("*************************************")

    conta_digitada = input('Digite sua conta : ')
    senha_digitada = getpass.getpass('Digite sua senha : ')

    #print(conta_digitada)
    #print(senha_digitada)

    contas_lista = {
        '0001-01': {
            'senha': '123456',
            'nome' : 'Edgar de Pontes',
            'valor': 180,
            'admin': False
        },
        '0002-01': {
            'senha': '654321',
            'nome' : 'Ana Paula',
            'valor': 100,
            'admin': False
        },
        '1111-11': {
            'senha': '123456',
            'nome' : 'Admin',
            'valor': '1000',
            'admin': True
        }
    }

    cedulas = {
        '20' : 0,
        '50' : 0,
        '100': 0
    }

    if conta_digitada in contas_lista and senha_digitada == contas_lista[conta_digitada]['senha']:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("*************************************")
        print("*********Caixa eletrônico************")
        print("*************************************")
        print('1 - Saldo')
        if contas_lista[conta_digitada]['admin']:
            print('10 - Incluir cédulas')
        opcao_digitada = input('Selecione uma opção: ')

        if opcao_digitada == '1':
            print('Seu saldo é %s ' % contas_lista[conta_digitada]['valor'])
        elif opcao_digitada == '10' and contas_lista[conta_digitada]['admin']:
            qtdo_cedulas = input('Digite a quantidade de cédulas: ')
            vlr_cedulas  = input('Digite qual cédulas vai inserir: ')
            cedulas[vlr_cedulas] += int(qtdo_cedulas)
            print(cedulas)

    else:
        print('Conta inválida')

    input('Pressione <ENTER> para continuar...')

    os.system('cls' if os.name == 'nt' else 'clear')
