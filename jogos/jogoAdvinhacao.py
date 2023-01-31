print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 42

tentativas = input('Digite o número de tentativas: ')
tentativas = int(tentativas)
rodadas = 1
for rodadas in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodadas, tentativas))
    chute_str = input('Digite o seu número: ')

    print('Você digitou ', chute_str)

    chute = int(chute_str)
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    if(acertou):
        print('Você acertou!')
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto.')
    else:
        print('Você errou! O seu chute foi menor que o número secreto.')

print('Fim do jogo')