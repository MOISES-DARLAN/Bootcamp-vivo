from saque import saque, endereço
from createUsers import *
from deposito import deposito
from databases import *
from menus import *

while True:
    opcao_login = input(menu_login)

    if opcao_login == '1': #fazer login
        usuario = verifyUsers(cpf_user=int(input("Digite o seu cpf: ")))
        
        if usuario != 404:
            print(f"Bem vindo de volta {usuario["name"]}")
            while True:
                opcao = input(menu_principal)

                if opcao == '1':
                    depo_novo_valor = float(input("Qual a quantia que você quer depositar: "))
                    novoDeposito = deposito(saldo, depo_novo_valor, extrato)
                    saldo = novoDeposito["saldo"]
                    extrato = novoDeposito["extrato"]

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
    
    elif opcao_login == "2": #cadastrar novo user
        print(mensagemCadastro)
        nome_NU = input("Seu nome é: ")
        dataNascimento_NU = input("O ano do seu nascimento é: ")
        cpf_NU = input("Seu cpf é: ")

        print("""\n   Agora vamos cadastrar seu endereço.
Preciso que informe respectivamente: logradouro , bairro , cidade, estado""")
        logradouro_NU = input("Logradouro: ")
        cidade_NU = input("Cidade/sigla: ")
        bairro_NU = input("Bairro: ")
        estado_NU = input("Estado/sigla: ")

        endereco_NU = endereço(logradouro=logradouro_NU, bairro=bairro_NU, cidade=cidade_NU, estado=estado_NU)
        newUser = criate_users(nome=nome_NU, data_nasc=dataNascimento_NU, cpf=cpf_NU, endereço=endereco_NU)

        if newUser == 200:
            print("Usuário criado com sucesso.")
        
        else: 
            print("Houve algum problema, por favor tente de novo mais tarde!")

    
    else:
        print("opção invalida")
    
