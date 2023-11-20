class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return  self._likes

    def dar_like(self):
         self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} : {self._likes} Likes"
class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
       return f"{self._nome} - {self.ano} - {self.duracao} Minutos : {self._likes} Likes"

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
            super().__init__(nome, ano)
            self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} Temporadas : {self._likes} Likes"


# Teste da classe
vingadores = Filme("Vingadores - Guerra infinita",2018,160)
suits = Serie("Suits",2019,10)

vingadores.dar_like()
vingadores.dar_like()


Filmes_e_series = [vingadores,suits]

for programa in Filmes_e_series:
    print(programa)