'''
Problema: beecrowd | 1051 - imposto de renda
Data: 2026.05.09
Estudante: Maria Julia Pereira Majer
'''
# Objetvo: calcular quanto de imposto de renda paga
# --- ANÁLISE (LIAC) ---
# Entrada: contei apenas um valor e um ponto flutuante
# Processamento: calcular o apenas o unico valor com o ponto flutuante 
# Saída: Mostradar o resultado com "R$" seguindo os espaços e do valor total devido de imposto de renda

salario = float(input())
if salario <= 2000.00:
    print("Isento")
else:
    imposto = 0
    if salario > 4500.00:
        imposto += (salario - 4500.00) * 0.28
        salario = 4500.00
    if salario > 3000.00:
        imposto += (salario - 3000.00) * 0.18
        salario = 3000.00
    if salario > 2000.00:
        imposto += (salario - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
