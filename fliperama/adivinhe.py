#================
#ARQUIVO: aivinhe.py (pasta fliperama)
#Conceito: Jogo como modulo, while, randint()
#Base: seu jogo da Aula 16 (atividade10), Refeito aqui
#Autor: Maria Julia Pereira Majer
# Data: 2026.08.11
# ===============

from random import randint
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NUMERO')
    print('Tente adivinhar o número que estou pensando entre 1 a 10')
    segredo = randint(1, 10)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas +=1

        if palpite < segredo:
            print('O numero secreto é maior. Tente novamente. ')
        elif palpite > segredo:
            print('O  numero secreto é menor. Tente novamente')
        else:
            acertou = True
    else:
        linha()
        print(f'Parabéns! Você acertou o número secreto {segredo} em {tentativas} tentativas.')
        linha()