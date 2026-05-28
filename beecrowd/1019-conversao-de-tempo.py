'''
Problema beecrowd | 1019
Data: 2026.04.11
Estudante: Maria Julia Pereira Majer
'''
# Objetivo: Ler uma duração em segundos e convertê-la para horas:minutos:segundos
#--- ANALISE (LIAC) ---
#Entrada: contem um valor inteiro N
#Saida: imprimir o tempo lido deentrada
N = int(input())
h = N // 3600
N = N % 3600
m = N // 60
s = N % 60
print(f"{h}:{m}:{s}")