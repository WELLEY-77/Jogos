def jogar_forca():
    print('*'*26)
    print('BEM VINDO AO JOGO DA FORCA')
    print('*'*26)
    
    palavra_secreta = 'banana'

    acertou = False
    enforcou = False

    while(not enforcou and not acertou):

        chute = input('Digite uma letra: ')

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print('Encontrei a letra {} na posição {} '.format(chute,index))
            index = index + 1
        print('Jogando...')
    
    print('FIM DE JOGO')

if (__name__ == '__main__'):
    jogar_forca()