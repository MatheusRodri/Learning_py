import advinhacao
import forca


print("*********************************")
print("Bem vindo, escolha um jogo")
print("*********************************")
print("1 - Adivinhação\n2 - Forca")

escolha = int(input("Qual jogo? "))

if(escolha == 1):
    print("Jogando o jogo Adivinhação")
    advinhacao.jogar()
elif(escolha == 2):
    print("Jogando o jogo Forca")
    forca.jogar()
