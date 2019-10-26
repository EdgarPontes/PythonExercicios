import utilidades
import operacoes

def main():
    utilidades.cabecalho()
    conta_autenticada = operacoes.get_conta_autenticada()

    if conta_autenticada:
        utilidades.limpar()

        utilidades.cabecalho()
        opcao_digitada = operacoes.get_opcao_digitada(conta_autenticada)
        operacoes.operacoes_disponiveis(opcao_digitada, conta_autenticada)
    else:
        print('Conta inválida')

while True:
    main()
    input('Pressione <ENTER> para continuar...')
    utilidades.limpar()
