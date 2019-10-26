import getpass
import os

contas_lista = {
    '0001-01': {
        'senha': '123456',
        'nome': 'Edgar de Pontes',
        'valor': 180,
        'admin': False
    },
    '0002-01': {
        'senha': '654321',
        'nome': 'Ana Paula',
        'valor': 100,
        'admin': False
    },
    '1111-11': {
        'senha': '123456',
        'nome': 'Admin',
        'valor': '1000',
        'admin': True
    }
}

cedulas = {
    '20': 5,
    '50': 5,
    '100': 5
}

def main():
    cabecalho()

    conta_autenticada = get_conta_autenticada()
    if conta_autenticada:
        limpar()

        cabecalho()
        opcao_digitada = get_opcao_digitada(conta_autenticada)
        if opcao_digitada == '1':
            print('Seu saldo é %s ' % contas_lista[conta_autenticada]['valor'])

        elif opcao_digitada == '2':
            valor_do_saque = input('Qual o valor do saque: ')
            valor_do_saque_int = int(valor_do_saque)

            cedulas_para_usuario = {}

            if valor_do_saque_int // 100 > 0 and valor_do_saque_int // 100 <= cedulas['100']:
                cedulas_para_usuario['100'] = valor_do_saque_int // 100
                valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 100 * 100

            if valor_do_saque_int // 50 > 0 and valor_do_saque_int // 50 <= cedulas['50']:
                cedulas_para_usuario['50'] = valor_do_saque_int // 50
                valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 50 * 50

            if valor_do_saque_int // 20 > 0 and valor_do_saque_int // 20 <= cedulas['20']:
                cedulas_para_usuario['20'] = valor_do_saque_int // 20
                valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 20 * 20

            if valor_do_saque_int != 0:
                print('Não à notas disponiveis para saque ')
            else:
                for retirada in cedulas_para_usuario:
                    cedulas[retirada] -= cedulas_para_usuario[retirada]
                print('Pegue as notas! ')
                print(cedulas_para_usuario)

        elif opcao_digitada == '10' and contas_lista[conta_autenticada]['admin']:
            qtdo_cedulas = input('Digite a quantidade de cédulas: ')
            vlr_cedulas = input('Digite qual cédulas vai inserir: ')
            cedulas[vlr_cedulas] += int(qtdo_cedulas)
            print(cedulas)

    else:
        print('Conta inválida')

def cabecalho():
    print("*************************************")
    print("*********Caixa eletrônico************")
    print("*************************************")


def get_conta_autenticada():
    conta_digitada = input('Digite sua conta : ')
    senha_digitada = getpass.getpass('Digite sua senha : ')

    if conta_digitada in contas_lista and senha_digitada == contas_lista[conta_digitada]['senha']:
        return conta_digitada
    else:
        return False


def get_opcao_digitada(conta_autenticada):
    print('1 - Saldo')
    print('2 - Saque')
    if contas_lista[conta_autenticada]['admin']:
        print('10 - Incluir cédulas')
    return input('Selecione uma opção: ')


def operacoes_disponiveis(opcao_digitada, conta_autenticada):
    if opcao_digitada == 1:
        saldo(conta_autenticada)
    elif opcao_digitada == 2:
        saque()
    elif opcao_digitada == 10:
        abastecimento_caixa()


def saldo(conta_autenticada):
    print('Seu saldo é %s ' % contas_lista[conta_autenticada]['valor'])


def saque():
    valor_do_saque = input('Qual o valor do saque: ')
    valor_do_saque_int = int(valor_do_saque)

    cedulas_para_usuario = {}

    if valor_do_saque_int // 100 > 0 and valor_do_saque_int // 100 <= cedulas['100']:
        cedulas_para_usuario['100'] = valor_do_saque_int // 100
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 100 * 100

    if valor_do_saque_int // 50 > 0 and valor_do_saque_int // 50 <= cedulas['50']:
        cedulas_para_usuario['50'] = valor_do_saque_int // 50
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 50 * 50

    if valor_do_saque_int // 20 > 0 and valor_do_saque_int // 20 <= cedulas['20']:
        cedulas_para_usuario['20'] = valor_do_saque_int // 20
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 20 * 20

    if valor_do_saque_int != 0:
        print('Não à notas disponiveis para saque ')
    else:
        for retirada in cedulas_para_usuario:
            cedulas[retirada] -= cedulas_para_usuario[retirada]
        print('Pegue as notas! ')
        print(cedulas_para_usuario)


def abastecimento_caixa():
    qtdo_cedulas = input('Digite a quantidade de cédulas: ')
    vlr_cedulas = input('Digite qual cédulas vai inserir: ')
    cedulas[vlr_cedulas] += int(qtdo_cedulas)
    print(cedulas)


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    main()
    input('Pressione <ENTER> para continuar...')
    limpar()
