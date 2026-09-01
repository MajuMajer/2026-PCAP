#==========================
# Arquivos: main.py
# Disciplina: 2026-PCAP
# Aulas: 20
# Autor: Maria Julia Pereira Majer
# Data: 2026.08.04
# Conceitos:
#==========================

#Importar funções de arquios (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_par_ou_impar
from adivinhecartas import jogar_adivinhe_cartas
from modulos import ler_opcao 
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores


NOME_DO_DONO = 'MARIA JULIA'
OPCOES = ['0', '1', '2', '3', '4', '5']

NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Adivinhe cartas']
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

def mostrar_menu():
    titulo('FLIPERAMA DO ' + 'NOME_DO_DONO')
    print('[1] Adivinhe o Numero')
    print('[2] Pedra-Papel-Tesoura')
    print('[3] Par ou Impar')
    print('[4] Adivinhe Cartas')
    print('[5] Jogaores')
    print('[0] Sair')
    linha()      

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('2 - Pedra-Papel-Tesoura')
    print('3 - Par ou Impar')
    print('4 - Adivinhe Cartas')
    print('5 - jogadores')
    print('0 - Sair do Fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo('Até a Proxima!')
        break

    if opcao == '4':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) -1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

    if opcao == '1':
        jogar_adivinhe()
    elif opcao == '2':
        jogar_ppt()
    elif opcao == '3':
        jogar_par_ou_impar()
    elif opcao == '4':
        jogar_adivinhe_cartas()
    else:
        
        input('Pressione Enter para voltar ao menu... ')