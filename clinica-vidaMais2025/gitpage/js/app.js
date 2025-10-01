// ===== SISTEMA CLÍNICA VIDA+ COM ORDINIX-123 - JAVASCRIPT PRINCIPAL =====
// Inventor: Adevilson de Lima - Estudante ADS Anhanguera
// Sistema revolucionário de triagem hospitalar com interface moderna

class SistemaVidaPlus {
    constructor() {
        this.usuarioLogado = null;
        this.pacientes = [];
        this.filaOrdinix = [];
        this.currentPage = 'dashboard';
        this.sidebarOpen = true;
        
        this.init();
    }

    init() {
        this.loadStoredData();
        this.setupEventListeners();
        this.updateClock();
        this.checkLoginStatus();
        this.preencheCamposLogin();
        
        // Atualizar estatísticas a cada 30 segundos
        setInterval(() => {
            this.updateDashboard();
        }, 30000);
    }

    // ===== GERENCIAMENTO DE DADOS =====
    loadStoredData() {
        const storedPacientes = localStorage.getItem('clinica_pacientes');
        const storedUser = localStorage.getItem('clinica_usuario');
        
        if (storedPacientes) {
            this.pacientes = JSON.parse(storedPacientes);
        }
        
        if (storedUser) {
            this.usuarioLogado = JSON.parse(storedUser);
        }
    }

    saveData() {
        localStorage.setItem('clinica_pacientes', JSON.stringify(this.pacientes));
        if (this.usuarioLogado) {
            localStorage.setItem('clinica_usuario', JSON.stringify(this.usuarioLogado));
        }
    }

