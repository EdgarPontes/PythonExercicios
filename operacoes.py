import getpass
import contas_variaveis


def get_conta_autenticada():
    conta_digitada = input('Digite sua conta : ')
    senha_digitada = getpass.getpass('Digite sua senha : ')

    if conta_digitada in contas_variaveis.contas_lista and senha_digitada == contas_variaveis.contas_lista[conta_digitada]['senha']:
        return conta_digitada
    else:
        return False


def get_opcao_digitada(conta_autenticada):
    print('1  - Saldo')
    print('2  - Saque')
    if contas_variaveis.contas_lista[conta_autenticada]['admin']:
        print('10 - Incluir cédulas')
    return int(input('Selecione uma opção: '))


def operacoes_disponiveis(opcao_digitada, conta_autenticada):
    if opcao_digitada == 1:
        saldo(conta_autenticada)
    elif opcao_digitada == 2:
        saque()
    elif opcao_digitada == 10:
        abastecimento_caixa()


def saldo(conta_autenticada):
    print('Seu saldo é %s ' % contas_variaveis.contas_lista[conta_autenticada]['valor'])


def saque():
    valor_do_saque = int(input('Qual o valor do saque: '))
    valor_do_saque_int = valor_do_saque

    cedulas_para_usuario = {}

    if valor_do_saque_int // 100 > 0 and valor_do_saque_int // 100 <= contas_variaveis.cedulas['100']:
        cedulas_para_usuario['100'] = valor_do_saque_int // 100
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 100 * 100

    if valor_do_saque_int // 50 > 0 and valor_do_saque_int // 50 <= contas_variaveis.cedulas['50']:
        cedulas_para_usuario['50'] = valor_do_saque_int // 50
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 50 * 50

    if valor_do_saque_int // 20 > 0 and valor_do_saque_int // 20 <= contas_variaveis.cedulas['20']:
        cedulas_para_usuario['20'] = valor_do_saque_int // 20
        valor_do_saque_int = valor_do_saque_int - valor_do_saque_int // 20 * 20

    if valor_do_saque_int != 0:
        print('Não à notas disponiveis para saque ')
    else:
        for retirada in cedulas_para_usuario:
            contas_variaveis.cedulas[retirada] -= cedulas_para_usuario[retirada]
        print('Pegue as notas! ')
        print(cedulas_para_usuario)


def abastecimento_caixa():
    qtdo_cedulas = input('Digite a quantidade de cédulas: ')
    vlr_cedulas = input('Digite qual cédulas vai inserir: ')
    contas_variaveis.cedulas[vlr_cedulas] += int(qtdo_cedulas)
    print(contas_variaveis.cedulas)
