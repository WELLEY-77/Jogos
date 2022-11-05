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
        
        enforcou = tentativas == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_menssagem_vencedor()
    else:
        imprime_menssagem_perdedor()        
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
    print('Você acertou!!')

def imprime_menssagem_perdedor():
    print('Você perdeu!!')



if (__name__ == '__main__'):
    jogar_forca()