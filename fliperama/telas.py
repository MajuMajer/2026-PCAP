#==========================
# Arquivos: telas.py
# Disciplina: 2026-PCAP
# Aulas: 20
# Autor: Maria Julia Pereira Majer
# Data: 2026.08.04
# Conceitos:
#==========================

# Sefinição da Moldura Caracteres e Tamanho
CAR = '#'
TAM = 60

#Funçãopara dsenhe uma linha na tela 
def linha():
    print(CAR * TAM)

#Função para desenha um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()

