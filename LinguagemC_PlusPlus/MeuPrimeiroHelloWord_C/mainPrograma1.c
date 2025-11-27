/*O problema...
Uma escola deseja automatizar o processo de gerenciamento de notas e informações de
alunos.
A escola possui várias turmas, cada turma tem vários alunos e cada aluno precisa
de informações como nome, número de matrícula e notas em várias disciplinas.
Criar um programa em C capaz de
Cadastrar aluno em uma turma, lançar notas de aluno, calcular a média de uma
turma, gerar o relatório de turma, exibindo as informações de todos os alunos
pertencentes à turma.*/

/*============================================================
SISTEMA DE GERENCIAMENTO ESCOLAR
Local: Salvar como "sistema_escola.c" na pasta do projeto
Compilar: gcc sistema_escola.c -o sistema_escola
Executar: ./sistema_escola (Linux/Mac) ou sistema_escola.exe (Windows)
============================================================*/

#include <stdio.h>   // Biblioteca para entrada/saída (printf, scanf)
#include <string.h>  // Biblioteca para manipulação de strings (strcpy, strcmp)
#include <stdlib.h>  // Biblioteca para funções gerais (system, etc)

// ============================================================
// DEFINIÇÃO DE CONSTANTES
// Constantes são valores fixos que não mudam durante o programa
// ============================================================
#define MAX_ALUNOS 50        // Máximo de alunos por turma
#define MAX_DISCIPLINAS 5    // Número de disciplinas que cada aluno tem
#define TAM_NOME 100         // Tamanho máximo para nomes

// ============================================================
// ESTRUTURAS DE DADOS
// Structs são como "moldes" que agrupam informações relacionadas
// ============================================================

// Estrutura que representa UM ALUNO
typedef struct {
    char nome[TAM_NOME];                    // Nome do aluno
    int matricula;                          // Número de matrícula único
    float notas[MAX_DISCIPLINAS];           // Array com as notas das disciplinas
    float media;                            // Média das notas do aluno
    int ativo;                              // 1 = aluno cadastrado, 0 = posição vazia
} Aluno;

// Estrutura que representa UMA TURMA
typedef struct {
    char nome_turma[TAM_NOME];              // Nome da turma (ex: "Turma A")
    Aluno alunos[MAX_ALUNOS];               // Array com todos os alunos da turma
    int total_alunos;                       // Contador de alunos cadastrados
} Turma;

// ============================================================
// PROTÓTIPOS DAS FUNÇÕES
// Declaramos aqui as funções que vamos criar depois
// ============================================================
void inicializarTurma(Turma *turma);
void cadastrarAluno(Turma *turma);
void lancarNotas(Turma *turma);
void calcularMedia(Aluno *aluno);
void calcularMediaTurma(Turma *turma);
void gerarRelatorio(Turma *turma);
void exibirMenu();
void limparTela();
void pausar();

// ============================================================
// FUNÇÃO PRINCIPAL (MAIN)
// É aqui que o programa começa a executar
// ============================================================
int main() {
    Turma turma;              // Cria uma variável do tipo Turma
    int opcao;                // Guarda a opção escolhida pelo usuário
    
    // Inicializa a turma (prepara para uso)
    inicializarTurma(&turma);
    
    // Solicita o nome da turma
    printf("=== SISTEMA DE GERENCIAMENTO ESCOLAR ===\n\n");
    printf("Digite o nome da turma: ");
    fgets(turma.nome_turma, TAM_NOME, stdin);
    turma.nome_turma[strcspn(turma.nome_turma, "\n")] = 0; // Remove o '\n'
    
    // Loop principal do programa (menu)
    do {
        limparTela();
        exibirMenu();
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        getchar(); // Limpa o buffer do teclado
        
        // Switch-case: executa diferentes ações baseado na opção escolhida
        switch(opcao) {
            case 1:
                cadastrarAluno(&turma);
                break;
            case 2:
                lancarNotas(&turma);
                break;
            case 3:
                calcularMediaTurma(&turma);
                break;
            case 4:
                gerarRelatorio(&turma);
                break;
            case 0:
                printf("\nEncerrando o sistema...\n");
                break;
            default:
                printf("\nOpcao invalida! Tente novamente.\n");
                pausar();
        }
        
    } while(opcao != 0); // Continua até o usuário digitar 0
    
    return 0; // Retorna 0 indicando que o programa terminou com sucesso
}

