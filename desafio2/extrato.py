from databases import saldo

def mostrarExtrato(*,saldo_, extrato_):
    print(f"O seu saldo atual é: R$ {saldo_:.2f}\n")
    modeExtrato = extrato_
    modeExtrato.reverse()
    for item in modeExtrato:
        print(item)