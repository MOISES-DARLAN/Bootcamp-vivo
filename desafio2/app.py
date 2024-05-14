from saque import saque, endereço
from createUsers import *
from deposito import deposito
from databases import *
from menus import *

while True:
    opcao_login = input(menu_login)

    if opcao_login == '1':
        cpf_verificar = int(input("digite seu cpf: "))
        usuario = verifyUsers(cpf_user=cpf_verificar)
        
        if usuario != 404:
            print(f"Bem vindo de volta {usuario["name"]}")
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
                    print("Você saiu do app.")
                    break

                else:
                    print('Opção inválida')
        
        else:
            print("Esse usuário não existe")
