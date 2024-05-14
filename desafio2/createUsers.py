from databases import *

def criate_users(nome="users", data_nasc="none", cpf="none", endereço=[]):
    global users
    if users.count(cpf)> 0:
        print("ERRO! JÁ EXISTE UM USUÁRIO CADASTRADO COM ESSE CPF.")

    else:
        new_user = {"name": nome, "data_nasc" : data_nasc, "cpf": cpf, "endereço": endereço}
        users.append(new_user)
        print(users)
        print('\n usuário criado com sucesso.')

def verifyUsers(cpf_user):
    for user in users:
        if cpf_user == user["cpf"]:
            return user
            
    else:
        return 404

verifyUsers(cpf_user=123)