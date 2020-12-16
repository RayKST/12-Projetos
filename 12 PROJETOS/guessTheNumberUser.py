from random import choice

números = list(range(1, 100))
teto = 100
chão = 1
chute = 0
númeroDeChutes = 0
númeroSorteado = choice(números)

while chute != númeroSorteado :
    chute = int(input("Qual número chutar? "))

    if chute > númeroSorteado :
        print("Seu Chute foi alto, chute um número menor...")
        teto = chute
        números = list(range(chão, teto))
        númeroDeChutes += 1
        print("O número sorteado está entre {} e {}".format(chão, teto))
        print("")

    elif chute < númeroSorteado :
        print("Seu chute foi baixo, chute um número maior")
        chão = chute
        números = list(range(chão, teto))
        númeroDeChutes += 1
        print("O número sorteado está entre {} e {}".format(chão, teto))
        print("")

print("Você acertou em {} chutes".format(númeroDeChutes))