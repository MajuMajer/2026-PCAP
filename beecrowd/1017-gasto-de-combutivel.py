'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Maria Julia Pereira Majer
'''
# Objetivo: mostrar o gasto de tempo em horas e a velociade media da viagem

tempo = int(input())
velocidade = int(input())
distancia = tempo * velocidade
litros = distancia / 12
print(f"{litros:.3f}")