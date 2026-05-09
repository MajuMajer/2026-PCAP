'''
Problema: beecrowd | 1046 - Tempo de jogo
Data: 2026.05.09
Estudante: Maria Julia Pereira Majer
'''
# Objetivo: calcular a hora inicial e ahora final e calcular a duração do jogo 
# --- ANÁLISE (LIAC) ---
# Entrada: dois valores representando inicio e fim
# Processamento: calcurar os dois horarios
# Saída: apresentar a duração de tempo

inicio, fim = map(int, input().split())
if inicio < fim:
    duracao = fim - inicio
else:
    duracao = (24 - inicio) + fim
print(f"O JOGO DUROU {duracao} HORA (S)")
