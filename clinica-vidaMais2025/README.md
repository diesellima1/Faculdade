# 🏥 Sistema Clínica Vida+ com Ordinix-123

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Ativo-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Sobre o Projeto

Sistema revolucionário de gestão hospitalar desenvolvido com tecnologia **Ordinix-123** para triagem inteligente de pacientes. Criado como projeto acadêmico para demonstrar competências em desenvolvimento de sistemas de saúde.

**Desenvolvedor:** Adevilson de Lima  
**Curso:** Análise e Desenvolvimento de Sistemas - Anhanguera  
**Versão:** 1.0.0

---

## 🎯 Funcionalidades Principais

### ✅ Sistema Ordinix-123 (Triagem Inteligente)
- 🟢 **Nível 1 (Verde)**: Casos normais - SLA 60 minutos
- 🟡 **Nível 2 (Amarelo)**: Casos urgentes - SLA 30 minutos
- 🔴 **Nível 3 (Vermelho)**: Emergências - SLA 15 minutos

### 📊 Módulos do Sistema
1. **Cadastro de Pacientes** - CPF validado, dados completos
2. **Busca Inteligente** - Por nome ou CPF
3. **Fila Ordinix-123** - Priorização automática
4. **Estatísticas** - Relatórios e análises
5. **Impressão** - Individual ou em lote
6. **Agendamentos** - Sistema de pré-cadastro
7. **Compartilhamento** - Entre setores hospitalares

---

## 🚀 Como Instalar

### Pré-requisitos

```bash
Python 3.8 ou superior instalado
Sistema Operacional: Windows, Linux ou macOS
```

### Passo 1: Baixar o Código

```bash
# Opção A: Clone o repositório (se estiver no GitHub)
git clone https://github.com/seu-usuario/clinica-vida-ordinix.git
cd clinica-vida-ordinix

# Opção B: Baixe o arquivo .py diretamente
# Salve como: sistema_clinica_vida.py
```

### Passo 2: Verificar Python

```bash
# Windows
python --version

# Linux/Mac
python3 --version
```

**Resultado esperado:** `Python 3.8.x` ou superior

### Passo 3: Executar o Sistema

```bash
# Windows
python sistema_clinica_vida.py

# Linux/Mac
python3 sistema_clinica_vida.py
```

---

## 📖 Como Usar o Sistema

### Iniciando

1. Execute o arquivo Python
2. O menu principal será exibido
3. Digite o número da opção desejada (1-9)

### Menu Principal

```
🏥 SISTEMA CLÍNICA VIDA+ - ORDINIX-123
=========================================
1. 👤 Cadastrar paciente
2. 📊 Ver estatísticas
3. 🔍 Buscar paciente
4. 📋 Listar todos pacientes
5. 📅 Sistema de Agendamento Inteligente
6. 🖨️ Impressão Individual/Lote
7. 🚨 Painel Ordinix-123
8. 📤 Compartilhar entre setores
9. ❌ Sair
```

---

## 🔧 Guia de Funcionalidades

### 1️⃣ Cadastrar Paciente

**Como fazer:**
1. Escolha opção `1` no menu
2. Digite o **nome completo** do paciente
3. Digite o **CPF** (apenas números - 11 dígitos)
   - ✅ Validação automática com algoritmo oficial
   - ❌ Não aceita CPFs inválidos
4. Digite a **idade** (apenas números)
5. Digite o **telefone** (apenas números)
6. Escolha o **nível Ordinix** (1, 2 ou 3)
7. Confirme o cadastro

**Dica:** Digite `sair` a qualquer momento para cancelar

**Exemplo:**
```
Nome: João Silva
CPF: 12345678901
✅ CPF válido: 123.456.789-01
Idade: 45
Telefone: 51999887766
Nível: 3
```

---

### 2️⃣ Ver Estatísticas

**Como fazer:**
1. Escolha opção `2` no menu
2. Visualize:
   - Total de pacientes cadastrados
   - Idade média
   - Paciente mais novo e mais velho
   - Distribuição por nível Ordinix
3. Pressione ENTER para voltar

---

### 3️⃣ Buscar Paciente

**Como fazer:**
1. Escolha opção `3` no menu
2. Selecione tipo de busca:
   - `1` - Buscar por nome
   - `2` - Buscar por CPF
   - `0` - Voltar ao menu
3. Digite o termo de busca
4. Veja os resultados encontrados

**Dica:** Digite `0` para voltar sem buscar

---

### 4️⃣ Listar Todos os Pacientes

**Como fazer:**
1. Escolha opção `4` no menu
2. Veja lista completa com:
   - 🟢🟡🔴 Indicador visual de prioridade
   - ID, Nome, CPF, Idade, Telefone
3. Pressione ENTER para voltar

---

### 5️⃣ Sistema de Agendamento

**Status:** 🚧 Em desenvolvimento

**Como fazer:**
1. Escolha opção `5` no menu
2. Veja funcionalidades planejadas:
   - Agendar consulta
   - Ver agenda do dia
   - Reagendar por prioridade
   - Relatórios de eficiência
