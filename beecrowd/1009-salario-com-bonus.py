'''
Problema: beecrowd | 1009
Data: 2026.04.11
Estudante: Maria Julia Pereira Majer
'''
# Objetivo: Ler nome, salário fixo e total de vendas; calcular e exibir o total a receber

#--- ANÁLISE (LIAC)---
# Entrada: nome (texto), salário (float), total de vendas efetuadas (float)
# Processamento: comissão = vendas * 0.15 total = salaário fixo + comissão
# Saída: exibir no formato exato "TOTAL = R$ valor" com 2 casas decimais

# input () sem conversão retorna o nome como texto (str)
n = input()

# float(input()) lê valores monetários (podem ter casas decimais)
s = float(input()) # salário fixo
v = float(input()) # total de vendas efetuadas no mês

# O vendendor ganha 15% de comissão sobre o total de vendas
c = v * 0.15

# Total a receber = salário fixo + comissão
st = s + c

# : .2f dentro da f-string formata o número com exatamente 2 casas decimais
print(f"TOTAL = R$ {st:.2f}")