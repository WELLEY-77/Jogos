from random import randint
from time import sleep


def jogar_jokepor():

    print('\033[32m-='*25)
    print('Bem vindo ao jogo PEDRA,PAPEL,TESOURA')
    print('-='*25)

    print('''\033[m
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA
    ''')

    itens = ('PEDRA','PAPEL','TESOURA')
    computador = randint(1,3)

    while True:
        jogador = abs(int(input('Qual a sua jogada: ').strip()))

        if jogador == 1:
            break
        elif jogador == 2:
            break
        elif jogador == 3:
            break
        else:
            print('Digite uma opção correta!!')
            continue

    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA')
    sleep(1)

    if jogador == 1: #---------------PEDRA
        print('O Jogador jogou {}'.format(itens[0]))
        if computador == 1:         
            print('O Computador tambem jogou {}'.format(itens[0])) 
            print('Empate')
        elif computador == 2:
            print('O Computador jogou {}'.format(itens[1]))
            print('O Computador venceu')
        elif computador == 3: 
            print('O Computador jogou {}'.format(itens[2]))
            print('O Jogador venceu')
    if jogador ==2:#-----------------PAPEL
        print('O Jogador jogou {}'.format(itens[1]))
        if computador == 1:    
            print('O Computador jogou {}'.format(itens[0]))
            print('O Jogador venceu')
        elif computador == 2:       
            print('O Computador tambem jogou {}'.format(itens[1]))
            print('Empate')
        elif computador == 3:      
            print('O Computador jogou {}'.format(itens[2]))
            print('O Computador venceu')
    if jogador == 3:#---------------TESOURA
        print('O Jogador jogou {}'.format(itens[2]))
        if computador == 1:
            print('O Computador jogou {}'.format(itens[0]))
            print('O Computador venceu')
        elif computador == 2:
            print('O Computador jogou {}'.format(itens[1]))
            print('O Jogador venceu')
        elif computador == 3:     
            print('O Computador tambem jogou {}'.format(itens[2]))
            print('Empate')

if (__name__ == '__main__'):
    jogar_jokepor()