from random import randint

def jogar_forca():

    imprime_menssagen_abertura()

    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = pede_o_chute()
        
        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)
        
        enforcou = tentativas == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_menssagem_vencedor()
    else:
        imprime_menssagem_perdedor(palavra_secreta)        
    print('FIM DE JOGO')


def imprime_menssagen_abertura():
    print('*'*26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('*'*26)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt','r')

    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = randint(0,len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    #---funciona tambem dessa forma--------

    #for letra in palavra_secreta:
    #    letras_acertadas.append('_')

    #-----List comprehensions
    return ['_' for letra in palavra]

def pede_o_chute():
    chute = input('Digite uma letra: ').strip().upper()[0] 
        #---------Pode fazer dessa outra maneira tambem para tira os espaços
        #chute = chute.strip()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra  
        index = index + 1

def imprime_menssagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_menssagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    jogar_forca()