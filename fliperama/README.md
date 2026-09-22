# Fliperama da MARIA JULIA

Um fliperama de terminal com quatro jogos, placar que não esquece e cadastro de jogadores. Projeto da disciplina PCAP, primeiro ano do Técico de Informática do IFPR.

## O que ele faz

- Quatro jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura, Par ou Ímpar e Adivinhe a Carta
- Placar que conta quantas vezes cada jogo foi jogado e continua contando mesm depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alterar e excluir 

## Como rodar

```
cd fliperama
python3 main.py
```

## Os arquivos

- `main.py` - gabinete: menu, palcar e chamadas
- `telas.py` - ferramenta visuais
- `modulo.py` - ferramentas de lógica: as três funções que perguntam e conferem 
- `placar.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
-`adivinhe.py`, `ppt.py`, `parimpar.py`, `adinhecartas.py` - um arquivo por jogo
- `plcar.csv` e `jogadores.csv` - os dados, que nascem sozinhos 

A função `ler_texto` ficou no `modulos.py` porque organiza e ultiliza outras vezes a leitura de dados de entrada di usuário em um único lugar dedicado a funções utilitária

## De onde ele veio

- Aula 20: os quatros jogos vieram um programa só, com módulos e menu
- Aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações 
- Aula 23: campo em branco barrado e o projeto documento 

## O que ainda não funciona 
- Nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador

 ## Autoavaliacao

Conceito que eu acho que a minha entrega vale: C

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| [NOME DO MEU JOGO] | `meujogo.py` | `jogar_meujogo` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | B |  |
| 2. As quatro operacoes | C |Pedra-Papel-tesoura, Par ou Impar, Adinhe o Numero e Adivinhe a Carta |
| 3. Busca e indice | B| É facil achar pelo indice |
| 4. Persistencia e primeira execucao | [C] | Nao estava dando certo bem no começo mas agora funciona  |
| 5. Documentacao e autoavaliacao | [C] |  |
| 6. Jogo autoral e reuso | [C] | [Não esta sendo muito funcional] |

### Usei IA?

[Usei um pouco pra saber qual jogo eu poderia fazer porque eu nao sabia qual dava ra fazer]