'''
Este código realiza duas interações simples com o usuário:

Solicita o nome do projeto e exibe uma mensagem de boas-vindas personalizada, destacando que o código é um artefato gerenciado.
Pede dois números ao usuário, calcula a soma deles e mostra o resultado. Se o usuário digitar algo que não seja número, exibe uma mensagem de erro.
Ao final, reforça a importância do código-fonte como artefato controlado e versionado, alinhado com práticas de governança de software.
'''


def saudacao_projeto(nome_projeto):
    """
    Função que retorna uma mensagem de boas-vindas para o projeto de software.
    """
    return f"Olá do projeto '{nome_projeto}'! Este é um artefato de código-fonte gerenciado."

def calcular_soma(a, b):
    """
    Função simples para somar dois números, demonstrando uma lógica básica de software.
    """
    return a + b

if __name__ == "__main__":
    # Interação com o usuário para obter o nome do projeto
    azul = "\033[94m"
    reset = "\033[0m"
    nome_do_meu_projeto = input(f"{azul}Digite o nome do seu projeto: {reset}")
    print(saudacao_projeto(nome_do_meu_projeto))

    # Interação para somar dois números
    try:
        num1 = float(input(f"{azul}Digite o primeiro número para soma: {reset}"))
        num2 = float(input(f"{azul}Digite o segundo número para soma: {reset}"))
        resultado_soma = calcular_soma(num1, num2)
        print(f"A soma de {num1} e {num2} é: {resultado_soma}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

    print("\nEste arquivo exemplifica a importância de manter o código-fonte como um artefato controlado e versionado.")
    print("É um passo fundamental para o controle de produtos e desenvolvimento de software, conforme a Estratégia e Governança [3].")


    #codigo testado e aprovado simples e funcional para fins didaticos.