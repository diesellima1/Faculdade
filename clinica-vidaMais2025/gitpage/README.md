# 🏥 Sistema Clínica Vida+ com Ordinix-123 - GitHub Pages

## 📋 Sobre o Projeto

Sistema revolucionário de gestão hospitalar desenvolvido para GitHub Pages, baseado na interface gráfica Python totalmente funcional. O sistema implementa o inovador **Sistema Ordinix-123** de classificação de prioridades médicas.

**Inventor:** Adevilson de Lima - Estudante ADS Anhanguera  
**Tecnologias:** HTML5, CSS3, JavaScript ES6+  
**Compatibilidade:** Todos os navegadores modernos  

## 🚀 Funcionalidades Principais

### 🔐 Sistema de Autenticação
- Login seguro com validação de credenciais
- Opção "Lembrar-me" com localStorage
- Logout com confirmação
- Interface responsiva e moderna

### 📊 Dashboard Inteligente
- Estatísticas em tempo real
- Contadores de pacientes por prioridade
- Fila Ordinix-123 dinâmica
- Relógio digital atualizado

### 👥 Gestão de Pacientes
- Cadastro completo com validações
- Busca avançada por nome, CPF ou telefone
- Lista de pacientes com ordenação
- Modal de detalhes expandido
- Sistema de edição e exclusão

### 🚨 Sistema Ordinix-123
O sistema revolucionário de triagem que classifica pacientes em três níveis:

#### 🟢 Nível 1 - VERDE (Normal)
- Casos não urgentes
- Atendimento por ordem de chegada
- Sintomas leves

#### 🟡 Nível 2 - AMARELO (Urgente)
- Casos que necessitam atenção prioritária
- Sintomas moderados
- Febre alta, dores intensas

#### 🔴 Nível 3 - VERMELHO (Emergência)
- Casos críticos com risco de vida
- Atendimento imediato obrigatório
- Sintomas graves: dor no peito, falta de ar, convulsões

### 📈 Relatórios Avançados
- Estatísticas gerais do sistema
- Distribuição por faixa etária
- Sintomas mais comuns
- Exportação de dados em JSON
- Backup automático

### ⚙️ Configurações
- Limpeza de dados do sistema
- Backup e restauração
- Configurações de usuário

## 🛠️ Estrutura do Projeto

```
gitpage/
├── index.html          # Página principal
├── css/
│   └── styles.css      # Estilos do sistema
├── js/
│   └── app.js          # Lógica principal
├── assets/             # Recursos (imagens, ícones)
└── README.md           # Documentação
```

## 🔧 Como Usar

### 1. Acesso ao Sistema
- Abra o arquivo `index.html` no navegador
- Use as credenciais: **Adevilson de lima** / **Anhanguera2025**
- Marque "Lembrar-me" para login automático

### 2. Navegação
- **Dashboard:** Visão geral do sistema
- **Cadastro:** Registrar novos pacientes
- **Busca:** Localizar pacientes específicos
- **Lista de Pacientes:** Visualizar todos os registros
- **Painel Ordinix:** Monitorar emergências
- **Relatórios:** Análises e estatísticas
- **Configurações:** Gerenciar sistema

### 3. Cadastro de Pacientes
1. Preencha todos os campos obrigatórios
2. O sistema calculará automaticamente a prioridade
3. Pacientes críticos geram alertas automáticos
4. Dados são salvos no localStorage

### 4. Sistema de Prioridades
O algoritmo Ordinix-123 considera:
- **Temperatura corporal**
- **Sintomas relatados**
- **Idade do paciente**
- **Sinais vitais**

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- 💻 Desktops (1200px+)
- 📱 Tablets (768px - 1199px)
- 📱 Smartphones (até 767px)

## 💾 Persistência de Dados

- Utiliza **localStorage** para armazenamento local
- Dados persistem entre sessões
- Backup e exportação disponíveis
- Importação de dados via JSON

## 🎨 Design System

### Cores Principais
- **Primária:** #2c3e50 (Azul escuro)
- **Secundária:** #3498db (Azul claro)
- **Sucesso:** #27ae60 (Verde)
- **Aviso:** #f39c12 (Amarelo)
- **Perigo:** #e74c3c (Vermelho)

### Tipografia
- **Fonte Principal:** 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Tamanhos:** 12px a 24px
- **Pesos:** 400 (normal), 600 (semi-bold), 700 (bold)

## 🔒 Segurança

- Validação de CPF com algoritmo oficial
- Sanitização de inputs
- Proteção contra XSS
- Dados criptografados no localStorage

## 📊 Métricas e Analytics

O sistema coleta automaticamente:
- Número total de pacientes
- Distribuição por prioridade
- Tempo médio de cadastro
- Sintomas mais frequentes

## 🚀 Deploy no GitHub Pages

1. Faça upload da pasta `gitpage` para seu repositório
2. Vá em Settings > Pages
3. Selecione a branch main
4. Escolha a pasta `/gitpage` como source
5. Acesse via: `https://seuusuario.github.io/seurepositorio`

## 🔄 Atualizações Futuras

- [ ] Integração com APIs médicas
- [ ] Sistema de notificações push
- [ ] Relatórios em PDF
- [ ] Integração com impressoras
- [ ] Sistema de agendamento
- [ ] Chat interno para equipe
- [ ] Módulo de farmácia
- [ ] Controle de leitos

## 📞 Suporte

Para dúvidas ou sugestões:
- **Desenvolvedor:** Adevilson de Lima
- **Instituição:** Anhanguera - ADS
- **Projeto:** Sistema Clínica Vida+ com Ordinix-123

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do curso de Análise e Desenvolvimento de Sistemas da Anhanguera.

---

**© 2025 Adevilson de Lima - Todos os direitos reservados**

*Sistema desenvolvido com 💙 para revolucionar o atendimento hospitalar*