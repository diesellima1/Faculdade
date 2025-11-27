/*
Leia 5 números e armazene-os em um vetor.
Imprima em ordem inversa de leitura os elementos do vetor.
*/
#include <stdio.h>  // Biblioteca padrão de entrada e saída

int main() {
    int i, num[5];  // Declara 'i' como contador e 'num' como vetor com 5 posições
    
    // Primeira parte: leitura dos valores do vetor
    for (i = 0; i < 5; i++) {
        printf("Digite a posição %d: ", i); // Pede ao usuário o número da posição atual
        scanf("%d", &num[i]);               // Armazena o valor digitado no vetor
    }

    // Segunda parte: exibição dos valores em ordem inversa
    // OBS: o laço original tinha um erro lógico (i <= 0), ele nunca executaria.
    // O correto é (i >= 0), pois queremos imprimir até o índice 0.
    for (i = 4; i >= 0; i--) {
        printf("%d\n", num[i]); // Imprime os valores do vetor de trás para frente
    }

    printf("\n\n\n"); // Apenas para espaçamento visual no final da execução
    return 0;         // Encerra o programa
}
