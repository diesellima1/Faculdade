/*
Programa que demonstra a ordem de precedência dos operadores em C.
A precedência determina qual operação é executada primeiro quando não há parênteses.

Ordem de precedência (do maior para o menor):
1. ( ) - Parênteses
2. *, /, % - Multiplicação, Divisão, Módulo
3. +, - - Adição, Subtração
*/

#include <stdio.h>

int main() {
    int a = 10, b = 5, c = 2;
    int resultado;
    
    printf("=== DEMONSTRACAO DE ORDEM DE PRECEDENCIA ===\n\n");
    printf("Valores iniciais: a = %d, b = %d, c = %d\n\n", a, b, c);
    
    // Exemplo 1: Multiplicação antes da adição
    resultado = a + b * c;
    printf("Exemplo 1: a + b * c\n");
    printf("Sem parenteses: %d + %d * %d = %d\n", a, b, c, resultado);
    printf("Calculo: %d + (%d * %d) = %d + %d = %d\n\n", a, b, c, a, b*c, resultado);
    
    // Exemplo 2: Forçando adição primeiro com parênteses
    resultado = (a + b) * c;
    printf("Exemplo 2: (a + b) * c\n");
    printf("Com parenteses: (%d + %d) * %d = %d\n", a, b, c, resultado);
    printf("Calculo: (%d + %d) * %d = %d * %d = %d\n\n", a, b, c, a+b, c, resultado);
    
    // Exemplo 3: Divisão antes da subtração
    resultado = a - b / c;
    printf("Exemplo 3: a - b / c\n");
    printf("Sem parenteses: %d - %d / %d = %d\n", a, b, c, resultado);
    printf("Calculo: %d - (%d / %d) = %d - %d = %d\n\n", a, b, c, a, b/c, resultado);
    
    // Exemplo 4: Expressão complexa
    resultado = a + b * c - b / c;
    printf("Exemplo 4: a + b * c - b / c\n");
    printf("Resultado: %d + %d * %d - %d / %d = %d\n", a, b, c, b, c, resultado);
    printf("Calculo: %d + (%d * %d) - (%d / %d) = %d + %d - %d = %d\n\n", 
           a, b, c, b, c, a, b*c, b/c, resultado);
    
    // Exemplo 5: Módulo (resto da divisão)
    resultado = a + b % c;
    printf("Exemplo 5: a + b %% c (modulo)\n");
    printf("Resultado: %d + %d %% %d = %d\n", a, b, c, resultado);
    printf("Calculo: %d + (%d %% %d) = %d + %d = %d\n\n", a, b, c, a, b%c, resultado);
    
    printf("=== RESUMO DA PRECEDENCIA ===\n");
    printf("1. Parenteses ( ) tem prioridade maxima\n");
    printf("2. *, /, %% executam antes de + e -\n");
    printf("3. Operacoes de mesma precedencia: da esquerda para direita\n");
    
    return 0;
}