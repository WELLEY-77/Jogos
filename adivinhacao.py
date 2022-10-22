from random import randint

def jogar_adivinhacao():
        
    print('*'*32)
    print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
    print('*'*32)

    numero_sorteado = randint(1,100)
    tentativas = 0
    pontos = 1000

    #-----------------------PARTE DA ESCOLHA DE NIVEL--------------
    print('''DIGITE PARA ESCOLHER UM NIVEL:
    \033[32m[ 1 ] FÁCIL\033[m
    \033[33m[ 2 ] MÉDIO \033[m
    \033[31m[ 3 ] DIFÍCIO \033[m''')

    while (True):
        nivel = int(input('Qual o nivel escolhido: '))
        #--------------------CADA NIVEL TEM UMA TOTALIDADE DE CHANCES------
        if (nivel == 1):
            tentativas = 20
            break
        elif(nivel == 2):
            tentativas = 10
            break
        elif(nivel == 3):
            tentativas = 5
            break
        else:
            print('Opção incorreta!!')
        

    for sorteio in range(1,tentativas +1):
        print('Digite um número entre 1 e 100')
        print('Essa é sua {1}/{0} chances '.format(tentativas,sorteio))
        #print(numero_sorteado)

        palpite = int(input('Qual o seu palpite: '))
        if (palpite < 1) or (palpite > 100) or (palpite < -1) :
            print('Você deve digitar um número entre 1 e 100')
            print('\033[31m Você perdeu uma chance!!\033[m')
            continue
        
        if (palpite == numero_sorteado):
            print('\033[32m parabéns você acertou!')
            print('E sua pontuaçao foi de {} \033[m '.format(pontos))
            break
        elif (palpite > numero_sorteado):
            print('O número digitado esta um pouco acima do numero sorteado')
            print('\033[32mTENTE NOVAMENTE!!\033[m')
        elif (palpite < numero_sorteado):
            print('O número digitado esta um pouco abaixo do numero sorteado ')
            print('\033[32m TENTE NOVAMENTE!!\033[m')

        pontos_perdidos = abs(palpite - numero_sorteado)
        pontos = pontos - pontos_perdidos
    print('\033[35m FIM DE JOGO \033[35m')

if (__name__ == '__main__'):
    jogar_adivinhacao()