saldo = 0
extrato = []
LIM_SAQUE = 3
vezes_sacadas = 0

def deposito():
    global saldo
    valor = input("Digite o valor que deseja depositar: ")
    if valor.isnumeric():
        saldo += float(valor)
        extrato.append(f"Nº {len(extrato)+1} - depósito - R$ {saldo:.2f}")
    else:
        print('Digite um valor válido')

def saque():
    global vezes_sacadas, saldo
    if vezes_sacadas < LIM_SAQUE:
        sacar_valor = input("Qual o valor que você quer sacar?")
        if sacar_valor.isnumeric() and float(sacar_valor) <= saldo:
            saldo -= float(sacar_valor)
            sacado = float(sacar_valor)
            extrato.append(f"Nº {len(extrato)+1} - SAQUE - R$ {sacado:.2f}")
            vezes_sacadas += 1
            print(f'\n Você sacou R$ {sacar_valor}')
        else:
            print('Valor inválido ou saldo insuficiente')
    else:
        print('Limite de saques diário atingido.')

menu = """
Escolha o que você quer fazer:
[1] Depositar
[2] Sacar
[3] Consultar extrato
[4] Sair
Eu escolho: """

while True:
    opcao = input(menu)
    if opcao == '1':
        deposito()
    elif opcao == '2':
        saque()
    elif opcao == '3':
        print(f"\nseu saldo é de R$ {saldo:.2f} \n")
        print('\n'.join(extrato))
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
