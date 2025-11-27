/*
Você está trabalhando em uma empresa que está desenvolvendo um software para 
uma loja de eletrodomésticos. Nesse sistema, temos a necessidade de calcular o 
preço final de um produto com base no preço de venda e na incidência de taxas 
fixas de impostos e descontos aplicáveis. Por exemplo, suponha que o preço de 
venda de um televisor seja de R$ 1500.00. Vamos considerar que a taxa de imposto 
aplicável seja de 10%, e que haja um desconto padrão de 5% para esse produto em 
particular.
*/
#include <stdio.h>
#define PRECO_VENDA 1500.00
#define TAXA_IMPOSTO 0.10   // 10%
#define DESCONTO 0.05       // 5%
int main() {
    double preco_final;
    double imposto = PRECO_VENDA * TAXA_IMPOSTO;
    double desconto = PRECO_VENDA * DESCONTO;
    
    preco_final = PRECO_VENDA + imposto - desconto;
    
    printf("Preco final do televisor: R$ %.2f\n", preco_final);
    return 0;
}
// Preço final do televisor: R$ 1575.00
// Explicação:
// 1. Calculamos o imposto como 10% do preço de venda: R$   1500.00 * 0.10 = R$ 150.00
// 2. Calculamos o desconto como 5% do preço de venda: R$   1500.00 * 0.05 = R$ 75.00
// 3. Calculamos o preço final: R$ 1500.00 + R$ 150.00 - R$ 75.00 = R$ 1575.00 
// Portanto, o preço final do televisor, após aplicar o imposto e o desconto, é R$ 1575.00.
// Obs: Utilizamos constantes para representar o preço de venda, a taxa de
// imposto e o desconto, facilitando futuras alterações nesses valores. 
// Além disso, o uso de variáveis auxiliares para o cálculo do imposto e do
// desconto torna o código mais legível.
// Este exemplo demonstra a aplicação prática de constantes e operações
// aritméticas em C para resolver um problema do mundo real.
// Você pode adaptar esse código para diferentes produtos, taxas de imposto
// e descontos conforme necessário.
