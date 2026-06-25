# ============
# Disciplina : Pensamento Computaacional, Algoritmo e Programação (PCAP)
# Projeto : Jogo "Par ou Ímpar"
# Arquivo : par_impar.py
#Autor : Maria Julia Pereira Majer
# Data : 2026/06/25
# ============

import random

numero_secreto = random.randint(0,5)
dedos_jogador = int(input("dedos jogador(0 a 5): "))
entrada = input("Sua jogada (par ou ímapr): ")
jogada = entrada.lower().strip()
opcoes = ["par", "ímpar"]
if jogada not in opcoes:
    print("Jogada inválida!")

numero = int(input("Digite um nùmero): "))

print(10 % 2)
print(7 % 2)
if numero % 2 == 0:
    print("par")
else:
    print("ìmpar")

def quem_venceu(soma, aposta):
    if soma % 2 ==0:
        pariedade = "par"
    else:
        pariedade = "ímpar"
    if pariedade == aposta:
        return "jogador"
    else:
        return "máquina"

pontos_jogador = 0
pontos_maquina = 0
for rodada in range(0,5):
    print("--- Rodada", rodada, "---")
    pontos_jogador = pontos_jogador + 1
print("Placar -> Você:", pontos_jogador, "|Máquina:", pontos_maquina)