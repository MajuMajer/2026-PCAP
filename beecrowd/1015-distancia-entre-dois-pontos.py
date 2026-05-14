'''
Problema: beecrowd | 1015
Data: 2026.05.14
Nome: Maria Julia Pereira Majer
'''
# Objetivo: ler os quatros valores correspondentes ao eixo X
# --- ANÁLISE (LIAC) ---
# Entrada: ler duas linhas de dados
# Processamento: calcular as duas linhas de dados
# Saída: Calcular e imprimir o valor da distância

import math
line1 = input().split()
x1 = float(line1[0])
y1 = float(line1[1])
line2 = input().split()
x2 = float(line2[0])
y2 = float(line2[1])
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4}" .format(distancia))