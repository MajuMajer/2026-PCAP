# 🎮 Adivinhe o Número
​
Jogo de adivinhação feito em Python na disciplina PCAP (Aula 16).
O computador sorteia um número e você tenta descobrir dentro de um
limite de chances. Tem 3 níveis: Fácil, Médio e Impossível.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python adivinhe.py
3. Escolha o nível (1, 2 ou 3) e tente adivinhar!
​

# Variaveis 
Linha 12
numero_secreto: é usado para comparar com o número que o jogador escolheu
Linha 31
nives =: por estar almentando as dificuldades aramzenando os números 
Linha 45
venceu =: por ir acomulando os niveis que o jogador está

# Operadores
Linha 21
elif palpite < numero_secreto: serve para calcular o número do palpite do jogador com o secreto
Linha 15
while chances > 0 and not acertou: serve que as chances acabaram e errou 
Linha 26
- 1: diminue as chances que o jogador vai ter 

# Estrutura de Repetição 
Linha 15
While chances: vai dando uma quantidade de chances para o jogador 

# Estrutura de condição 
Linha 18
if paplpte == numero_secreto: sereve para falar que o jogador acertou 
Linha 23
else:
serve para falar que o palpite do jogador é muuito alto 
Linha 47
if not venceu: serve para falar que o jogador perdeu 

# Sub rotina 
Linha 11
def jogar (maximo, chances): é para dar um número maximo de para o numero secreto

# Entrada
Linha 16
input ("seu palpite (1 a " + str(maximo) + "): ")): serve para o jogador dar um palpite de um numero maximo 
Linha 42
(input (digite 1, 2 ou 3: ")): para escoler o nivel que o jogador que jogador ou que nivel ele esta 

# Saida
Linha 38
print("Escolha o nível de dificuldade): vai escolher em 1, 2 ou 3 de dificuldade 
Linha 44
print("voce ecolheu o nivel:" , nivel[0]): erve para começar o nivel que voce escolheu 
print("chances restantes:" , chances): a quantidadde de chances que a pessoa ainda tem
​## 🎯 Autoavaliação
Conceito pretendido: [ A / B / C / D ]
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: par_impar.py, linhas 9 a  48
 Extensão/originalidade .....: par_impar.py, B


​
Autor: Maria Julia Pereira Majer 