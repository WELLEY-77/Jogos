def jogar_forca():
    print('*'*26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('*'*26)
    
    palavra_secreta = 'banana'.upper()
    letra_secreta = ['_', '_', '_', '_', '_', '_']

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
            
    print('FIM DE JOGO')

if (__name__ == '__main__'):
    jogar_forca()