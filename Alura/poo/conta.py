def criar_conta(numero,titular,saldo,limite):
    conta = {"numero":numero,"titular":titular,"saldo":saldo,"limite":limite}
    return conta


conta = criar_conta(123,"Matheus",55,1000)

print(conta["titular"])