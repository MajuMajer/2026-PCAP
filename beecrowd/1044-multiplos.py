'''
Promeba: beecrowd | 1044
Data: 2026.04.18
Estudante: Maria Julia Pereira Majer
'''
# Objrtivo: Verificar se dois inteiros são multiplos entre si

# --- ANÁLISE (LIAC) ---
# Entrada: dois inteiros A e B mesma linha separados por espaço
# Processament: indentificar maior e menor verificar se maior 4 menor == 0
# Saída: "São Multiplos" ou "Não são Multiplos"

A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A
if maior % menor == 0:
    print("São Multiplos")
else:
    print("Não são Multiplos")