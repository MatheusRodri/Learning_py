class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def saca(self,valor):
        self.__saldo -= valor
    
    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite

    def set_limite(self,limite):
        self.__limite = limite

# Teste da classe

conta = Conta(123,"Matheus",100,1000.0)
conta2 = Conta(321,"Joao",100,1000.0)
print(conta.extrato())
print(conta2.extrato())
# print(conta.deposita(900))
# print(conta.saca(100))
# print(conta.extrato())
conta.transfere(100,conta2)
print(conta.extrato())
print(conta2.extrato())