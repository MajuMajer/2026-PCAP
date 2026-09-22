/* Comentário de Bloco
Programa: Hello.c
Data: 2026.06.22
Autor: Maria Julia Pereira Majer
*/

// importa biblioteca padrão de entrada e saída
#include <stdio.h>

// defino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na Tela ; "entre aspas == texto" ; comando se encerra com ;
    printf("Hello World!\n");

    // Receber 2 valores somar e mostrar p resultado
    int A=0;
    int B=0;
    printf("Digite um valor:");
    scanf("%d", &A);
    printf("Digite outro valor:");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma:%d\n", soma);

   
    // indica que chegou ao fim da função == retorna 0
    return 0;
}

/*
para compilar ==
gcc ,nome-do-arquivo> -o
nome-do -programa

para executar ==
./nome-do-programa
 */