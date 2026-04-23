'''
Problema: beecrowd | 1010
Data: 2026.04.18
Estudante: Maria Julia Pereira Majer
'''

cod1, qtd1, val1 = input().split()

qtd1 = int(qtd1)
val1 = float(val1)

cod2, qtd2, val2 = input().split()

qtd2 = int(qtd2)
val2 = float(val2)

total = (qtd1*val1) + (qtd2*val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")