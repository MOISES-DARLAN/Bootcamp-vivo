from databases import *

def criate_users(nome="users", data_nasc="none", cpf="none", endereço=[]):
    global users
    if users.count(int(cpf))> 0:
        error = "ERRO! JÁ EXISTE UM USUÁRIO CADASTRADO COM ESSE CPF."
        return 400

    else:
        new_user = {"name": nome, "data_nasc" : data_nasc, "cpf": int(cpf), "endereço": endereço}
        users.append(new_user)
        return 200

def verifyUsers(cpf_user):
    for user in users:
        if cpf_user == user["cpf"]:
            return user
            
    else:
        return 404

verifyUsers(cpf_user=123)