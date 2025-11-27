#include <stdio.h>

int main() {
    int numero;

    // Solicita ao usuário que digite um número
    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    // Usa o operador ternário para verificar se o número é par ou ímpar
    // Sintaxe: condição ? valor_se_verdadeiro : valor_se_falso
    const char* resultado = (numero % 2 == 0) ? "par" : "ímpar";

    // Exibe o resultado
    printf("O número %d é %s.\n", numero, resultado);

    return 0;
}