// ============================================================
// IMPLEMENTAÇÃO DAS FUNÇÕES
// Aqui criamos o código de cada função declarada acima
// ============================================================

// Função: Inicializa a turma com valores padrão
// Parâmetro: ponteiro para a turma (permite modificar a turma original)
void inicializarTurma(Turma *turma) {
    turma->total_alunos = 0; // Começa sem alunos cadastrados
    
    // Loop que marca todas as posições como vazias
    for(int i = 0; i < MAX_ALUNOS; i++) {
        turma->alunos[i].ativo = 0; // 0 = posição vazia
    }
}

// Função: Cadastra um novo aluno na turma
void cadastrarAluno(Turma *turma) {
    limparTela();
    printf("=== CADASTRAR ALUNO ===\n\n");
    
    // Verifica se ainda há espaço na turma
    if(turma->total_alunos >= MAX_ALUNOS) {
        printf("Turma cheia! Nao e possivel cadastrar mais alunos.\n");
        pausar();
        return; // Sai da função
    }
    
    // Encontra a primeira posição vazia
    int posicao = -1;
    for(int i = 0; i < MAX_ALUNOS; i++) {
        if(turma->alunos[i].ativo == 0) {
            posicao = i;
            break; // Para o loop quando encontrar posição vazia
        }
    }
    
    // Solicita os dados do aluno
    printf("Nome do aluno: ");
    fgets(turma->alunos[posicao].nome, TAM_NOME, stdin);
    turma->alunos[posicao].nome[strcspn(turma->alunos[posicao].nome, "\n")] = 0;
    
    printf("Numero de matricula: ");
    scanf("%d", &turma->alunos[posicao].matricula);
    getchar(); // Limpa o buffer
    
    // Inicializa as notas com 0
    for(int i = 0; i < MAX_DISCIPLINAS; i++) {
        turma->alunos[posicao].notas[i] = 0.0;
    }
    
    turma->alunos[posicao].media = 0.0;
    turma->alunos[posicao].ativo = 1; // Marca como posição ocupada
    turma->total_alunos++; // Incrementa o contador de alunos
    
    printf("\nAluno cadastrado com sucesso!\n");
    pausar();
}

// Função: Lança notas para um aluno específico
void lancarNotas(Turma *turma) {
    limparTela();
    printf("=== LANCAR NOTAS ===\n\n");
    
    // Verifica se há alunos cadastrados
    if(turma->total_alunos == 0) {
        printf("Nenhum aluno cadastrado ainda!\n");
        pausar();
        return;
    }
    
    // Solicita o número de matrícula
    int matricula;
    printf("Digite o numero de matricula do aluno: ");
    scanf("%d", &matricula);
    getchar();
    
    // Busca o aluno pela matrícula
    int encontrado = 0;
    for(int i = 0; i < MAX_ALUNOS; i++) {
        if(turma->alunos[i].ativo == 1 && turma->alunos[i].matricula == matricula) {
            encontrado = 1;
            
            printf("\nAluno: %s\n", turma->alunos[i].nome);
            printf("Lancando notas das %d disciplinas:\n\n", MAX_DISCIPLINAS);
            
            // Solicita a nota de cada disciplina
            for(int j = 0; j < MAX_DISCIPLINAS; j++) {
                printf("Nota da disciplina %d: ", j + 1);
                scanf("%f", &turma->alunos[i].notas[j]);
            }
            getchar();
            
            // Calcula a média do aluno
            calcularMedia(&turma->alunos[i]);
            
            printf("\nNotas lancadas com sucesso!\n");
            printf("Media do aluno: %.2f\n", turma->alunos[i].media);
            break;
        }
    }
    
    if(!encontrado) {
        printf("\nAluno nao encontrado!\n");
    }
    
    pausar();
}

