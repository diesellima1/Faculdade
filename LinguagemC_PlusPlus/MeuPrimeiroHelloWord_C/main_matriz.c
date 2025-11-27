/*
Criar uma Matriz identidade com deimensões 5 x 5
100
010
001
*/

#include <stdio.h>  // Biblioteca padrão de entrada e saída
#include <stdlib.h> // Biblioteca padrão para funções utilitárias

int main() {
    int matriz[5][5];   // Declaração de uma matriz 5x5

    for(int i=0; i<5; i++) { // loop para linhas
        for(int j=0; j<5; j++) { // loop para colunas
            if(i == j) {
                matriz[i][j] = 1; // Atribui 1 na diagonal principal
            } else {
                matriz[i][j] = 0; // Atribui 0 nas outras posições
            }
        }

    }
    printf("Matriz Identidade 5x5:\n");
    for(int i=0; i<5; i++) { // loop para linhas
        for(int j=0; j<5; j++) { // loop para colunas
            printf("%d ", matriz[i][j]); // Imprime o elemento da matriz
        }
        printf("\n"); // Nova linha após cada linha da matriz formatação para pular uma linha
    }
    return 0; // Indica que o programa terminou com sucesso
}