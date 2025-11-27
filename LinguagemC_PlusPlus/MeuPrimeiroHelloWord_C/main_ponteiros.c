/*Ponteiros armazena um endereços "sistema avançado de programação"
*ptr ele imprime o conteúdo do endereço de memória apontado pelo ponteiro
*/ 

#include <stdio.h>

int main() {
    // Declara um ponteiro para inteiro chamado 'ptr'
    int *ptr = NULL; 
    // Inicialmente o ponteiro aponta para "NULL", ou seja, para nenhum endereço válido.
    // Isso é uma boa prática para evitar erros (ponteiros "soltos").

    printf("Valor inicial de ptr: %p (NULL significa que não aponta para nada)\n", ptr);

    int numero = 10; // Cria uma variável comum chamada 'numero'

    // Agora fazemos o ponteiro 'ptr' apontar para o endereço de memória de 'numero'
    ptr = &numero;

    printf("\nEndereco de memoria de 'numero': %p\n", &numero);
    printf("Valor armazenado em 'numero': %d\n", numero);

    // O operador * é usado para acessar o valor do endereço apontado pelo ponteiro
    printf("\nAgora ptr aponta para 'numero'.\n");
    printf("Endereco armazenado em ptr: %p\n", ptr);
    printf("Conteudo do endereco apontado por ptr (*ptr): %d\n", *ptr);

    return 0;
}
