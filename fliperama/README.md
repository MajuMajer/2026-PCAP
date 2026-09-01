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