3. Digite `0` para voltar

---

### 6️⃣ Sistema de Impressão

**Como fazer:**
1. Escolha opção `6` no menu
2. Selecione tipo de impressão:
   - `1` - **Individual**: Digite nome do paciente
   - `2` - **Lote**: Imprime todos (requer confirmação)
   - `3` - **Por nível**: Escolha nível 1, 2 ou 3
   - `4` - Relatório personalizado (em desenvolvimento)
   - `0` - Voltar ao menu

**Exemplo de Impressão:**
```
📄 FICHA INDIVIDUAL - CLÍNICA VIDA+
====================================
ID: 1
Nome: João Silva
CPF: 123.456.789-01
Idade: 45 anos
Telefone: 51999887766
Ordinix-123: Nível 3 (Vermelho)
Data/Hora: 29/09/2025 14:30
====================================
```

---

### 7️⃣ Painel Ordinix-123

**Como fazer:**
1. Escolha opção `7` no menu
2. Veja fila de atendimento em tempo real:
   - Ordem de prioridade (3 → 2 → 1)
   - Nome, CPF e horário de chegada
   - Total de pacientes aguardando
3. Pressione ENTER para voltar

**Exemplo:**
```
🚨 PAINEL ORDINIX-123 - FILA DE ATENDIMENTO
============================================
Total na fila: 3 pacientes

1º lugar - 🔴 EMERGÊNCIA
   Nome: João Silva
   CPF: 123.456.789-01
   Chegada: 14:30:15
--------------------------------------------
2º lugar - 🟡 Urgente
   Nome: Maria Santos
   CPF: 987.654.321-00
   Chegada: 14:25:30
```

---

### 8️⃣ Compartilhar entre Setores

**Como fazer:**
1. Escolha opção `8` no menu
2. Veja setores disponíveis:
   - Recepção
   - Enfermagem
   - Médico
   - Farmácia
   - Administração
3. Funcionalidades (planejadas):
   - Lista unificada
   - Permissões por usuário
   - Sincronização em tempo real

---

### 9️⃣ Sair do Sistema

**Como fazer:**
1. Escolha opção `9` no menu
2. Confirme com `s` ou cancele com `n`
3. Sistema encerrado com segurança

---

## ⌨️ Atalhos e Dicas

### Navegação Rápida
- 🔢 **Menu principal**: Digite números de 1 a 9
- 0️⃣ **Voltar**: Digite `0` em qualquer submenu
- ❌ **Cancelar cadastro**: Digite `sair` durante preenchimento
- ⏎ **Retornar**: Pressione ENTER após visualizações

### Validações Automáticas
- ✅ **CPF**: Validação com algoritmo oficial da Receita Federal
- ✅ **Números**: Campos numéricos não aceitam letras
- ✅ **Nível Ordinix**: Aceita apenas 1, 2 ou 3
- ✅ **Campos obrigatórios**: Sistema não prossegue sem preencher

### Segurança
- 🔒 Confirmação antes de sair do sistema
- 🔒 Confirmação de nível de emergência
- 🔒 Confirmação antes de impressão em lote
- 🔒 Validação anti-duplicidade de CPF (planejado)

---

## 🚨 Sistema Ordinix-123 Explicado

### Como Funciona a Priorização?

#### 🔴 Nível 3 - EMERGÊNCIA (Vermelho)
**Quando usar:**
- Hemorragias graves
- Parada cardíaca/respiratória
- Inconsciência
- Trauma grave
- Dor torácica intensa

**Características:**
- ⚡ Prioridade MÁXIMA
- ⏱️ SLA: 15 minutos
- 🔊 Alertas sonoros ativados
- 🔄 Movido automaticamente para início da fila
- 👨‍⚕️ Notificação imediata para equipe médica

#### 🟡 Nível 2 - URGENTE (Amarelo)
**Quando usar:**
- Dor intensa (mas estável)
- Febre alta persistente
- Dificuldade respiratória moderada
- Sangramento controlável
- Vômitos/diarreia intensos

**Características:**
- ⚡ Prioridade ALTA
- ⏱️ SLA: 30 minutos
- 📊 Posicionamento automático na fila

#### 🟢 Nível 1 - NORMAL (Verde)
**Quando usar:**
- Sintomas leves
- Consultas de rotina
- Exames preventivos
- Renovação de receitas
- Acompanhamento pós-tratamento

**Características:**
- ⚡ Prioridade NORMAL
- ⏱️ SLA: 60 minutos
- 📋 Atendimento por ordem de chegada (dentro do nível)

---

## 📊 Exemplos de Uso

### Cenário 1: Paciente de Emergência

```
1. Paciente chega com dor torácica intensa
2. Recepcionista escolhe: 1. Cadastrar paciente
3. Preenche dados + seleciona Nível 3 (Vermelho)
4. Sistema ativa automaticamente:
   🚨 ALERTA DE EMERGÊNCIA
   🔴 Movido para início da fila
   📢 Notificação para equipe médica
   ⏱️ Cronômetro SLA 15 minutos ativado
```

