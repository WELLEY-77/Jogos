from adivinhacao import jogar_adivinhacao
from forca import jogar_forca
from jokepo import jogar_jokepor


def escollher_jogo():
    print('*'*26)
    print('ESCOLHA UM JOGO PARA JOGAR')
    print('*'*26)


    while (True):
        print('''QUAL JOGO VOCÊ DESEJA JOGAR? 
        [ 1 ] Adivinhção
        [ 2 ] Forca
        [ 3 ] Jokenpor ''')

        jogo_selecionado = int(input('Qual a sua opção: '))

        if (jogo_selecionado == 1):
            jogar_adivinhacao()
            break
        elif(jogo_selecionado == 2):
            jogar_forca()
            break
        elif (jogo_selecionado == 3):
            jogar_jokepor()
            break
        else:
            print('Digite uma opção correta! ')

if(__name__ == '__main__'):
    escollher_jogo()