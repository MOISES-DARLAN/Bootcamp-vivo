def deposito():
    global saldo, extrato
    valor = input("Digite o valor que deseja depositar: ")
    if valor.isnumeric():
        saldo += float(valor)
        extrato.append(f"Nº {len(extrato)+1} - depósito - R$ {saldo:.2f}")
        print(f"Depositado R$ {valor}")
    else:
        print('Digite um valor válido')