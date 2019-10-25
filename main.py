import getpass

print("*************************************")
print("*********Caixa eletrônico************")
print("*************************************")

conta_digitada = input('Digite sua conta : ')
senha_digitada = getpass.getpass('Digite sua senha : ')

print(conta_digitada)
print(senha_digitada)

contas_lista = {
    '0001-01': {
        'senha': '123456',
        'nome' : 'Edgar de Pontes',
        'valor': 0
    },
    '0002-01': {
        'senha': '654321',
        'nome' : 'Ana Paula',
        'valor': 0
    }
}

if conta_digitada in contas_lista and senha_digitada == contas_lista[conta_digitada]['senha']:
    print('Conta válida')
else:
    print('Conta inválida')