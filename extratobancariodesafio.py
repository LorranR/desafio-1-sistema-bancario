menu = """
        Banco TRADER

Serviço ou operação desejada:

[d] Depositar
[s] Sacar
[P] Pagamento de Boleto
[c] Cheque Especial
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#implementação cheque especial
limite_cheque_especial = 1000
limite_saque_cheque_especial = 1
numero_saques_cheque_especial = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito realizado: R${valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor > saldo
        limitador_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor > limite

        if saldo_insuficiente:
            print("\nFalha na operação!\nSaldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação!\nO valor do saque excede o limite.")

        elif limitador_saques:
            print("Falha na operação!\nNúmero máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            numero_saques+=1
            extrato += f"Saque realizado: R${valor:.2f}\n"
        else:
            print("\nFalha na operação!\nO valor informado é inválido.")

    elif opcao == "p":
    
        codigo_barras = float(input("Informe o código de barras "))
        valor = float(input("Informe o valor do boleto: ")) 

        saldo_insuficiente = valor > saldo

        if  saldo_insuficiente:
            print("\nFalha na operação!\nSaldo insuficiente.")
        elif saldo> 0:
            saldo -= valor
            extrato += f"Pagamento realizado: R$ {valor:.2f}\n"
        else:
            print("\nFalha na operação!\nO valor informado é inválido.")

    elif opcao == "c":
        valor = float(input("Informe o valor para saque no Cheque Especial: "))
        
        limitador_saques = numero_saques_cheque_especial >= limite_saque_cheque_especial
        excedeu_limite = valor > limite_cheque_especial

        if excedeu_limite:
            print("Falha na operação!\nO valor do saque do Cheque Especial excede o limite.")

        elif limitador_saques:
            print("Falha na operação!\nNúmero máximo de saques excedido.")

        elif valor > 0: 
            
            numero_saques_cheque_especial+=1
            extrato += f"Saque Cheque Especial realizado: R$ {valor:.2f}\n"
        else:
            print("\nFalha na operação!\nO valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nenhum registro de movimentação encontrado." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print()
        print("Inforções, reclamações, sugestões  e elogios ")
        print("SAC 0800-555 0000")
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")