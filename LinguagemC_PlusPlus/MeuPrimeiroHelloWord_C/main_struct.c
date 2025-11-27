/*struct  (estrutura) é uma palavra-chave para definir um tipo de dado composto que
agrupa variáveis de diferentes tipos sob um único nome, permitindo organizar dados
relacionados*/

#include <stdio.h>  // Biblioteca padrão de entrada e saída

// Definição de uma estrutura chamada "Pessoa"
struct Pessoa {
    char nome[50];
    int idade;
    float altura;
};

int main() {
    // Declara uma variável do tipo struct Pessoa
    struct Pessoa p1;

    // Solicita os dados ao usuário
    printf("Digite o nome: ");
    fgets(p1.nome, 50, stdin); // Lê uma string (inclui espaços)
    
    printf("Digite a idade: ");
    scanf("%d", &p1.idade);

    printf("Digite a altura (em metros): ");
    scanf("%f", &p1.altura);

    // Exibe os dados armazenados
    printf("\n--- Dados da Pessoa ---\n");
    printf("Nome: %s", p1.nome);
    printf("Idade: %d anos\n", p1.idade);
    printf("Altura: %.2f m\n", p1.altura);

    return 0;
}
