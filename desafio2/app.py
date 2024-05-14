from saque import saque
from databases import *
from menus import *

saldo = 0
LIM_SAQUE = 3
vezes_sacadas = 0




def deposito():
    global saldo, extrato
    valor = input("Digite o valor que deseja depositar: ")
    if valor.isnumeric():
        saldo += float(valor)
        extrato.append(f"Nº {len(extrato)+1} - depósito - R$ {saldo:.2f}")
        print(f"Depositado R$ {valor}")
    else:
        print('Digite um valor válido')
    
# def saque():
#     global vezes_sacadas, saldo
#     if vezes_sacadas < LIM_SAQUE:
#         sacar_valor = input("Qual o valor que você quer sacar?")
#         if sacar_valor.isnumeric() and float(sacar_valor) <= saldo:
#             saldo -= float(sacar_valor)
#             sacado = float(sacar_valor)
#             extrato.append(f"Nº {len(extrato)+1} - SAQUE - R$ {sacado:.2f}")
#             vezes_sacadas += 1
#             print(f'\n Você sacou R$ {sacar_valor}')
#         else:
#             print('Valor inválido ou saldo insuficiente')
#     else:
#         print('Limite de saques diário atingido.'

def saque(*, saldo, val_saque, ext, lim, num_saque, lim_saque ):
    global vezes_sacadas
    if vezes_sacadas < lim_saque:
        sacar_valor = val_saque
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



while True:
    opcao_login = input(menu_login)

    if opcao_login == '1':
        while True:
            opcao = input(menu_principal)
            if opcao == '1':
                deposito()
            elif opcao == '2':
                valor_saque = input("QUAL VALOR VOCÊ QUER SACAR?")
                cont_saque = 0
                saque(saldo=saldo,lim_saque=LIM_SAQUE, val_saque=valor_saque)
            elif opcao == '3':
                print(f"\nseu saldo é de R$ {saldo:.2f} \n")
                print('\n'.join(extrato))
            elif opcao == '4':
                break
            else:
                print('Opção inválida')