### Cenário 2: Consulta de Rotina

```
1. Paciente agenda retorno de consulta
2. Recepcionista escolhe: 1. Cadastrar paciente
3. Preenche dados + seleciona Nível 1 (Verde)
4. Paciente entra na fila normal
5. Aguarda atendimento por ordem de chegada
```

### Cenário 3: Busca de Paciente

```
1. Médico precisa localizar paciente
2. Escolhe: 3. Buscar paciente
3. Opção: 2. Buscar por CPF
4. Digite CPF: 12345678901
5. Sistema retorna ficha completa do paciente
```

---

## 🛠️ Resolução de Problemas

### ❌ Erro: "Python não é reconhecido"

**Solução:**
1. Verifique se Python está instalado
2. Adicione Python ao PATH do sistema
3. Reinstale Python marcando "Add to PATH"

### ❌ Erro: "CPF inválido"

**Solução:**
- Digite apenas os 11 números do CPF
- Não use pontos nem traços
- Verifique se o CPF está correto
- CPFs com todos os dígitos iguais são inválidos (ex: 11111111111)

### ❌ Erro: "Idade deve conter apenas números"

**Solução:**
- Digite apenas números
- Não use letras, espaços ou caracteres especiais
- Exemplo correto: `45`
- Exemplo errado: `45 anos`

### ❌ Sistema não aceita Nível 4 ou superior

**Solução:**
- O sistema aceita apenas níveis 1, 2 ou 3
- Esta é uma validação de segurança
- Revise a classificação Ordinix-123

---

## 📝 Requisitos Técnicos

### Mínimos
- **Python:** 3.8 ou superior
- **RAM:** 512 MB
- **Espaço em disco:** 10 MB
- **Sistema Operacional:** Windows 7+, Linux, macOS

### Recomendados
- **Python:** 3.10 ou superior
- **RAM:** 2 GB
- **Processador:** Dual-core 2.0 GHz
- **Resolução:** 1280x720 ou superior

---

## 🔐 Segurança e Privacidade

### Conformidade LGPD
- ✅ Dados armazenados localmente (sessão)
- ✅ Sem envio de dados para servidores externos
- ✅ CPF validado mas não compartilhado
- ✅ Sistema não mantém dados após encerramento

### Boas Práticas
- 🔒 Não compartilhe CPFs completos em telas públicas
- 🔒 Use controle de acesso por usuário (implementar)
- 🔒 Realize backups regulares dos dados
- 🔒 Treine equipe sobre LGPD

---

## 🎓 Objetivos Educacionais

Este projeto demonstra competências em:

1. **Programação Python**
   - Classes e métodos
   - Estruturas de controle
   - Validação de dados

2. **Lógica de Negócio**
   - Algoritmos de priorização
   - Regras de triagem hospitalar
   - Gestão de filas

3. **Experiência do Usuário**
   - Interface intuitiva
   - Validações em tempo real
   - Mensagens claras de erro

4. **Boas Práticas**
   - Código documentado
   - Tratamento de exceções
   - Validação de CPF oficial

---

## 📞 Suporte

### Problemas ou Dúvidas?

- 📧 http://www.linkedin.com/in/adevilson-de-lima
- 💬 Issues no GitHub:

### Reportar Bugs

Ao reportar um problema, inclua:
1. Descrição do erro
2. Passos para reproduzir
3. Versão do Python
4. Sistema Operacional
5. Mensagem de erro completa (se houver)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Adevilson de Lima**  
Estudante de Análise e Desenvolvimento de Sistemas  
Anhanguera - 2025

---

## 🎯 Roadmap (Próximas Versões)

### Versão 1.1 (Planejada)
- [ ] Sistema de login com usuários
- [ ] Persistência de dados em banco
- [ ] Agendamento completo
- [ ] Relatórios em PDF

### Versão 2.0 (Futura)
- [ ] Interface gráfica (GUI)
- [ ] Integração com impressoras térmicas
- [ ] Dashboard web em tempo real
- [ ] API REST para integração

---

## 🌟 Agradecimentos

- Anhanguera - Instituição de Ensino
- Professores e colegas de turma
- Tutor(a):RICARDO HIROSHI JULIO SUZUKI Pós-graduado
- Comunidade Python Brasil
- PROJETO_INTEGRADO_INOVACAO_ADS_2025.2

---
## 🔒 Password Interface gráfica ordinix-123
usuario: Adevilson de lima
senha: Anhanguera2025


---

## 📚 Referências

- [Documentação Python](https://docs.python.org/3/)
- [Protocolo de Manchester](https://www.protocolo-manchester.com/)
- [LGPD - Lei Geral de Proteção de Dados](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [Validação de CPF - Receita Federal](http://www.receita.fazenda.gov.br/)

---

<div align="center">

**Feito com ❤️ por Adevilson de Lima**

⭐ Se este projeto foi útil, deixe uma estrela no GitHub!

</div>