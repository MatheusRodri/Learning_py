class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "033"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    
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
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco(self):
        return self.__codigo_banco
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}

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