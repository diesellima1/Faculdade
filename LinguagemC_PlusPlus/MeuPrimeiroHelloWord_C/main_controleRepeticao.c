/*
Faça um programa em C que calcula a idade média de um grupo de 5 pessoas. 
A finalização da entradada de números é dada por um 0.
O programa não de aceitar idades negativas.
*/
#include <stdio.h>

int main() {
    int idade, soma = 0, contador = 0;

    while (1) {
        printf("Digite a idade (0 para sair): ");
        scanf("%d", &idade);

        if (idade == 0) {
            break; // Encerra o loop se a idade for 0
        }

        if (idade < 0) {
            printf("Não existe idade negativa. Tente novamente...\n");
            continue; // Pula para a próxima iteração se a idade for negativa
        }

        soma += idade;
        contador++;
    }

    if (contador > 0) {
        float media = (float)soma / contador;
        printf("A idade média do grupo é: %.2f\n", media);
    } else {
        printf("Nenhuma idade válida foi inserida.\n");
    }

    return 0;
}