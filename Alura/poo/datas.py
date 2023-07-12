class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")



# Teste classe

data = Data(11,7,2023)
data.formatada()
