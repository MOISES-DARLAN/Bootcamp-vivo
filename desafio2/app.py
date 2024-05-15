from saque import saque, endereço
from createUsers import *
from deposito import *
from databases import *
from menus import *
from extrato import *
from contasUsers import *

while True:
    opcao_login = input(menu_login)

    if opcao_login == '1': #fazer login
        usuario = verifyUsers(cpf_user=int(input("Digite o seu cpf: ")))
        
        if usuario != 404:
            print(f"Bem vindo de volta {usuario["name"]}")
            while True:
                opcao = input(menu_principal)
                if opcao == '0':
                    contas_usuario = buscar_contas(cpf_=usuario["cpf"], bd_contas_=contas)

                    if contas_usuario != 404:
                        id_conta = 0
                        for contaUser in contas_usuario:
                            print(f"[{id_conta}] {contaUser['username']}")
                            id_conta += 1
                        
                        trocar_para_conta = input("\nQual a conta que você quer acessar?")
                    else:
                        print("Você não possui mais contas.")

                if opcao == '1':
                    depo_novo_valor = float(input("Qual a quantia que você quer depositar: "))
                    objetoDeposito = deposito(saldo, depo_novo_valor, extrato)
                    if objetoDeposito != 404:     
                        saldo = objetoDeposito["saldo"]
                        extrato = objetoDeposito["extrato"]
                        print(f"Você depositou R$ {depo_novo_valor:.2f}")
                    
                    else: 
                        print("Houve um problema ao realizar o deposito")

                elif opcao == '2':
                    valor_saque = int(input("QUAL VALOR VOCÊ QUER SACAR?"))
                    cont_saque = 0
                    novoSaque = saque(saldo_=saldo, val_saque_=valor_saque, ext=extrato, lim_saque=LIM_SAQUE, vezes_sacadas_=vezes_sacadas)
                    if novoSaque["code"] != 404:
                        saldo = novoSaque["saldo"]
                        extrato = novoSaque["extrato"]
                        print(f"Você sacou R$ {valor_saque:.2f}")
                    else: 
                        print("não foi possivel fazer o saque.")

                elif opcao == '3':
                    mostrarExtrato(saldo_=saldo, extrato_=extrato)

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
        
        elif newUser == 404:
            print("já existe um usuário cadastrado com essa conta!")

        else: 
            print("Houve algum problema, por favor tente de novo mais tarde!")

    
    else:
        print("opção invalida")
    
