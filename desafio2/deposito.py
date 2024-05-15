from databases import *

def deposito(saldo_, depo_valor, extrato_=[]):
        if depo_valor > 0:
            novo_valor = saldo_ + depo_valor
            extrato_.append(f"Nº {len(extrato_)+1} - depósito - R$ {float(depo_valor):.2f}")
            return {"saldo" : novo_valor, "extrato": extrato_}
        else:
             return 404


