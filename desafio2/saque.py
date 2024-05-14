from databases import *



def saque(*, saldo, val_saque, ext, lim, num_saque, lim_saque ):
    vezes_sacadas += 1
    if vezes_sacadas < lim_saque:
        sacar_valor = val
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

    print(ext)


def endereço(*, logradouro , bairro , cidade, estado):
    if logradouro and bairro and cidade and estado:
        endereço = [f"{logradouro or None} - {bairro or None} - {cidade or None} - {estado or None}"]
        return endereço

def criate_users(nome="users", data_nasc="none", cpf="none", endereço=[]):
    global users
    if users.count(cpf)> 0:
        print("ERRO! JÁ EXISTE UM USUÁRIO CADASTRADO COM ESSE CPF.")

    else:
        new_user = {"name": nome, "data_nasc" : data_nasc, "cpf": cpf, "endereço": endereço}
        users.append(new_user)
        print(users)

criate_users(cpf=1, nome="moises", data_nasc=2006, endereço=endereço(logradouro="zona rural", bairro="av. aluizio", cidade="gm", estado='ro'))