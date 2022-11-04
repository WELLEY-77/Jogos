def jogar_forca():
    print('*'*26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('*'*26)
    
    palavra_secreta = 'banana'
    letra_secreta = ['_', '_', '_', '_', '_', '_']

    acertou = False
    enforcou = False

    while(not enforcou and not acertou):

        chute = input('Digite uma letra: ').strip()
        
        #---------Pode fazer dessa outra maneira tambem para tira os espaços
        #chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letra_secreta[index] = letra  
            index = index + 1
            
        print(letra_secreta)
    print('FIM DE JOGO')

if (__name__ == '__main__'):
    jogar_forca()