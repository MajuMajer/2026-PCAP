#==========================
# Arquivos: modulos.py
# Disciplina: 2026-PCAP
# Aulas: 20
# Autor: Maria Julia Pereira Majer
# Data: 2026.08.04
# Conceitos:
#==========================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas:
        print("Opção Inválida, Tente Novamente!")
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numero = []
    for n in range(minimo, maximo + 1):
        numero.append(str(n))
    return int(ler_opcao(mensagem, numero))


def ler_texto(mensagem):
    #So devolve quando o texto nao estiver vazio.
    resposta = input(mensagem + ': ').strip()
    while resposta == '':
        print('Nao pode ficar em branco! Tente de novo.')
        resposta = input(mensagem + ': ').strip()
    return resposta