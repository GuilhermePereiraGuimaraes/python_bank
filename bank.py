from time import sleep

def Depositar(saldo, valor, extrato):
    saldo_anterior = saldo
    saldo += valor
    print(f"Deposito realizado com sucesso! Seu novo saldo R${saldo:.2f}")
    extrato = f"""{" "*6}SALDO ANTERIOR R${saldo_anterior:.2f} | DEPOSITO DE R${valor:.2f} | NOVO SALDO R${saldo:.2f}\n"""

    return (saldo,extrato)


def Saque(saldo, valor, extrato):
    if valor > saldo or valor > 500:
        print(f"Saque indisponivel. Seu saldo é de R${saldo:.2f}")
    else:
        saldo_anterior = saldo
        saldo -= valor
        print(f"Saque realizado com sucesso! Seu novo saldo R${saldo:.2f}")
        
        extrato = f"""{" "*6}SALDO ANTERIOR R${saldo_anterior:.2f} | SAQUE DE R${valor:.2f} | NOVO SALDO R${saldo:.2f}\n"""

        return (saldo,extrato)


def Exibir_extrato(extrato):
    print(extrato)

seu_saldo = float(input("Digite seu saldo: R$"))
seu_extrato = "======EXTRATO====== \n"
options = 1
saque_max = 3

while options != 0:
    if saque_max > 0:
        options = int(input("""
        ======BANCO PYTHON======
            LISTA DE OPÇÕES

            0 - SAIR    
            1 - DEPOSITAR
            2 - CONSULTAR EXTRATO
            3 - SACAR
        ========================

        """))
    else:
        options = int(input("""
        ======BANCO PYTHON======
            LISTA DE OPÇÕES

            0 - SAIR    
            1 - DEPOSITAR
            2 - CONSULTAR EXTRATO
        ========================

        """))
    print()
    if options == 0:
        print("Saindo...")
    elif options == 1:
        valor_deposito = float(input("Digite quanto quer depositar: R$"))
        depositado = Depositar(seu_saldo, valor_deposito, seu_extrato)
        seu_saldo = depositado[0]
        seu_extrato += depositado[1]
    elif options == 2:
        valor_final = f"SALDO ATUAL: R${seu_saldo:.2f}"
        print(f"{" "*6}{seu_extrato}{" "*6}{valor_final}")
    elif options == 3 and saque_max > 0:
        valor_saque = float(input("Digite quanto quer sacar: R$"))
        if valor_saque <= 500 and valor_saque > 0:
            sacado = Saque(seu_saldo, valor_saque, seu_extrato)
            seu_saldo = sacado[0]
            seu_extrato += sacado[1]
            saque_max -=1
        else:
            print("Valor do saque inválido. Saque máximo de R$500.00 e mínimo de R$1.00")
    else:
        print("Opção inválida tente novamente.")
    
    sleep(3)
    print()
    
