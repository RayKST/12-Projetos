from random import choice

números = list(range(1, 1000))
teto = 1000
chão = 1
númeroDeChutes = 0
chuteMáquina = True
númeroSorteado = choice(números)

while chuteMáquina != númeroSorteado :
    chuteMáquina = choice(números)

    if chuteMáquina > númeroSorteado :
        teto = chuteMáquina
        números = list(range(chão, teto))
        númeroDeChutes += 1

    elif chuteMáquina < númeroSorteado :
        chão = chuteMáquina
        números = list(range(chão, teto))
        númeroDeChutes += 1

print("A máquina acertou em {} chutes".format(númeroDeChutes))