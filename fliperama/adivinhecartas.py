#================
#ARQUIVO: aivinhe.py (pasta fliperama)
#Conceito: Jogo como modulo, while, randint()
#Base: seu jogo da Aula 16 (atividade10), Refeito aqui
#Autor: Maria Julia Pereira Majer
# Data: 2026.08.30
# ===============
from random import choice
from telas import titulo, linha
from modulos import ler_numero
from modulos import jogar_adivinhe_carta
from modulos import valor_secreto
from modulos import naipe_secreto
from modulos import palpite_naipe
from modulos import palpite_valor
from modulos import carta_formata
from modulos import carta_secreta
def jogar_adivinhe_carta():
    titulo('JOGO ADINHE A CARTA')

    # Definicao dos naipes e valor das cartas
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    # O computador vai escolher uma carta 
    naipe_secreto = choice(naipes)
    valor_secreto = choice(valores)
    print('Tente adivinhar a carta que eu tirei do baralho!')
    print(f'Os naipes possíveis são:{' , '.join(naipes)}')

    tentativas = 0
    acertou = False 

    while not acertou:
        linha()
        print('Dica: Você precisa acertar o NAIPE e o VALOR.')


        palpite_naipe = input('Digite o NAIPE  da carta: ').strip().lower()
        palpite_valor = input('Digite o VALOR da carta').strip().lower()
        tentativas += 1

        if palpite_naipe == naipe_secreto and palpite_valor == valor_secreto:
            acertou = True
        else:
            print('\nErrado! Deixe - me te dar uma pista:')
            if palpite_naipe != valor_secreto[0]:
                print(f' -> Você ACERTOU o valor({palpite_valor}), mas ERROU o naipe!')
            elif palpite_naipe == valor_secreto[1]:
                print(f'-> Você ERROU o valor, mas Acertou ({palpite_naipe})!')

    else:
        linha()
        carta_formatada = (f'{carta_secreta[0]} de {carta_secreta[1]}')
        print(f'Parabéns! Você acertou a carta secreta ({carta_formatada}) em {tentativas} tentativas.')
        linha()