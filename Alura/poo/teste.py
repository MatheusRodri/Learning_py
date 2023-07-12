def criar_conta(numero,titular,saldo,limite):
    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta

def deposita(conta,valor):
    conta["saldo"] += valor

def saca(conta,valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

conta = criar_conta(123,"Matheus",55,1000)

print("Primeiro",conta)

deposita(conta,500)
print("Segundo",conta)

saca(conta,100)
print("Terceiro",conta)

extrato(conta)