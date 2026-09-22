# Adivhe cartas
Jogo autoral do meu fliperama. Abre pela opcao [4] do menu.
Autor: Maria Julia Pereira Majer

## A regra

O computador vai escolher uma carta no baralho e o jogador vai ter que adivinhar o naipe e o numero
## Como jogar

1. Dentro da pasta `fliperama`, rode `python3 main.py`.
2. Escolha a opcao `[4]` no menu.
3. Depois que o computador escolher uma carta, o jogador vai ter que acertar o naipe e o numero 

## O que eu reusei do projeto, e onde

| Peca | De qual modulo | Onde eu uso | Para que serve ali |
|---|---|---|---|
| `titulo()` | `telas.py` | `meujogo.py`, linha 20 | desenha a testeira do jogo |
| `linha()` | `telas.py` | `meujogo.py`, linha [18] | fecha a tela no fim da partida |
| `ler_numero()` | `modulos.py` | `meujogo.py`, linha [N] | pede o numero e recusa fora do intervalo |
| contagem da partida | `placar.py` | `main.py`, linha [22] | soma 1 em `vezes_jogado` a cada partida |



## Exemplo de execucao

```
(Vou ter que escrever o que é pra aparecer pq nao to conseguindo chamar no terminal) É para aprecer que escolheu uma carta e que a pessoa acertar o naipe e o numero 
```

## O que ainda nao funciona

- Ele ainda tem alguams dificuldaes sobre a escolha 