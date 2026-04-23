'''
Problema: beecrowd | 1037
Data: 2026.04.23
Estudante: Maria Julia Pereira Majer
'''
# Objetiv: Ler um valor float e indicar em qual intervalo ele se encotra

valor = float(input())
if 0 <= valor <= 25:
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
