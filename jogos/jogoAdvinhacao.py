import random

def jogar():

    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')

    print('Qual o nível de dificuldade?')
    nivel = input('(1) Fácil (2) Médio (3) Difícil: ')
    nivel_jogo = int(nivel)

    pontos = 1000

    if (nivel_jogo == 1):
        total_de_tentativas = 20
    elif (nivel_jogo == 2):
        total_de_tentativas = 10
    elif (nivel_jogo == 3):
        total_de_tentativas = 5

    numero_secreto = random.randint(1, 101)

    rodadas = 1
    for rodadas in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodadas, total_de_tentativas))
        chute_str = input('Digite o seu número: ')

        print('Você digitou ', chute_str)

        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        elif(maior):
            print('Você errou! O seu chute foi maior que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        else:
            print('Você errou! O seu chute foi menor que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim do jogo, o número sorteado era: ', numero_secreto)

if(__name__ == '__main__'):
    jogar()