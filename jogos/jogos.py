import forca
import jogoAdvinhacao

print('*****************')
print('Escolha seu jogo!')
print('*****************')

print('(1) Forca (2) Adivinhação')

jogo = int(input('Qual jogo? '))

if(jogo == 1):
    print('Jogando Forca')
    forca.jogar()
if(jogo == 2):
    print('Jogando Adivinhação')
    jogoAdvinhacao.jogar()