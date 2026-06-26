#Bibiliotecas
from datetime import datetime as dt

menu = """

Sistema Bancário - Banco do Brasil
Escolha sua opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
numero_transacoes = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito: \n")
        if numero_transacoes >= LIMITE_TRANSACOES:
            print("❌ Você excedeu o número de transações diárias (10 por dia)!")
            continue

        valor = float(input("Quanto você deseja depositar? \n=> "))

        if valor > 0:
            saldo += valor
            data_hora = dt.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
            numero_transacoes += 1
        else:
            print("Operação falhou, o valor informado é inválido.")
            
      
    elif opcao == "s":
        print("\nSaque: \n")
        if numero_transacoes >= LIMITE_TRANSACOES:
            print("❌ Você excedeu o número de transações diárias (10 por dia)!")
            continue
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        
        elif valor > 0:
            saldo -= valor
            data_hora = dt.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            numero_transacoes += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

      
    elif opcao == "e":
        print("\n==============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")