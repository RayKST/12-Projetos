from random import randint

def winTieOrLose (e1, e2):
    if e1 == e2:
        print("Empate")

    elif e1 + e2 == 3:
        print("Papel ganhou!")

    elif e1 +e2 == 4:
        print("Pedra ganhou!")

    elif e1 + e2 == 5:
        print("Tesoura ganhou")


def UserXUser ():
    escolha = 5
    escolha2 = 5

    while not(escolha in [1,2,3]):
        escolha = int(input('''
            Qual sua Escolha?
            1 - Pedra
            2 - Papel
            3 - Tesoura
        '''))

    while not(escolha2 in [1,2,3]):
        escolha2 = int(input('''
            Qual a Escolha do seu oponente?
            1 - Pedra
            2 - Papel
            3 - Tesoura
        '''))

    winTieOrLose(escolha, escolha2)


def UserxIA () :
    escolha = 5

    while not(escolha in [1,2,3]):
        escolha = int(input('''
            Qual sua Escolha?
            1 - Pedra
            2 - Papel
            3 - Tesoura
        '''))

    winTieOrLose(escolha, randint(1, 3))


print("Bem vindo ao Pedra, Papel, Tesoura...")
while True :
    caminho = int(input('''
        Qual modo de jogo você deseja?
        1 - User VS User
        2 - User VS IA
        3 - Sair
    '''))

    if caminho == 1:
        UserXUser()
    elif caminho == 2:
        UserxIA()
    elif caminho == 3:
        break
    else :
        print("Tente Novamente")