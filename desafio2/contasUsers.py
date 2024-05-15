from databases import contas

def buscar_contas(*, cpf_, bd_contas_):
    contas_user = []
    for conta in bd_contas_:
        if conta["usuario"] == int(cpf_):
            contas_user.append(conta)

    if len(contas_user)>0: 
        return contas_user
    
    else:
        return 404
    

buscar_contas(cpf_=123, bd_contas_=contas)


