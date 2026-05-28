'''
Problema: beecrowd | 1020
Data: 2026.04.11
Estutante: Maria Julia Pereira Majer
'''
# Objetivo: ler um valor inteiro correspondente a idade da pessoa em dias e iformar anos, meses, e dias 
#: Entrada: o arquivo de entrada contem um valor inteiro
# Saída: imprimir a saída em forma de ano meses e dias

idade_em_dias = int(input())
anos = idade_em_dias // 365
resto = idade_em_dias % 365
meses = resto // 30
dias = resto % 30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")