'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Maria Julia Pereira Majer
'''
# Objetivo: mostrar o gasto de tempo em horas e a velociade media da viagem
# ---ANALIE (LIAC) ---
# Entrada: contem dois inteiros o tempo gasto de viagem em horas e o sesgundos e a velocidade
#saida: imprimir a qauntidade necesária de litros de combustivel que vai ser ultilizado 
tempo = int(input())
velocidade = int(input())
distancia = tempo * velocidade
litros = distancia / 12
print(f"{litros:.3f}")