'''
Problema: beecrowd | 1002
Data: 2026.04.11
'''
# Objetivo: Calcular a área de uma circnferencia
# --- ANÁLISE (LIAC) ---
# Entrada: contem um  valor de um número flutuante
#Procesamento: calcular o raio
# Saída: apre4neentar a mensagem "A=" seguido pelo o valor
R = float(input())
pi = 3.14159
AREA = pi * (R ** 2)
print(f"A={AREA:.4f}")