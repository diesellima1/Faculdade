/*
Escreva um algoritimo que receba dois valores x e y e calcula e retorna x elevado a z ( sem 
utilizar funções ou operadores de potência). 

for (;;){}

------------------------------

for (inicialização; condição; incremento/decremento){
    //bloco de código
}



--------------------------------
*/

#include <stdio.h> // Biblioteca padrão de entrada e saída

int main() {
    int x, z;           // Variáveis para entrada do usuário
    int res = 1;        // Inicializa resultado como 1

    printf("Digite o valor de x: ");
    scanf("%d", &x);    // Lê o valor de x

    printf("Digite o valor de z: ");
    scanf("%d", &z);    // Lê o valor de z

    // Laço for para calcular x elevado a z
    for(int i = 0; i < z; i++) {
        res = res * x;  // Multiplica res por x a cada iteração
    }

    printf("%d elevado a %d é igual a %d\n", x, z, res); // Exibe o resultado
    return 0; // Finaliza o programa
}