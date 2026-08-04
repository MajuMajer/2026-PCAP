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
from modulos import ler_opcao 
NOME_DO_DONO = 'MARIA JULIA'
OPCOES =['0', '1']

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('0 - Sair do Fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        print('Até a Proxima!')
        break
    elif opcao == '1':
         jogar_adivinhe()
   