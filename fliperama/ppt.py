#============================
# ARQUIVO : ppt.py (pasta fliperama)
#Conceitos: Jogo com modulo, lista como tabela de nomes, funçao com retorno operador % para dar a volta
#Base: Jogo da auala 17 (atividade 11)
# Autor: Mria Julia Pereira Majer
#Data: 2026.08.11
#============================

#importa funçao randint da biblioteca random, que sorteia um numero inteiro aleatorio em intervalo definido
from random import randint

# importa a funçao titulo e linha do arquivo telas.py
from telas import titulo, linha

#importa a funçao ler_opçao que valida a entrada do usuario do arquivo modulos.py
from modulos import ler_opcao

#lista com PEDRA == posiçao 0; PAPEL == 1; TESOURA == 2
JOGADAS = ["PEDRA", "PAPEL", "TESOURA"]

#definir jogador

def quem_vence(jogador, computador):
    if jogador == computador:
        return 'empate'
    if jogador == (computador + 1) % 3:
        return 'jogador'
    return 'computador'

#mostrar as opçoes de jogo

def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')

def jogar_ppt():
    titulo('Pedra - Papel - Tesoura')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você Jogou ' + JOGADAS[jogador] + '.')
        print('Computador Jogou ' + JOGADAS[computador] + '.')

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguém venceu!')
        elif resultado == 'jogador':
            pontos_jogador += 1
            print('Você Venceu essa rodada!')
        elif resultado == 'computador':
            pontos_computador += 1
            print('Computador Venceu essa rodada!')
        linha()
        print(f'Placar: Jogador {pontos_jogador} X {pontos_computador} Cmputador')
        linha()
    if pontos_jogador > pontos_computador:
        titulo('YOU WIN')
    else:
        titulo('YOU LOSE')
