import random
def jogar():

    print("🎮-------------------------------------🎮")
    print(" ❓ Bem vindo ao jogo de Adivinhação! ❓")
    print("🎮-------------------------------------🎮")

    numero_secreto = random.randrange(1,101)
    tentativa = 0
    rodada = 1
    pontos = 1000

    print("Escolha o nivel de dificuldade :")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input(""))

    if (nivel == 1):
        tentativa = 20

    elif (nivel == 2):
        tentativa = 10

    else:
        tentativa = 5

    # td for precisa do in range(numero_inicial, numero_final +1, quanto_em_quanto)
    # qd numero incial ser = a numero final, ele para por isso usar o +1
    # for rodada in range (1,tentativa + 1):

    # O format.(var1,var2) serve para inserir valores em colchetes ("{}") dentro do print https://pyformat.info/
    # print("Tentativa {} de {}".format(rodada,tentativa))

    # break(for/while) -  parar a repeticao
    # continue (for/while) - ir para a proxima interação

    for rodada in range (1,tentativa + 1):
        print("Tentativa {} de {}".format(rodada,tentativa))
        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)
        print("--------------------")
        print("Você digitou: ", chute)
        print("--------------------")
        if (chute <1) or (chute>100):
            print("❌❌❌---------------------------------❌❌❌")
            print(" Voce deve digitar um número entre 1 e 100 !!!")
            print("❌❌❌---------------------------------❌❌❌")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        # menor   = try_num < secret_num

        if (acertou):
            print("🎉*****************************🎉")
            print("          Você acertou !!!")
            print("🎉*****************************🎉")
            break
        else:
            if(maior):
                print("⬆️⬆️⬆️**********************************************⬆️⬆️⬆️")
                print(" Você errou, O seu chute foi maior que o número secreto.")
                print("⬆️⬆️⬆️**********************************************⬆️⬆️⬆️")
            else:
                print("⬇️⬇️⬇️**********************************************⬇️⬇️⬇️")
                print("   Você errou, O seu chute foi menor que o número secreto.")
                print("⬇️⬇️⬇️**********************************************⬇️⬇️⬇️")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    if (acertou == True):
        print("*******************************")
        print("  Parabens, você venceu 🤩     ")
        print("          Pontuação: {}       ".format(pontos))
        print("* 🎮       Game-Over       🎮 *")
        print("*******************************")
    else:
        print("*******************************")
        print("   Que pena, você perdeu 😞    ")
        print("   O número secreto era {}.     ".format(numero_secreto))
        print("          Pontuação: {}       ".format(pontos))
        print("* 🎮       Game-Over       🎮 *")
        print("*******************************")
if (__name__ == "__main__"):
    jogar()