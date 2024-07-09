menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        valor = float(input("Digite o valor para depósito: "))
        saldo += valor
        extrato += f"Depósito: R${valor:.2f} realizado.\n"
        print(f"Depósito no valor de R${valor:.2f} realizado.")
    elif opcao == 's':
        if numero_saques < limite_saques:
            valor = float(input("Digite o valor para saque: "))
            if valor <= saldo:
                if valor <= limite:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R${valor:.2f}\n"
                    print(f"Saque de R${valor:.2f} realizado.")
                else:
                    print(f"Valor do saque excede o limite de R${limite:.2f}.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários atingido.")
    elif opcao == 'e':
        print("\nExtrato:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}\n")
        print(f"Saques realizados: {numero_saques}/{limite_saques}\n")
    elif opcao == 'q':
        print("Saindo... \n Obrigado(a) por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida. Tente novamente.")