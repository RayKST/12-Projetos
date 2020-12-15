def validaçãoResposta (rspt):
    if len(palavras) == 3:
        if rspt == 2:
            print("Resposta Correta!")
            palavra = palavras.pop(rspt - 1)
            frase[1] = palavra
    elif len(palavras) == 2:
        if rspt == 2:
            print("Resposta Correta!")
            palavra = palavras.pop(rspt - 1)
            frase[3] = palavra
    elif len(palavras) == 1:
        if rspt == 1:
            print("Resposta Correta!")
            palavra = palavras.pop(rspt - 1)
            frase[5] = palavra


frase = [["O Rato "], ["--- "], ["a "], ["--- "], ["do "], ["--- "], ["de Roma!"]]
palavras = ["rei ", "roeu ", "roupa "]

print("Bem vindo ao medlibs, insira a palavra correta a frase...")
print("A frase que você terá que completar é :")

while len(palavras) != 0:
    for x in frase :
        for y in x:
            print(y, end="")
    print("")

    print("Qual palavra dessa lista se encaixa no espaço? ")
    for i, x in enumerate(palavras) :
        print(i+1, "-", x)
    resposta = int(input("... "))

    if resposta > len(palavras) or resposta < 1:
        print("Resposta Inválida")
    else:
        validaçãoResposta(resposta)

for x in frase :
    for y in x:
        print(y, end="")
print("")

print("Você ganhou o jogo")