import random

print("**************")
print("Bem vindo ao jogo")
print("**************")


numero_secreto = random.randrange(1,101)
total_tentativas = 3

print(numero_secreto)

for rodada in range(1,total_tentativas +1):
    print("Tentativa {} de {}".format (rodada, total_tentativas))
    chute_str = input( "Digite um numero entre 1 e 100 : ")
    print("Você digitou " , chute_str )
    chute =int(chute_str)

    if (chute<1 or chute > 100):
        print("Você deve digitar um numero de 1 a 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou")
        break

    if(maior):
        print("Você errou ! O seu chute foi maior que o número secreto")

    if(menor):
        print("Você errou! O seu chute foi menor do que o número secreto")

    rodada = rodada + 1

print ("Fim de jogo")