// Função: Calcula a média de um aluno
void calcularMedia(Aluno *aluno) {
    float soma = 0.0;
    
    // Soma todas as notas
    for(int i = 0; i < MAX_DISCIPLINAS; i++) {
        soma += aluno->notas[i];
    }
    
    // Divide pela quantidade de disciplinas
    aluno->media = soma / MAX_DISCIPLINAS;
}

// Função: Calcula a média geral da turma
void calcularMediaTurma(Turma *turma) {
    limparTela();
    printf("=== MEDIA DA TURMA ===\n\n");
    
    if(turma->total_alunos == 0) {
        printf("Nenhum aluno cadastrado ainda!\n");
        pausar();
        return;
    }
    
    float soma_medias = 0.0;
    int alunos_com_notas = 0;
    
    // Soma as médias de todos os alunos
    for(int i = 0; i < MAX_ALUNOS; i++) {
        if(turma->alunos[i].ativo == 1) {
            soma_medias += turma->alunos[i].media;
            alunos_com_notas++;
        }
    }
    
    // Calcula e exibe a média da turma
    if(alunos_com_notas > 0) {
        float media_turma = soma_medias / alunos_com_notas;
        printf("Turma: %s\n", turma->nome_turma);
        printf("Total de alunos: %d\n", turma->total_alunos);
        printf("Media geral da turma: %.2f\n", media_turma);
    } else {
        printf("Nenhum aluno com notas lancadas!\n");
    }
    
    pausar();
}

// Função: Gera relatório completo da turma
void gerarRelatorio(Turma *turma) {
    limparTela();
    printf("============================================\n");
    printf("       RELATORIO DA TURMA: %s\n", turma->nome_turma);
    printf("============================================\n\n");
    
    if(turma->total_alunos == 0) {
        printf("Nenhum aluno cadastrado ainda!\n");
        pausar();
        return;
    }
    
    // Percorre todos os alunos e exibe suas informações
    for(int i = 0; i < MAX_ALUNOS; i++) {
        if(turma->alunos[i].ativo == 1) {
            printf("--------------------------------------------\n");
            printf("Nome: %s\n", turma->alunos[i].nome);
            printf("Matricula: %d\n", turma->alunos[i].matricula);
            printf("Notas: ");
            
            // Exibe todas as notas
            for(int j = 0; j < MAX_DISCIPLINAS; j++) {
                printf("%.2f ", turma->alunos[i].notas[j]);
            }
            
            printf("\nMedia: %.2f\n", turma->alunos[i].media);
            
            // Indica se o aluno foi aprovado ou reprovado
            if(turma->alunos[i].media >= 7.0) {
                printf("Situacao: APROVADO\n");
            } else if(turma->alunos[i].media >= 5.0) {
                printf("Situacao: RECUPERACAO\n");
            } else {
                printf("Situacao: REPROVADO\n");
            }
        }
    }
    
    printf("--------------------------------------------\n");
    printf("\nTotal de alunos na turma: %d\n", turma->total_alunos);
    
    pausar();
}

// Função: Exibe o menu principal
void exibirMenu() {
    printf("============================================\n");
    printf("    SISTEMA DE GERENCIAMENTO ESCOLAR\n");
    printf("============================================\n\n");
    printf("1 - Cadastrar aluno\n");
    printf("2 - Lancar notas\n");
    printf("3 - Calcular media da turma\n");
    printf("4 - Gerar relatorio da turma\n");
    printf("0 - Sair\n\n");
    printf("============================================\n");
}

// Função: Limpa a tela do terminal
void limparTela() {
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear"); // Linux/Mac
    #endif
}

// Função: Pausa a execução até o usuário pressionar Enter
void pausar() {
    printf("\nPressione ENTER para continuar...");
    getchar();
}