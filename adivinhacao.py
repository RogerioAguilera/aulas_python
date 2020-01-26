print("**************")
print("Bem vindo ao jogo")
print("**************")


numero_secreto = 42

chute_str = input( "Digite seu numero : ")
print("Você digitou " , chute_str )

chute =int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Voce acertou")

if(maior):
    print("Você errou ! O seu chute foi maior que o número secreto")

if (menor):
    print("Você errou! O seu chute foi menor do que o número secreto")


print ("Fim de jogo")