import os
class Contas:
    def __init__(self):
        self.ano = input("Ano: ")
        self.mes = input("Mês: ")
        self.produto = input("Produto: ")
        self.preco = float(input("Preço: "))

def setConta():
    conta = Contas()
    os.system("clear")
    arquivoPreco = open("preço" + conta.mes + conta.ano + ".txt", "a")
    arquivoProduto = open("produto" + conta.mes + conta.ano + ".txt", "a")

    arquivoPreco.write(str(conta.preco) + '\n')
    arquivoProduto.write(str(conta.produto) + '\n')

    arquivoPreco.close()
    arquivoProduto.close()

def getConta():
    os.system("clear")
    print('-------------Digite o mês e o ano da conta------------')
    ano = input("Ano: ")
    mes = input("Mês: ")
    os.system("clear")

    try:
        arquivoPreco = open("preço" + mes + ano + ".txt", "r")
        arquivoProduto = open("produto" + mes + ano + ".txt", "r")
    except:
        print("O mês de", mes, "não possui contas cadastradas")

    print("---------------------------------------------------")
    print("Mês:", mes)
    print("Ano:", ano)
    print("---------------------------------------------------")
    total = 0
    for lines in arquivoPreco:
        preco = float(lines)
        print(arquivoProduto.readline(), end='')
        print("R$", preco)
        total += preco  
    print("---------------------------------------------------")
    print("Total: R$", total)
    print("---------------------------------------------------")

    arquivoProduto.close()
    arquivoPreco.close()

def menu():
    print('[*] SELECIONE UMA OPÇÃO PARA CONTINUAR')
    print('[1] Cadastrar gasto')
    print('[2] Verificar gasto do mês')
    print('[3] Sair')
    print("---------------------------------------------------")
    menu = input('Seleção: ')
    if(menu == '1'):
        setConta()
    elif(menu == '2'):
        getConta()
    else:
        exit()

if (__name__ == '__main__'):
    print("----------Gerenciador de Contas-----------")
    while True:
        menu()