# 🏥 CLÍNICA VIDA+ - Sistema Ordinix-123 (Versão Web)

## 📋 Sobre o Projeto

O **CLÍNICA VIDA+** é um sistema híbrido de gestão clínica que combina uma aplicação desktop (Tkinter) com uma moderna interface web. Esta versão web mantém todas as funcionalidades do sistema original, oferecendo uma experiência moderna, responsiva e acessível através de navegadores.

### 🎯 Características Principais

- **Interface Web Moderna**: HTML5, CSS3 e JavaScript ES6+
- **Backend Robusto**: Flask com arquitetura RESTful
- **Comunicação em Tempo Real**: WebSockets com Socket.IO
- **Sistema Ordinix-123**: IA integrada para análise de prioridade de pacientes
- **Design Responsivo**: Compatível com desktop, tablet e mobile
- **Segurança Avançada**: Autenticação, autorização e proteção CSRF
- **Performance Otimizada**: Cache, compressão e lazy loading

## 🚀 Tecnologias Utilizadas

### Backend
- **Flask 2.3.3** - Framework web principal
- **Flask-SocketIO** - Comunicação em tempo real
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Sistema de autenticação
- **Flask-WTF** - Formulários e proteção CSRF
- **Flask-CORS** - Controle de acesso cross-origin

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna com variáveis CSS
- **JavaScript ES6+** - Funcionalidades interativas
- **Bootstrap 5.3** - Framework CSS responsivo
- **Font Awesome 6** - Ícones vetoriais
- **Socket.IO Client** - Comunicação em tempo real

### Utilitários
- **Gunicorn** - Servidor WSGI para produção
- **Redis** - Cache e sessões
- **Pillow** - Processamento de imagens
- **ReportLab** - Geração de PDFs
- **Pandas** - Processamento de dados

## 📁 Estrutura do Projeto

```
clinica-web-app/
├── backend/
│   ├── api/                    # Endpoints da API REST
│   ├── models/                 # Modelos de dados
│   ├── services/               # Lógica de negócio
│   ├── utils/                  # Utilitários
│   ├── app.py                  # Aplicação Flask principal
│   └── interface_grafica_original.py  # Referência do sistema original
├── frontend/
│   ├── components/             # Componentes reutilizáveis
│   ├── pages/                  # Páginas específicas
│   └── utils/                  # Utilitários frontend
├── static/
│   ├── css/
│   │   └── main.css           # Estilos principais
│   ├── js/
│   │   └── main.js            # JavaScript principal
│   ├── img/                   # Imagens e ícones
│   └── fonts/                 # Fontes customizadas
├── templates/
│   ├── base.html              # Template base
│   ├── login.html             # Página de login
│   ├── dashboard.html         # Dashboard principal
│   ├── cadastro.html          # Cadastro de pacientes
│   └── busca.html             # Busca avançada
├── docs/                      # Documentação
├── tests/                     # Testes automatizados
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonagem)

### 1. Preparação do Ambiente

```bash
# Navegar para o diretório do projeto web
cd clinica-web-app

# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Instalação das Dependências

```bash
# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração do Banco de Dados

```bash
# Inicializar banco de dados
python -c "from backend.app import app, db; app.app_context().push(); db.create_all()"
```

### 4. Executar a Aplicação

```bash
# Modo desenvolvimento
python backend/app.py

# Ou usando Flask CLI
export FLASK_APP=backend/app.py
export FLASK_ENV=development
flask run
```

### 5. Acessar a Aplicação

Abra seu navegador e acesse: `http://localhost:5000`

## 🎨 Funcionalidades

### 🔐 Sistema de Autenticação
- Login seguro com validação
- Controle de sessões
- Diferentes níveis de acesso
- Logout automático por inatividade

### 📊 Dashboard Interativo
- Estatísticas em tempo real
- Gráficos e métricas
- Ações rápidas
- Status do sistema Ordinix-123

### 👤 Gestão de Pacientes
- Cadastro completo com validação
- Busca avançada e filtros
- Histórico médico
- Análise de prioridade (Ordinix-123)

### 🔍 Sistema de Busca
- Busca em tempo real
- Múltiplos critérios
- Resultados paginados
- Exportação de dados

### 🤖 Sistema Ordinix-123
- Análise inteligente de prioridade
- Classificação automática
- Alertas e notificações
- Relatórios de eficiência

### 📱 Interface Responsiva
- Design mobile-first
- Compatibilidade cross-browser
- Acessibilidade (WCAG 2.1)
- Modo escuro (futuro)

## 🔧 Configuração Avançada

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Configurações da aplicação
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=sqlite:///clinica.db

# Configurações do Redis (opcional)
REDIS_URL=redis://localhost:6379/0

# Configurações de email (opcional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_app

# Configurações do Ordinix-123
ORDINIX_API_KEY=sua_chave_api
ORDINIX_ENDPOINT=https://api.ordinix.com/v1
```

### Configuração para Produção

```bash
# Instalar servidor de produção
pip install gunicorn

# Executar com Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app

# Com WebSockets
gunicorn -w 1 -k eventlet -b 0.0.0.0:5000 backend.app:app
```

### Configuração do Nginx (Produção)

```nginx
server {
    listen 80;
    server_name seu_dominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /socket.io/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=backend

# Executar testes específicos
pytest tests/test_api.py
```

## 📈 Performance e Monitoramento

### Métricas Disponíveis
- Tempo de resposta das APIs
- Uso de memória e CPU
- Conexões ativas
- Erros e exceções

### Endpoints de Monitoramento
- `/health` - Status da aplicação
- `/metrics` - Métricas Prometheus
- `/api/stats` - Estatísticas do sistema

## 🔒 Segurança

### Medidas Implementadas
- Proteção CSRF em formulários
- Sanitização de inputs
- Rate limiting em APIs
- Headers de segurança
- Validação de dados
- Logs de auditoria

### Boas Práticas
- Senhas hasheadas com bcrypt
- Tokens JWT para APIs
- Validação server-side
- Escape de HTML
- Proteção contra SQL injection

## 🚀 Deploy

### Heroku
```bash
# Criar Procfile
echo "web: gunicorn -w 1 -k eventlet backend.app:app" > Procfile

# Deploy
git add .
git commit -m "Deploy inicial"
heroku create sua-app
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "1", "-k", "eventlet", "-b", "0.0.0.0:5000", "backend.app:app"]
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0 (2024-01-XX)
- ✨ Versão inicial da aplicação web
- 🎨 Interface moderna e responsiva
- 🔐 Sistema de autenticação completo
- 👤 Gestão completa de pacientes
- 🤖 Integração com sistema Ordinix-123
- 📊 Dashboard interativo
- 🔍 Sistema de busca avançada

## 📞 Suporte

Para suporte técnico ou dúvidas:

- 📧 Email: suporte@clinicavidamais.com
- 📱 WhatsApp: (11) 99999-9999
- 🌐 Site: https://clinicavidamais.com
- 📚 Documentação: https://docs.clinicavidamais.com

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- Equipe de desenvolvimento da CLÍNICA VIDA+
- Comunidade Flask e Python
- Contribuidores do projeto
- Beta testers e usuários

---

**CLÍNICA VIDA+** - Transformando o cuidado com tecnologia 🏥✨