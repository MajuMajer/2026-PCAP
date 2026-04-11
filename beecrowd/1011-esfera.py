'''
Problema: beecrowd | 1011
Data: 2026.04.09
Estudante: Maria Julia Pereira Majer
'''
# Objetio: Ler o raio de uma esfera e calcular seu volume com a formula (4/3) * pi *R³

#--- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante (o raio R)
# Peocessamento: aplicar a fórmula do volume da esfera
# Saída: exibir no formato " VOLUME = valor" com 3 casas decimais

R = float(input())
pi = 3.14159
V = (4.0 / 3) * pi * R ** 3
print(f"VOLUME = {V:.3f}")