    // ===== SISTEMA DE LOGIN =====
    setupEventListeners() {
        // Login
        const loginForm = document.getElementById('login-form');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => this.handleLogin(e));
        }

        const togglePassword = document.getElementById('toggle-password');
        if (togglePassword) {
            togglePassword.addEventListener('click', () => this.togglePasswordVisibility());
        }

        const limparCampos = document.getElementById('limpar-campos');
        if (limparCampos) {
            limparCampos.addEventListener('click', () => this.clearLoginFields());
        }

        // Sistema principal
        const menuToggle = document.getElementById('menu-toggle');
        if (menuToggle) {
            menuToggle.addEventListener('click', () => this.toggleSidebar());
        }

        const logoutBtn = document.getElementById('logout-btn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => this.logout());
        }

        // Menu de navegação
        const menuItems = document.querySelectorAll('.menu-item');
        menuItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                const page = item.getAttribute('data-page');
                this.navigateTo(page);
            });
        });

        // Formulário de cadastro
        const cadastroForm = document.getElementById('cadastro-form');
        if (cadastroForm) {
            cadastroForm.addEventListener('submit', (e) => this.handleCadastro(e));
        }

        const limparForm = document.getElementById('limpar-form');
        if (limparForm) {
            limparForm.addEventListener('click', () => this.clearCadastroForm());
        }

        // Busca
        const searchBtn = document.getElementById('search-btn');
        if (searchBtn) {
            searchBtn.addEventListener('click', () => this.performSearch());
        }

        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.performSearch();
                }
            });
        }

        // Relatórios
        const gerarRelatorio = document.getElementById('gerar-relatorio');
        if (gerarRelatorio) {
            gerarRelatorio.addEventListener('click', () => this.generateReport());
        }

        const exportarDados = document.getElementById('exportar-dados');
        if (exportarDados) {
            exportarDados.addEventListener('click', () => this.exportData());
        }

        // Configurações
        const limparDados = document.getElementById('limpar-dados');
        if (limparDados) {
            limparDados.addEventListener('click', () => this.clearAllData());
        }

        const backupDados = document.getElementById('backup-dados');
        if (backupDados) {
            backupDados.addEventListener('click', () => this.backupData());
        }

        // Modal
        const modal = document.getElementById('patient-modal');
        const closeModal = document.querySelector('.close');
        if (closeModal) {
            closeModal.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }

        if (modal) {
            window.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.style.display = 'none';
                }
            });
        }

        // Máscara para CPF
        const cpfInput = document.getElementById('cpf');
        if (cpfInput) {
            cpfInput.addEventListener('input', (e) => this.formatCPF(e));
        }

        // Máscara para telefone
        const telefoneInput = document.getElementById('telefone');
        if (telefoneInput) {
            telefoneInput.addEventListener('input', (e) => this.formatTelefone(e));
        }

        // Seletor de prioridade
        const autoPriorityCheckbox = document.getElementById('auto-priority');
        if (autoPriorityCheckbox) {
            autoPriorityCheckbox.addEventListener('change', (e) => {
                this.togglePriorityMode(e.target.checked);
            });
        }

        // Atualização automática da prioridade
        const formFields = ['sintomas', 'temperatura', 'idade'];
        formFields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (field) {
                field.addEventListener('input', () => this.updateAutoPriority());
            }
        });

        // Gráficos
        const gerarGraficosBtn = document.getElementById('gerar-graficos');
        if (gerarGraficosBtn) {
            gerarGraficosBtn.addEventListener('click', () => this.generateCharts());
        }

        // Funcionalidades de impressão
        const printButtons = [
            'imprimir-relatorio-completo',
            'imprimir-estatisticas', 
            'imprimir-lista-pacientes',
            'imprimir-fila-ordinix',
            'imprimir-dashboard',
            'imprimir-resumo-diario'
        ];

        printButtons.forEach(buttonId => {
            const button = document.getElementById(buttonId);
            if (button) {
                button.addEventListener('click', () => this.handlePrint(buttonId));
            }
        });
    }

    checkLoginStatus() {
        if (this.usuarioLogado) {
            this.showMainSystem();
        } else {
            this.showLoginScreen();
        }
    }

    preencheCamposLogin() {
        // Aguardar um pouco para garantir que os elementos estejam carregados
        setTimeout(() => {
            const usuarioInput = document.getElementById('usuario');
            const senhaInput = document.getElementById('senha');
            const lembrarCheckbox = document.getElementById('lembrar');
            
            if (usuarioInput && senhaInput && lembrarCheckbox) {
                usuarioInput.value = 'Adevilson de lima';
                senhaInput.value = 'Anhanguera2025';
                lembrarCheckbox.checked = true;
            }
        }, 100);
    }

    handleLogin(e) {
        e.preventDefault();
        
        const usuario = document.getElementById('usuario').value.trim();
        const senha = document.getElementById('senha').value;
        const lembrar = document.getElementById('lembrar').checked;

        // Validação simples (em produção, seria validado no servidor)
        if (usuario === 'Adevilson de lima' && senha === 'Anhanguera2025') {
            this.usuarioLogado = {
                nome: usuario,
                tipo: 'Administrador',
                loginTime: new Date().toISOString()
            };

            if (lembrar) {
                localStorage.setItem('clinica_lembrar', 'true');
                localStorage.setItem('clinica_usuario_nome', usuario);
            } else {
                localStorage.removeItem('clinica_lembrar');
                localStorage.removeItem('clinica_usuario_nome');
            }

            this.saveData();
            this.showMainSystem();
            this.showAlert('Login realizado com sucesso!', 'success');
        } else {
            this.showAlert('Usuário ou senha inválidos!', 'danger');
        }
    }

    togglePasswordVisibility() {
        const senhaInput = document.getElementById('senha');
        const toggleIcon = document.querySelector('#toggle-password i');
        
        if (senhaInput.type === 'password') {
            senhaInput.type = 'text';
            toggleIcon.className = 'fas fa-eye-slash';
        } else {
            senhaInput.type = 'password';
            toggleIcon.className = 'fas fa-eye';
        }
    }

    clearLoginFields() {
        document.getElementById('usuario').value = 'Adevilson de lima';
        document.getElementById('senha').value = 'Anhanguera2025';
        document.getElementById('lembrar').checked = true;
    }

    logout() {
        if (confirm('Deseja realmente sair do sistema?')) {
            this.usuarioLogado = null;
            localStorage.removeItem('clinica_usuario');
            this.showLoginScreen();
            this.showAlert('Logout realizado com sucesso!', 'success');
        }
    }

    showLoginScreen() {
        document.getElementById('login-screen').style.display = 'flex';
        document.getElementById('main-system').style.display = 'none';
        
        // Preencher campos automaticamente com as credenciais do usuário
        document.getElementById('usuario').value = 'Adevilson de lima';
        document.getElementById('senha').value = 'Anhanguera2025';
        document.getElementById('lembrar').checked = true;
        
        // Carregar credenciais salvas se "lembrar" estiver ativo (mantido para compatibilidade)
        const lembrar = localStorage.getItem('clinica_lembrar');
        const usuarioSalvo = localStorage.getItem('clinica_usuario_nome');
        
        if (lembrar === 'true' && usuarioSalvo) {
            document.getElementById('usuario').value = usuarioSalvo;
            document.getElementById('lembrar').checked = true;
        }
    }

    showMainSystem() {
        document.getElementById('login-screen').style.display = 'none';
        document.getElementById('main-system').style.display = 'block';
        
        // Atualizar informações do usuário
        document.getElementById('user-info').textContent = 
            `${this.usuarioLogado.tipo}: ${this.usuarioLogado.nome}`;
        
        this.navigateTo('dashboard');
        this.updateDashboard();
        
        // Inicializar modo de prioridade automático
        setTimeout(() => {
            const autoPriorityCheckbox = document.getElementById('auto-priority');
            if (autoPriorityCheckbox) {
                this.togglePriorityMode(autoPriorityCheckbox.checked);
            }
        }, 100);
    }

    // ===== NAVEGAÇÃO =====
    navigateTo(page) {
        // Remover classe active de todos os itens do menu
        document.querySelectorAll('.menu-item').forEach(item => {
            item.classList.remove('active');
        });

        // Adicionar classe active ao item selecionado
        const activeItem = document.querySelector(`[data-page="${page}"]`);
        if (activeItem) {
            activeItem.classList.add('active');
        }

        // Esconder todas as páginas
        document.querySelectorAll('.page').forEach(p => {
            p.classList.remove('active');
        });

        // Mostrar página selecionada
        const targetPage = document.getElementById(`${page}-page`);
        if (targetPage) {
            targetPage.classList.add('active');
        }

        this.currentPage = page;

        // Executar ações específicas da página
        switch (page) {
            case 'dashboard':
                this.updateDashboard();
                break;
            case 'lista-pacientes':
                this.updatePatientsList();
                break;
            case 'busca':
                this.clearSearchResults();
                break;
            case 'ordinix':
                this.updateOrdinixPanel();
                break;
        }
    }

    toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        this.sidebarOpen = !this.sidebarOpen;
        
        if (window.innerWidth <= 768) {
            sidebar.classList.toggle('open');
        } else {
            sidebar.classList.toggle('collapsed');
        }
    }

    // ===== DASHBOARD =====
    updateDashboard() {
        const stats = this.calculateStats();
        
        document.getElementById('total-pacientes').textContent = stats.total;
        document.getElementById('nivel-1').textContent = stats.nivel1;
        document.getElementById('nivel-2').textContent = stats.nivel2;
        document.getElementById('nivel-3').textContent = stats.nivel3;

        this.updateFilaOrdinix();
    }

    calculateStats() {
        const total = this.pacientes.length;
        const nivel1 = this.pacientes.filter(p => p.prioridade === 1).length;
        const nivel2 = this.pacientes.filter(p => p.prioridade === 2).length;
        const nivel3 = this.pacientes.filter(p => p.prioridade === 3).length;

        return { total, nivel1, nivel2, nivel3 };
    }

    updateFilaOrdinix() {
        const filaContainer = document.getElementById('fila-container');
        const pacientesOrdenados = this.pacientes
            .filter(p => p.prioridade >= 2) // Apenas níveis 2 e 3 na fila
            .sort((a, b) => b.prioridade - a.prioridade); // Prioridade maior primeiro

        if (pacientesOrdenados.length === 0) {
            filaContainer.innerHTML = '<p class="empty-message">Nenhum paciente na fila</p>';
            return;
        }

        filaContainer.innerHTML = pacientesOrdenados.map((paciente, index) => `
            <div class="paciente-fila nivel-${paciente.prioridade}">
                <div class="paciente-info">
                    <h4>${paciente.nome}</h4>
                    <p>CPF: ${paciente.cpf} | Idade: ${paciente.idade} anos</p>
                    <p>Sintomas: ${paciente.sintomas}</p>
                </div>
                <div class="prioridade-badge nivel-${paciente.prioridade}">
                    ${this.getPrioridadeText(paciente.prioridade)}
                </div>
            </div>
        `).join('');
    }

    getPrioridadeText(nivel) {
        switch (nivel) {
            case 1: return 'VERDE';
            case 2: return 'AMARELO';
            case 3: return 'VERMELHO';
            default: return 'NORMAL';
        }
    }

    // ===== CADASTRO =====
    handleCadastro(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const autoPriority = document.getElementById('auto-priority').checked;
        const manualPriority = formData.get('prioridade');
        
        const paciente = {
            id: Date.now(),
            nome: formData.get('nome'),
            cpf: formData.get('cpf'),
            idade: parseInt(formData.get('idade')),
            telefone: formData.get('telefone'),
            sintomas: formData.get('sintomas'),
            pressao: formData.get('pressao'),
            temperatura: parseFloat(formData.get('temperatura')),
            dataHora: new Date().toISOString(),
            prioridade: autoPriority ? this.calculatePriority(formData) : parseInt(manualPriority) || 1
        };

        // Validações
        if (!this.validateCPF(paciente.cpf)) {
            this.showAlert('CPF inválido!', 'danger');
            return;
        }

        if (this.pacientes.find(p => p.cpf === paciente.cpf)) {
            this.showAlert('Paciente com este CPF já cadastrado!', 'warning');
            return;
        }

        this.pacientes.push(paciente);
        this.saveData();
        
        this.showAlert('Paciente cadastrado com sucesso!', 'success');
        this.clearCadastroForm();
        
        // Mostrar alerta se for emergência
        if (paciente.prioridade === 3) {
            this.showEmergencyAlert(paciente);
        }
    }

    calculatePriority(formData) {
        const temperatura = parseFloat(formData.get('temperatura')) || 36.5;
        const sintomas = formData.get('sintomas').toLowerCase();
        const idade = parseInt(formData.get('idade')) || 0;
        const pressao = formData.get('pressao') || '';
        
        let score = 0;
        let emergencyDetected = false;

        // === SINTOMAS DE EMERGÊNCIA IMEDIATA (Nível 3 direto) ===
        const emergenciaImediata = [
            'parada cardíaca', 'parada respiratória', 'infarto', 'avc', 'derrame',
            'convulsão', 'coma', 'inconsciência', 'desmaio', 'perda de consciência',
            'hemorragia grave', 'sangramento intenso', 'trauma grave', 'acidente grave',
            'queimadura grave', 'intoxicação', 'overdose', 'tentativa de suicídio',
            'dificuldade respiratória severa', 'não consegue respirar', 'sufocamento',
            'dor no peito intensa', 'dor torácica', 'angina', 'pressão no peito'
        ];

        if (emergenciaImediata.some(s => sintomas.includes(s))) {
            emergencyDetected = true;
            score += 10; // Score muito alto para garantir nível 3
        }

        // === SINTOMAS CRÍTICOS (Score alto) ===
        const sintomasCriticos = [
            'dor no peito', 'falta de ar', 'falta de fôlego', 'dispneia',
            'dor abdominal intensa', 'dor de cabeça severa', 'enxaqueca severa',
            'vômito com sangue', 'sangue no vômito', 'fezes com sangue',
            'dor nas costas intensa', 'paralisia', 'dormência', 'formigamento intenso',
            'visão turva', 'perda de visão', 'zumbido no ouvido', 'tontura severa',
            'palpitação', 'batimento irregular', 'taquicardia'
        ];

        const criticosEncontrados = sintomasCriticos.filter(s => sintomas.includes(s));
        if (criticosEncontrados.length > 0) {
            score += criticosEncontrados.length * 2; // Múltiplos sintomas críticos
        }

        // === SINTOMAS MODERADOS ===
        const sintomasModeratos = [
            'febre alta', 'febre', 'vômito', 'náusea', 'diarreia',
            'dor de cabeça', 'cefaleia', 'tontura', 'mal estar',
            'dor muscular', 'dor nas articulações', 'cansaço extremo',
            'tosse persistente', 'garganta inflamada', 'dor de garganta'
        ];

        const moderadosEncontrados = sintomasModeratos.filter(s => sintomas.includes(s));
        if (moderadosEncontrados.length > 0) {
            score += moderadosEncontrados.length; // 1 ponto por sintoma moderado
        }

        // === ANÁLISE DE TEMPERATURA ===
        if (temperatura >= 40) {
            score += 4; // Febre muito alta
            emergencyDetected = true;
        } else if (temperatura >= 39) {
            score += 3; // Febre alta
        } else if (temperatura >= 38.5) {
            score += 2; // Febre moderada
        } else if (temperatura <= 35) {
            score += 3; // Hipotermia
        } else if (temperatura <= 35.5) {
            score += 2; // Temperatura baixa
        }

        // === ANÁLISE DE PRESSÃO ARTERIAL ===
        if (pressao) {
            const pressaoLimpa = pressao.replace(/[^\d\/]/g, '');
            const [sistolica, diastolica] = pressaoLimpa.split('/').map(p => parseInt(p));
            
            if (sistolica && diastolica) {
                // Hipertensão severa
                if (sistolica >= 180 || diastolica >= 110) {
                    score += 4;
                    emergencyDetected = true;
                }
                // Hipertensão moderada
                else if (sistolica >= 160 || diastolica >= 100) {
                    score += 2;
                }
                // Hipotensão
                else if (sistolica <= 90 || diastolica <= 60) {
                    score += 2;
                }
            }
        }

        // === FATORES DE IDADE ===
        if (idade >= 80) {
            score += 2; // Idosos muito vulneráveis
        } else if (idade >= 65) {
            score += 1; // Idosos
        } else if (idade <= 1) {
            score += 3; // Bebês muito vulneráveis
        } else if (idade <= 5) {
            score += 2; // Crianças pequenas
        }

        // === ANÁLISE DE MÚLTIPLOS SINTOMAS ===
        const totalSintomas = sintomas.split(/[,;.]/).filter(s => s.trim().length > 3).length;
        if (totalSintomas >= 5) {
            score += 2; // Múltiplos sintomas podem indicar gravidade
        }

        // === DETERMINAÇÃO FINAL DA PRIORIDADE ===
        if (emergencyDetected || score >= 8) {
            return 3; // Vermelho - Emergência
        } else if (score >= 4) {
            return 2; // Amarelo - Urgente
        } else if (score >= 1) {
            return 2; // Amarelo - Urgente (qualquer sintoma merece atenção)
        }
        
        return 1; // Verde - Normal
    }

    showEmergencyAlert(paciente) {
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert danger';
        alertDiv.innerHTML = `
            <strong>🚨 EMERGÊNCIA DETECTADA!</strong><br>
            Paciente: ${paciente.nome}<br>
            Prioridade: VERMELHA - Atendimento imediato necessário!
        `;
        
        document.body.appendChild(alertDiv);
        
        setTimeout(() => {
            alertDiv.remove();
        }, 10000);
    }

    clearCadastroForm() {
        document.getElementById('cadastro-form').reset();
        // Reativar modo automático após limpar
        const autoPriorityCheckbox = document.getElementById('auto-priority');
        if (autoPriorityCheckbox) {
            autoPriorityCheckbox.checked = true;
            this.togglePriorityMode(true);
        }
    }

    // ===== SELETOR DE PRIORIDADE =====
    togglePriorityMode(isAuto) {
        const priorityOptions = document.querySelectorAll('input[name="prioridade"]');
        const prioritySelector = document.querySelector('.priority-selector');
        const existingIndicator = document.querySelector('.priority-indicator');
        
        if (isAuto) {
            // Modo automático: desabilitar seleção manual
            priorityOptions.forEach(option => {
                option.disabled = true;
                option.checked = false;
            });
            prioritySelector.style.opacity = '0.5';
            prioritySelector.style.pointerEvents = 'none';
            
            // Calcular prioridade automaticamente
            this.updateAutoPriority();
        } else {
            // Modo manual: habilitar seleção
            priorityOptions.forEach(option => {
                option.disabled = false;
                option.checked = false; // Limpar seleções anteriores
            });
            prioritySelector.style.opacity = '1';
            prioritySelector.style.pointerEvents = 'auto';
            
            // Remover indicador automático
            if (existingIndicator) {
                existingIndicator.remove();
            }
            
            // Selecionar nível 1 por padrão
            const nivel1 = document.getElementById('prioridade-1');
            if (nivel1) nivel1.checked = true;
            
            // Mostrar indicador de modo manual
            this.showManualModeIndicator();
        }
    }

    updateAutoPriority() {
        const autoPriorityCheckbox = document.getElementById('auto-priority');
        if (!autoPriorityCheckbox || !autoPriorityCheckbox.checked) return;

        // Criar FormData simulado para calcular prioridade
        const sintomas = document.getElementById('sintomas')?.value || '';
        const temperatura = document.getElementById('temperatura')?.value || '';
        const idade = document.getElementById('idade')?.value || '';

        const mockFormData = new Map();
        mockFormData.set('sintomas', sintomas);
        mockFormData.set('temperatura', temperatura);
        mockFormData.set('idade', idade);

        const prioridade = this.calculatePriority(mockFormData);
        
        // Atualizar seleção visual
        const priorityOptions = document.querySelectorAll('input[name="prioridade"]');
        priorityOptions.forEach(option => {
            option.checked = (parseInt(option.value) === prioridade);
        });

        // Mostrar indicador visual da prioridade calculada
        this.showPriorityIndicator(prioridade);
    }

    showPriorityIndicator(prioridade) {
        // Remover indicador anterior
        const existingIndicator = document.querySelector('.priority-indicator');
        if (existingIndicator) existingIndicator.remove();

        // Criar novo indicador
        const indicator = document.createElement('div');
        indicator.className = 'priority-indicator';
        indicator.innerHTML = `
            <i class="fas fa-robot"></i> 
            Prioridade calculada: <strong>${this.getPrioridadeText(prioridade)}</strong>
        `;
        indicator.style.cssText = `
            background: rgba(0, 102, 204, 0.1);
            border: 1px solid rgba(0, 102, 204, 0.3);
            border-radius: 8px;
            padding: 8px 12px;
            margin-top: 10px;
            font-size: 12px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        `;

        const prioritySelector = document.querySelector('.priority-selector');
        if (prioritySelector) {
            prioritySelector.parentNode.appendChild(indicator);
        }
    }

    showManualModeIndicator() {
        // Remover indicador anterior
        const existingIndicator = document.querySelector('.priority-indicator');
        if (existingIndicator) existingIndicator.remove();

        // Criar indicador de modo manual
        const indicator = document.createElement('div');
        indicator.className = 'priority-indicator';
        indicator.innerHTML = `
            <i class="fas fa-hand-pointer"></i> 
            Modo manual ativo: <strong>Selecione a prioridade desejada</strong>
        `;
        indicator.style.cssText = `
            background: rgba(255, 193, 7, 0.1);
            border: 1px solid rgba(255, 193, 7, 0.3);
            border-radius: 8px;
            padding: 8px 12px;
            margin-top: 10px;
            font-size: 12px;
            color: #856404;
            display: flex;
            align-items: center;
            gap: 8px;
        `;

        const prioritySelector = document.querySelector('.priority-selector');
        if (prioritySelector) {
            prioritySelector.parentNode.appendChild(indicator);
        }
    }

    // ===== BUSCA =====
    performSearch() {
        const query = document.getElementById('search-input').value.trim().toLowerCase();
        const resultsContainer = document.getElementById('search-results');
        
        if (!query) {
            resultsContainer.innerHTML = '<p class="empty-message">Digite algo para buscar pacientes</p>';
            return;
        }

        const results = this.pacientes.filter(paciente => 
            paciente.nome.toLowerCase().includes(query) ||
            paciente.cpf.includes(query) ||
            paciente.telefone.includes(query)
        );

        if (results.length === 0) {
            resultsContainer.innerHTML = '<p class="empty-message">Nenhum paciente encontrado</p>';
            return;
        }

        resultsContainer.innerHTML = results.map(paciente => this.createPatientCard(paciente)).join('');
    }

    clearSearchResults() {
        document.getElementById('search-input').value = '';
        document.getElementById('search-results').innerHTML = 
            '<p class="empty-message">Digite algo para buscar pacientes</p>';
    }

    // ===== LISTA DE PACIENTES =====
    updatePatientsList() {
        const listContainer = document.getElementById('patients-list');
        
        if (this.pacientes.length === 0) {
            listContainer.innerHTML = '<p class="empty-message">Nenhum paciente cadastrado</p>';
            return;
        }

        const sortedPatients = [...this.pacientes].sort((a, b) => 
            new Date(b.dataHora) - new Date(a.dataHora)
        );

        listContainer.innerHTML = sortedPatients.map(paciente => 
            this.createPatientCard(paciente)
        ).join('');
    }

    createPatientCard(paciente) {
        const dataFormatada = new Date(paciente.dataHora).toLocaleString('pt-BR');
        
        return `
            <div class="patient-card">
                <h4>${paciente.nome}</h4>
                <p><strong>CPF:</strong> ${paciente.cpf}</p>
                <p><strong>Idade:</strong> ${paciente.idade} anos</p>
                <p><strong>Telefone:</strong> ${paciente.telefone}</p>
                <p><strong>Sintomas:</strong> ${paciente.sintomas}</p>
                <p><strong>Prioridade:</strong> 
                    <span class="prioridade-badge nivel-${paciente.prioridade}">
                        ${this.getPrioridadeText(paciente.prioridade)}
                    </span>
                </p>
                <p><strong>Data/Hora:</strong> ${dataFormatada}</p>
                <div class="patient-actions">
                    <button class="btn-primary" onclick="sistema.showPatientDetails(${paciente.id})">
                        <i class="fas fa-eye"></i> Ver Detalhes
                    </button>
                    <button class="btn-secondary" onclick="sistema.editPatient(${paciente.id})">
                        <i class="fas fa-edit"></i> Editar
                    </button>
                    <button class="btn-danger" onclick="sistema.deletePatient(${paciente.id})">
                        <i class="fas fa-trash"></i> Excluir
                    </button>
                </div>
            </div>
        `;
    }

    // ===== MODAL DE DETALHES =====
    showPatientDetails(id) {
        const paciente = this.pacientes.find(p => p.id === id);
        if (!paciente) return;

        const modal = document.getElementById('patient-modal');
        const modalBody = document.getElementById('modal-body');
        
        modalBody.innerHTML = `
            <h3>Detalhes do Paciente</h3>
            <div class="patient-details">
                <p><strong>Nome:</strong> ${paciente.nome}</p>
                <p><strong>CPF:</strong> ${paciente.cpf}</p>
                <p><strong>Idade:</strong> ${paciente.idade} anos</p>
                <p><strong>Telefone:</strong> ${paciente.telefone}</p>
                <p><strong>Sintomas:</strong> ${paciente.sintomas}</p>
                <p><strong>Pressão Arterial:</strong> ${paciente.pressao || 'Não informado'}</p>
                <p><strong>Temperatura:</strong> ${paciente.temperatura || 'Não informado'}°C</p>
                <p><strong>Prioridade:</strong> 
                    <span class="prioridade-badge nivel-${paciente.prioridade}">
                        ${this.getPrioridadeText(paciente.prioridade)}
                    </span>
                </p>
                <p><strong>Data/Hora do Cadastro:</strong> ${new Date(paciente.dataHora).toLocaleString('pt-BR')}</p>
            </div>
        `;
        
        modal.style.display = 'block';
    }

    editPatient(id) {
        // Implementar edição de paciente
        this.showAlert('Funcionalidade de edição em desenvolvimento', 'info');
    }

    deletePatient(id) {
        if (confirm('Deseja realmente excluir este paciente?')) {
            this.pacientes = this.pacientes.filter(p => p.id !== id);
            this.saveData();
            this.updatePatientsList();
            this.updateDashboard();
            this.showAlert('Paciente excluído com sucesso!', 'success');
        }
    }

    // ===== PAINEL ORDINIX =====
    updateOrdinixPanel() {
        const ordinixQueue = document.getElementById('ordinix-queue');
        const emergencyPatients = this.pacientes.filter(p => p.prioridade === 3);
        
        if (emergencyPatients.length === 0) {
            ordinixQueue.innerHTML = '<p class="empty-message">Nenhum paciente na fila de emergência</p>';
            return;
        }

        ordinixQueue.innerHTML = emergencyPatients.map(paciente => `
            <div class="patient-card">
                <h4>🚨 ${paciente.nome}</h4>
                <p><strong>Sintomas:</strong> ${paciente.sintomas}</p>
                <p><strong>Temperatura:</strong> ${paciente.temperatura}°C</p>
                <p><strong>Cadastrado:</strong> ${new Date(paciente.dataHora).toLocaleString('pt-BR')}</p>
                <div class="patient-actions">
                    <button class="btn-danger">ATENDER IMEDIATAMENTE</button>
                </div>
            </div>
        `).join('');
    }

    // ===== RELATÓRIOS =====
    generateReport() {
        const reportContent = document.getElementById('report-content');
        const stats = this.calculateStats();
        
        const report = `
            <h3>Relatório Geral do Sistema</h3>
            <div class="report-stats">
                <h4>Estatísticas Gerais</h4>
                <p><strong>Total de Pacientes:</strong> ${stats.total}</p>
                <p><strong>Nível Verde (Normal):</strong> ${stats.nivel1}</p>
                <p><strong>Nível Amarelo (Urgente):</strong> ${stats.nivel2}</p>
                <p><strong>Nível Vermelho (Emergência):</strong> ${stats.nivel3}</p>
                
                <h4>Distribuição por Idade</h4>
                ${this.getAgeDistribution()}
                
                <h4>Sintomas Mais Comuns</h4>
                ${this.getCommonSymptoms()}
                
                <h4>Relatório Gerado em:</h4>
                <p>${new Date().toLocaleString('pt-BR')}</p>
            </div>
        `;
        
        reportContent.innerHTML = report;
    }

    getAgeDistribution() {
        const ageGroups = {
            '0-18': 0,
            '19-35': 0,
            '36-60': 0,
            '60+': 0
        };

        this.pacientes.forEach(p => {
            if (p.idade <= 18) ageGroups['0-18']++;
            else if (p.idade <= 35) ageGroups['19-35']++;
            else if (p.idade <= 60) ageGroups['36-60']++;
            else ageGroups['60+']++;
        });

        return Object.entries(ageGroups)
            .map(([group, count]) => `<p><strong>${group} anos:</strong> ${count}</p>`)
            .join('');
    }

    getCommonSymptoms() {
        const symptoms = {};
        this.pacientes.forEach(p => {
            const words = p.sintomas.toLowerCase().split(/\s+/);
            words.forEach(word => {
                if (word.length > 3) {
                    symptoms[word] = (symptoms[word] || 0) + 1;
                }
            });
        });

        return Object.entries(symptoms)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 5)
            .map(([symptom, count]) => `<p><strong>${symptom}:</strong> ${count} ocorrências</p>`)
            .join('');
    }

    exportData() {
        const data = {
            pacientes: this.pacientes,
            exportDate: new Date().toISOString(),
            totalPacientes: this.pacientes.length
        };

        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `clinica_dados_${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);

        this.showAlert('Dados exportados com sucesso!', 'success');
    }

    // ===== CONFIGURAÇÕES =====
    clearAllData() {
        if (confirm('ATENÇÃO: Esta ação irá apagar todos os dados do sistema. Deseja continuar?')) {
            if (confirm('Tem certeza? Esta ação não pode ser desfeita!')) {
                this.pacientes = [];
                localStorage.clear();
                this.updateDashboard();
                this.updatePatientsList();
                this.showAlert('Todos os dados foram apagados!', 'warning');
            }
        }
    }

    backupData() {
        this.exportData();
        this.showAlert('Backup realizado com sucesso!', 'success');
    }

    // ===== UTILITÁRIOS =====
    formatCPF(e) {
        let value = e.target.value.replace(/\D/g, '');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        e.target.value = value;
    }

    formatTelefone(e) {
        let value = e.target.value.replace(/\D/g, '');
        value = value.replace(/(\d{2})(\d)/, '($1) $2');
        value = value.replace(/(\d{5})(\d)/, '$1-$2');
        e.target.value = value;
    }

    validateCPF(cpf) {
        cpf = cpf.replace(/\D/g, '');
        if (cpf.length !== 11) return false;
        
        // Verificar se todos os dígitos são iguais
        if (/^(\d)\1{10}$/.test(cpf)) return false;
        
        // Validar dígitos verificadores
        let sum = 0;
        for (let i = 0; i < 9; i++) {
            sum += parseInt(cpf.charAt(i)) * (10 - i);
        }
        let digit1 = 11 - (sum % 11);
        if (digit1 > 9) digit1 = 0;
        
        sum = 0;
        for (let i = 0; i < 10; i++) {
            sum += parseInt(cpf.charAt(i)) * (11 - i);
        }
        let digit2 = 11 - (sum % 11);
        if (digit2 > 9) digit2 = 0;
        
        return digit1 === parseInt(cpf.charAt(9)) && digit2 === parseInt(cpf.charAt(10));
    }

    updateClock() {
        const updateTime = () => {
            const now = new Date();
            const timeString = now.toLocaleString('pt-BR');
            const clockElement = document.getElementById('current-time');
            if (clockElement) {
                clockElement.textContent = timeString;
            }
        };

        updateTime();
        setInterval(updateTime, 1000);
    }

    showAlert(message, type = 'info') {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.innerHTML = `
            <span>${message}</span>
            <button onclick="this.parentElement.remove()" class="alert-close">&times;</button>
        `;
        
        alertDiv.style.cssText = `
            position: fixed; top: 20px; right: 20px; z-index: 10000;
            padding: 15px 20px; border-radius: 5px; color: white;
            background: ${type === 'success' ? '#28a745' : type === 'error' ? '#dc3545' : '#007bff'};
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        `;
        
        document.body.appendChild(alertDiv);
        setTimeout(() => alertDiv.remove(), 5000);
    }

    // ===== FUNCIONALIDADES DE GRÁFICOS =====
    generateCharts() {
        const chartsContainer = document.getElementById('charts-container');
        if (chartsContainer) {
            chartsContainer.style.display = 'grid';
        }

        this.createPriorityChart();
        this.createAgeChart();
        this.createSymptomsChart();
        this.createTimeChart();
        
        this.showAlert('Gráficos gerados com sucesso!', 'success');
    }

    createPriorityChart() {
        const ctx = document.getElementById('priorityChart');
        if (!ctx) return;

        const stats = this.calculateStats();
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Prioridade Baixa', 'Prioridade Média', 'Prioridade Alta'],
                datasets: [{
                    label: 'Número de Pacientes',
                    data: [stats.nivel1, stats.nivel2, stats.nivel3],
                    backgroundColor: [
                        'rgba(40, 167, 69, 0.8)',   // Verde
                        'rgba(255, 193, 7, 0.8)',   // Amarelo
                        'rgba(220, 53, 69, 0.8)'    // Vermelho
                    ],
                    borderColor: [
                        'rgba(40, 167, 69, 1)',
                        'rgba(255, 193, 7, 1)',
                        'rgba(220, 53, 69, 1)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    }

    createAgeChart() {
        const ctx = document.getElementById('ageChart');
        if (!ctx) return;

        const ageDistribution = this.getAgeDistribution();
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(ageDistribution),
                datasets: [{
                    label: 'Número de Pacientes',
                    data: Object.values(ageDistribution),
                    backgroundColor: 'rgba(0, 102, 204, 0.8)',
                    borderColor: 'rgba(0, 102, 204, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    }

    createSymptomsChart() {
        const ctx = document.getElementById('symptomsChart');
        if (!ctx) return;

        const symptoms = this.getCommonSymptoms();
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: symptoms.map(s => s.sintoma),
                datasets: [{
                    label: 'Frequência',
                    data: symptoms.map(s => s.count),
                    backgroundColor: 'rgba(255, 99, 132, 0.8)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    },
                    x: {
                        ticks: {
                            maxRotation: 45
                        }
                    }
                }
            }
        });
    }

    createTimeChart() {
        const ctx = document.getElementById('timeChart');
        if (!ctx) return;

        // Simular dados de atendimento por período
        const timeData = {
            'Manhã (6h-12h)': 0,
            'Tarde (12h-18h)': 0,
            'Noite (18h-24h)': 0,
            'Madrugada (0h-6h)': 0
        };

        this.pacientes.forEach(paciente => {
            const hora = new Date(paciente.dataHora).getHours();
            if (hora >= 6 && hora < 12) timeData['Manhã (6h-12h)']++;
            else if (hora >= 12 && hora < 18) timeData['Tarde (12h-18h)']++;
            else if (hora >= 18 && hora < 24) timeData['Noite (18h-24h)']++;
            else timeData['Madrugada (0h-6h)']++;
        });
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(timeData),
                datasets: [{
                    label: 'Atendimentos',
                    data: Object.values(timeData),
                    backgroundColor: 'rgba(75, 192, 192, 0.8)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    }

    // ===== FUNCIONALIDADES DE IMPRESSÃO =====
    handlePrint(buttonId) {
        const printPreview = document.querySelector('.preview-content');
        let content = '';

        switch(buttonId) {
            case 'imprimir-relatorio-completo':
                content = this.generatePrintableReport();
                break;
            case 'imprimir-estatisticas':
                content = this.generatePrintableStats();
                break;
            case 'imprimir-lista-pacientes':
                content = this.generatePrintablePatientList();
                break;
            case 'imprimir-fila-ordinix':
                content = this.generatePrintableOrdinixQueue();
                break;
            case 'imprimir-dashboard':
                content = this.generatePrintableDashboard();
                break;
            case 'imprimir-resumo-diario':
                content = this.generatePrintableDailySummary();
                break;
        }

        if (printPreview) {
            printPreview.innerHTML = content;
        }

        // Adicionar botão de impressão
        const printButton = document.createElement('button');
        printButton.className = 'btn-primary no-print';
        printButton.innerHTML = '<i class="fas fa-print"></i> Imprimir Agora';
        printButton.style.marginTop = '20px';
        printButton.onclick = () => this.printContent();
        
        if (printPreview) {
            printPreview.appendChild(printButton);
        }
    }

    generatePrintableReport() {
        const stats = this.calculateStats();
        const now = new Date().toLocaleString('pt-BR');
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Relatório Completo</h2>
                <p><strong>Data/Hora:</strong> ${now}</p>
                <hr>
                
                <h3>Estatísticas Gerais</h3>
                <ul>
                    <li><strong>Total de Pacientes:</strong> ${stats.total}</li>
                    <li><strong>Prioridade Baixa:</strong> ${stats.nivel1}</li>
                    <li><strong>Prioridade Média:</strong> ${stats.nivel2}</li>
                    <li><strong>Prioridade Alta:</strong> ${stats.nivel3}</li>
                </ul>
                
                <h3>Lista de Pacientes</h3>
                ${this.generatePatientTable()}
                
                <div class="page-break"></div>
                
                <h3>Distribuição por Idade</h3>
                ${this.generateAgeTable()}
                
                <h3>Sintomas Mais Comuns</h3>
                ${this.generateSymptomsTable()}
            </div>
        `;
    }

    generatePrintableStats() {
        const stats = this.calculateStats();
        const now = new Date().toLocaleString('pt-BR');
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Estatísticas</h2>
                <p><strong>Data/Hora:</strong> ${now}</p>
                <hr>
                
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                    <div>
                        <h3>Resumo Geral</h3>
                        <table style="width: 100%; border-collapse: collapse;">
                            <tr><td style="border: 1px solid #ddd; padding: 8px;"><strong>Total de Pacientes</strong></td><td style="border: 1px solid #ddd; padding: 8px;">${stats.total}</td></tr>
                            <tr><td style="border: 1px solid #ddd; padding: 8px;"><strong>Prioridade Baixa</strong></td><td style="border: 1px solid #ddd; padding: 8px;">${stats.nivel1}</td></tr>
                            <tr><td style="border: 1px solid #ddd; padding: 8px;"><strong>Prioridade Média</strong></td><td style="border: 1px solid #ddd; padding: 8px;">${stats.nivel2}</td></tr>
                            <tr><td style="border: 1px solid #ddd; padding: 8px;"><strong>Prioridade Alta</strong></td><td style="border: 1px solid #ddd; padding: 8px;">${stats.nivel3}</td></tr>
                        </table>
                    </div>
                    
                    <div>
                        <h3>Distribuição por Idade</h3>
                        ${this.generateAgeTable()}
                    </div>
                </div>
            </div>
        `;
    }

    generatePrintablePatientList() {
        const now = new Date().toLocaleString('pt-BR');
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Lista de Pacientes</h2>
                <p><strong>Data/Hora:</strong> ${now}</p>
                <p><strong>Total:</strong> ${this.pacientes.length} pacientes</p>
                <hr>
                
                ${this.generatePatientTable()}
            </div>
        `;
    }

    generatePrintableOrdinixQueue() {
        const now = new Date().toLocaleString('pt-BR');
        const filaOrdinix = this.pacientes
            .filter(p => p.prioridade === 3)
            .sort((a, b) => new Date(a.dataHora) - new Date(b.dataHora));
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Fila Ordinix (Prioridade Alta)</h2>
                <p><strong>Data/Hora:</strong> ${now}</p>
                <p><strong>Pacientes na Fila:</strong> ${filaOrdinix.length}</p>
                <hr>
                
                ${filaOrdinix.length > 0 ? this.generatePatientTable(filaOrdinix) : '<p>Nenhum paciente na fila de prioridade alta.</p>'}
            </div>
        `;
    }

    generatePrintableDashboard() {
        const stats = this.calculateStats();
        const now = new Date().toLocaleString('pt-BR');
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Dashboard</h2>
                <p><strong>Data/Hora:</strong> ${now}</p>
                <hr>
                
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px;">
                    <div>
                        <h3>Estatísticas Principais</h3>
                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; text-align: center;">
                                <div style="font-size: 24px; font-weight: bold; color: #007bff;">${stats.total}</div>
                                <div>Total de Pacientes</div>
                            </div>
                            <div style="background: #d4edda; padding: 15px; border-radius: 8px; text-align: center;">
                                <div style="font-size: 24px; font-weight: bold; color: #28a745;">${stats.nivel1}</div>
                                <div>Prioridade Baixa</div>
                            </div>
                            <div style="background: #fff3cd; padding: 15px; border-radius: 8px; text-align: center;">
                                <div style="font-size: 24px; font-weight: bold; color: #ffc107;">${stats.nivel2}</div>
                                <div>Prioridade Média</div>
                            </div>
                            <div style="background: #f8d7da; padding: 15px; border-radius: 8px; text-align: center;">
                                <div style="font-size: 24px; font-weight: bold; color: #dc3545;">${stats.nivel3}</div>
                                <div>Prioridade Alta</div>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <h3>Últimos Pacientes</h3>
                        ${this.generateRecentPatientsTable()}
                    </div>
                </div>
            </div>
        `;
    }

    generatePrintableDailySummary() {
        const stats = this.calculateStats();
        const now = new Date().toLocaleString('pt-BR');
        const today = new Date().toLocaleDateString('pt-BR');
        
        return `
            <div class="print-content">
                <h2>🏥 CLÍNICA VIDA+ - Resumo Diário</h2>
                <p><strong>Data:</strong> ${today}</p>
                <p><strong>Gerado em:</strong> ${now}</p>
                <hr>
                
                <h3>Resumo do Dia</h3>
                <ul>
                    <li><strong>Total de Atendimentos:</strong> ${stats.total}</li>
                    <li><strong>Emergências (Prioridade Alta):</strong> ${stats.nivel3}</li>
                    <li><strong>Casos Moderados:</strong> ${stats.nivel2}</li>
                    <li><strong>Casos Leves:</strong> ${stats.nivel1}</li>
                </ul>
                
                <h3>Sintomas Mais Relatados</h3>
                ${this.generateSymptomsTable()}
                
                <h3>Observações</h3>
                <p>• Sistema funcionando normalmente</p>
                <p>• Todos os pacientes foram devidamente classificados</p>
                <p>• Relatório gerado automaticamente pelo Sistema Ordinix-123</p>
            </div>
        `;
    }

    generatePatientTable(patients = this.pacientes) {
        if (patients.length === 0) {
            return '<p>Nenhum paciente cadastrado.</p>';
        }

        let table = `
            <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                <thead>
                    <tr style="background: #f8f9fa;">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Nome</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">CPF</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Idade</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Prioridade</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Data/Hora</th>
                    </tr>
                </thead>
                <tbody>
        `;

        patients.forEach(paciente => {
            const prioridadeText = this.getPrioridadeText(paciente.prioridade);
            const dataHora = new Date(paciente.dataHora).toLocaleString('pt-BR');
            
            table += `
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">${paciente.nome}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${paciente.cpf}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${paciente.idade}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${prioridadeText}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${dataHora}</td>
                </tr>
            `;
        });

        table += '</tbody></table>';
        return table;
    }

    generateAgeTable() {
        const ageDistribution = this.getAgeDistribution();
        
        let table = `
            <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
                <thead>
                    <tr style="background: #f8f9fa;">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Faixa Etária</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Quantidade</th>
                    </tr>
                </thead>
                <tbody>
        `;

        Object.entries(ageDistribution).forEach(([faixa, quantidade]) => {
            table += `
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">${faixa}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${quantidade}</td>
                </tr>
            `;
        });

        table += '</tbody></table>';
        return table;
    }

    generateSymptomsTable() {
        const symptoms = this.getCommonSymptoms();
        
        if (symptoms.length === 0) {
            return '<p>Nenhum sintoma registrado.</p>';
        }

        let table = `
            <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
                <thead>
                    <tr style="background: #f8f9fa;">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Sintoma</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Frequência</th>
                    </tr>
                </thead>
                <tbody>
        `;

        symptoms.forEach(symptom => {
            table += `
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">${symptom.sintoma}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${symptom.count}</td>
                </tr>
            `;
        });

        table += '</tbody></table>';
        return table;
    }

    generateRecentPatientsTable() {
        const recentPatients = this.pacientes
            .sort((a, b) => new Date(b.dataHora) - new Date(a.dataHora))
            .slice(0, 5);

        if (recentPatients.length === 0) {
            return '<p>Nenhum paciente recente.</p>';
        }

        let table = `
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="background: #f8f9fa;">
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Nome</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Prioridade</th>
                        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Hora</th>
                    </tr>
                </thead>
                <tbody>
        `;

        recentPatients.forEach(paciente => {
            const prioridadeText = this.getPrioridadeText(paciente.prioridade);
            const hora = new Date(paciente.dataHora).toLocaleTimeString('pt-BR');
            
            table += `
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">${paciente.nome}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${prioridadeText}</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">${hora}</td>
                </tr>
            `;
        });

        table += '</tbody></table>';
        return table;
    }

    printContent() {
        window.print();
    }
}

// Inicializar sistema quando a página carregar
let sistema;
document.addEventListener('DOMContentLoaded', () => {
    sistema = new SistemaVidaPlus();
});