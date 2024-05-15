from databases import *

def podeSaque(*, lim_saque_, vezes_sacadas_):
    if vezes_sacadas_ <lim_saque_:
        return True 
    else:
        return False
def saque(*, saldo_, val_saque_=0, ext,lim_saque, vezes_sacadas_=0):
    crontrole = podeSaque(lim_saque_=lim_saque, vezes_sacadas_=vezes_sacadas_)# add num_saque
    if crontrole:
        sacar_valor = float(val_saque_)
        if saldo_>= sacar_valor:
            novo_saldo = saldo_ - sacar_valor
            ext.append(f"Nº {len(extrato)+1} - SAQUE - R$ {sacar_valor:.2f}")
            vezes_sacadas_ += 1
            return {'code': 200, 'mensage': 'Saldo atualizado', "extrato": ext, 'saldo': novo_saldo}
        else:
            return {'code': 402}
    else:
        return {'code': 404}


def endereço(*, logradouro , bairro , cidade, estado):
    if logradouro and bairro and cidade and estado:
        endereço = [f"{logradouro or None} - {bairro or None} - {cidade or None} - {estado or None}"]
        return endereço
