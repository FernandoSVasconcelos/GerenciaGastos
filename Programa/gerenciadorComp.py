import os
class Contas:
    def __init__(self):
        self.ano = input("Ano: ")
        self.mes = input("Mês: ")
        self.net = float(input("Internet(99.9): "))
        self.condo = float(input("Condomínio(322.6): "))
        self.aluguel = float(input("Aluguel(1120.92): "))
        self.luz = float(input("Luz: "))
        self.extra = float(input("Extra: "))

    def total(self):
        return float(self.net + self.condo + self.aluguel + self.luz + self.extra)

    def suite(self, total):
        return float(total - 70)

    def semSuite(self, suite):
        return float(suite/3)

    def comSuite(self, suite):
        return float((suite/3) + 70)

def menu():
    print('[*] SELECIONE UMA OPÇÃO PARA CONTINUAR')
    print('[1] Setar conta do mês')
    print('[2] Verificar conta do mês')
    print('[3] Sair')
    print('-------------------------------------------------------------------')
    menu = input('Seleção: ')
    if(menu == '1'):
        conta = Contas()
        os.system("clear")
        arquivo = open(conta.mes + conta.ano + ".txt", "a")

        arquivo.write(conta.mes + '\n')
        arquivo.write(conta.ano + '\n')
        arquivo.write(str(conta.net) + '\n')
        arquivo.write(str(conta.condo) + '\n')
        arquivo.write(str(conta.aluguel) + '\n')
        arquivo.write(str(conta.luz) + '\n')
        arquivo.write(str(conta.extra) + '\n')

        total = conta.total()
        arquivo.write(str(total) + '\n')

        totalSuite = conta.suite(total)
        arquivo.write(str(totalSuite) + '\n')

        bigas = conta.semSuite(totalSuite)
        arquivo.write(str(bigas) + '\n')

        fer = conta.comSuite(totalSuite)
        arquivo.write(str(fer) + '\n')

        jhony = conta.semSuite(totalSuite)
        arquivo.write(str(jhony))

        arquivo.close()

    elif(menu == '2'):
        os.system("clear")
        print('-------------Digite o mês e o ano da conta------------')
        ano = input("Ano: ")
        mes = input("Mês: ")
        os.system("clear")

        try:
            arquivo = open(mes + ano + ".txt", "r")
            print("---------------------------------------------------")
            print("Mês:", arquivo.readline(), end='')
            print("Ano:", arquivo.readline(), end='')
            print("---------------------------------------------------")
            print("Internet:", arquivo.readline(), end='')
            print("Condomínio:", arquivo.readline(), end='')
            print("Aluguel:", arquivo.readline(), end='')
            print("Luz:", arquivo.readline(), end='')
            print("Extra:", arquivo.readline(),end='')
            print("---------------------------------------------------")
            print("Total:", arquivo.readline(),end='')
            print("Total com desconto da suíte:", arquivo.readline(), end='')
            print("---------------------------------------------------")
            print("Bigas:", arquivo.readline(), end='')
            print("Fer:", arquivo.readline(), end='')
            print("Jhony:", arquivo.readline())
            print("---------------------------------------------------")
            arquivo.close()
        except:
            print("Conta não cadastrada")
    
    else:
        exit()

if (__name__ == '__main__'):
    print("----------Contas Comp-----------")
    menu()