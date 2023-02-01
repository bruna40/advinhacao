import random

def jogar():
    print('***************************')
    print('Bem vindo ao jogo da Forca!')
    print('***************************')

    palavras =  ['banana', 'laranja', 'abacaxi', 'melancia', 'morango', 'uva', 'pera', 'manga', 'abacate', 'melao', 'caju', 'acerola', 'amora', 'goiaba', 'limao', 'maracuja', 'pitanga', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego', 'graviola', 'mamao', 'caqui', 'coco', 'pitanga', 'tamarindo', 'tangerina', 'cereja', 'pessego']

    enforcou = False
    acertou = False
    erros = 0

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)

    while(not enforcou and not acertou):
            
            chute = input('Qual letra? ')
            chute = chute.strip().lower()
    
            if(chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if(chute.upper() == letra.upper()):
                        letras_acertadas[index] = letra
                    index += 1
            else:
                erros += 1
    
            enforcou = erros == 6
            acertou = '_' not in letras_acertadas
            print(letras_acertadas)


    
    
    print('Fim do jogo, a palavra era: ', palavra_secreta)

if(__name__ == '__main__'):
    jogar()

