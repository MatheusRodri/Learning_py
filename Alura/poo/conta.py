class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo,self.titular))

    def deposita(self,valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor




# Teste da classe

conta = Conta(123,"Matheus",100,1000.0)
print(conta.extrato())
print(conta.deposita(900))
print(conta.saca(100))
print(conta.extrato())