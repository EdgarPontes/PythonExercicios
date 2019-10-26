import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho():
    print("*************************************")
    print("*********Caixa eletrônico************")
    print("*************************************")
