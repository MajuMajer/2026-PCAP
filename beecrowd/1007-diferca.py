'''
Problema: beecrowd | 1007
Data: 2026.04.11
Estudantes: MAria Julia Pereira Majer
'''
# Objetivo: Ler quatro inteiros e calcular Diferenca = (A * B) - (C * D)

# --- ANÁLISE (LIAC) ---
# Entrada: quatro valores inteiros A, B, C e D (um por linha)
# Processamento: difença entre o produto A*B e o produto C*D
# Saída: "DIFEMRENCA = valor" (inteiro, leras maiúsculas, espaço ao redor do =)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Caluclar a difernça dos produtos conforme a fórmula do enunciado
dif = (A * B) - (C * D)

print(f"DIFENCA = {dif}")