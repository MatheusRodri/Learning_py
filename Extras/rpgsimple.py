'''
Crie um programa simples que simule um mini rpg, na qual terá o um heroi e um inimigo,
ambos vão começar com 100 de vidas,e cada erro do usuario vai resulta na perca
de 20 pontos na vida do usuario e no caso de acerto -15 pontos na vida do inimigo.
O jogo consiste em advinhação de numero, na qual o usuario pode tentar algumas vezes(Pode
variar de acordo com o nivel) antes de perder o pontos.
'''

import random

vida_heroi = 100
vida_inimigo = 100
rodada = 1
limite_rodada = 10

print("=====================")
print("Bem-vindo ao mini rpg")
print("=====================")

def rpg(limite):

    if(vida_inimigo > 0):
        valor_inimigo = random.randrange(1, 11)#Gerando um numero aleatorio para o valor do inimigo
        print(f"valor do inimigo {valor_inimigo}") #Imprimir o numero, para teste

        while (rodada < limite):
            print(f"rodada {rodada} de {limite}")
            valor_escolhido_heroi = int(input("Inimigo: Informe um numero, meu caro: ")) #Valor que o usuario digita

            if(valor_escolhido_heroi == valor_inimigo):
                print("Ainda não acabou")
                valor_inimigo = valor_inimigo - 20
                escolha = int(input("1-Sim\n2-Não"))
                if (escolha == 1):
                    limite = limite - 3
                    rpg(limite)
                else:
                    break
            else:
                print("Você errou")
                vida_heroi = vida_heroi - 20
                rodada = rodada + 1


rpg(limite_rodada)
print("Fim de jogo !")