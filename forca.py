from random import randint

def jogar_forca():
    print('*'*26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('*'*26)
    
    arquivo = open('palavras.txt','r')

    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = randint(0,len(palavra))
    palavra_secreta = palavra[numero].upper()

    #-----List comprehensions
    letra_secreta = ['_' for letra in palavra_secreta]

    #---funciona tambem dessa forma--------

    #for letra in palavra_secreta:
    #    letra_secreta.append('_')

    acertou = False
    enforcou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = input('Digite uma letra: ').strip().upper()
        
        #---------Pode fazer dessa outra maneira tambem para tira os espaços
        #chute = chute.strip()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letra_secreta[index] = letra  
                index = index + 1
        else:
            tentativas += 1
        
        enforcou = tentativas == 6
        acertou = '_' not in letra_secreta

        print(letra_secreta)

    if (acertou):
        print('Você acertou!!')
    else:
        print('Você errou!!')        
    print('FIM DE JOGO')

if (__name__ == '__main__'):
    jogar_forca()