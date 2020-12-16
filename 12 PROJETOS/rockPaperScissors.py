from random import randint

def win (p, t):
    if p == t:
        print("Empate")
    elif p+t == 3:
        print("Papel ganhou!")
    elif p+t == 4:
        print("Pedra ganhou!")
    elif p+t == 5:
        print("Tesoura ganhou")


def UserXUser ():
    escolha = int(input('''
        Qual sua Escolha?
        1 - Pedra
        2 - Papel
        3 - Tesoura
    '''))

    escolha2 = int(input('''
        Qual a Escolha do seu oponente?
        1 - Pedra
        2 - Papel
        3 - Tesoura
    '''))

    win(escolha, escolha2)


def UserxIA () :
    escolha = int(input('''
        Qual sua Escolha?
        1 - Pedra
        2 - Papel
        3 - Tesoura
    '''))

    escolha2 = randint(1, 3)
    win(escolha, escolha2)

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