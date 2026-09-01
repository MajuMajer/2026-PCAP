#============================
# ARQUIVO : ppt.py (pasta fliperama)
#Conceitos: Jogo com modulo, lista como tabela de nomes, funçao com retorno operador % para dar a volta
#Base: Jogo da auala 17 (atividade 11)
# Autor: Mria Julia Pereira Majer
#Data: 2026.08.28
#============================
from random import randint
from telas import titulo, linha
from modulos import ler_numero
from modulos import ler_opcao
from modulos import jogador_opcao
from modulos import jogador_num
def jogar_par_ou_impar():
    titulo('JOGO DON PAR OU ÍMPAR')
    vitoria  = 0

    while True:
        comp_num = randint(0, 5)

        print('Escolha seu movimento:')
        jogador_opcao = input('Par ou Ímpar? [P/I]: ').strip().lower()[0]
        while jogador_opcao not in 'PI':
            jogador_opcao = input('Opção inválida! Escolha P ou I: ').strip().lower()[0]

        jogador_num = ler_numero('Digite quantos dedos vai jogar (0 a 5)', 0,5)

        total = comp_num + jogador_num
        resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR'

        linha()
        print(f'Você jogou {jogador_num} e o computador {comp_num}. Total de {total} deu {resultado}!')
        linha()

        if(jogador_opcao == 'P' and resultado == 'PAR') or (jogador_opcao == 'I' and resultado == 'ÍMPAR'):
            print('Você VENCEU! Vamos jogar novament...')
            vitorias += 1
            linha()
        else:
            print('Você PERDEU!')
            linha()
            break

    print(f'Fim de jogo! Você conseguiu uma sequência de {vitorias} vitórias.')