from random import choice

def game ():
    while [] in palavra:
        chute = input("Chute uma letra...")
        chuteNaPalavra(chute)
        print(palavra)
        

def chuteNaPalavra (c):
    for i, l in enumerate(palavraEscolhida):
        if not(c in palavraEscolhida):
            print("Chute Errado, Tente Novamente...")
            break
        elif c == l:
            palavra.pop(i)
            palavra.insert(i, c)
        else:
            pass

palavras = ["cachorro", "gato", "vaca",
"carro", "moto", "aviao"
]
palavraEscolhida = choice(palavras)
palavra = []
for x in palavraEscolhida:
    palavra.append([])

print(palavra)
game()
print("Obrigado por Jogar!")