/**
 * CLÍNICA VIDA+ - Sistema Ordinix-123
 * Main JavaScript File
 * Funcionalidades principais e utilitários
 */

// ===== CONFIGURAÇÕES GLOBAIS =====
const CONFIG = {
    API_BASE_URL: window.location.origin,
    SOCKET_NAMESPACE: '/',
    DEBOUNCE_DELAY: 300,
    ANIMATION_DURATION: 300,
    TOAST_DURATION: 5000,
    PAGINATION_SIZE: 10,
    MAX_FILE_SIZE: 5 * 1024 * 1024, // 5MB
    ALLOWED_FILE_TYPES: ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'],
    DATE_FORMAT: 'DD/MM/YYYY',
    DATETIME_FORMAT: 'DD/MM/YYYY HH:mm',
    CURRENCY_FORMAT: 'pt-BR'
};

// ===== ESTADO GLOBAL DA APLICAÇÃO =====
const AppState = {
    user: null,
    socket: null,
    isOnline: navigator.onLine,
    notifications: [],
    modals: new Map(),
    forms: new Map(),
    cache: new Map(),
    
    // Getters e Setters
    setUser(user) {
        this.user = user;
        this.saveToStorage('user', user);
        this.emit('userChanged', user);
    },
    
    getUser() {
        return this.user || this.loadFromStorage('user');
    },
    
    // Event System
    listeners: new Map(),
    
    on(event, callback) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }
        this.listeners.get(event).push(callback);
    },
    
    emit(event, data) {
        if (this.listeners.has(event)) {
            this.listeners.get(event).forEach(callback => callback(data));
        }
    },
    
    // Storage
    saveToStorage(key, value) {
        try {
            localStorage.setItem(`clinica_${key}`, JSON.stringify(value));
        } catch (error) {
            console.warn('Erro ao salvar no localStorage:', error);
        }
    },
    
    loadFromStorage(key) {
        try {
            const value = localStorage.getItem(`clinica_${key}`);
            return value ? JSON.parse(value) : null;
        } catch (error) {
            console.warn('Erro ao carregar do localStorage:', error);
            return null;
        }
    }
};

// ===== UTILITÁRIOS =====
const Utils = {
    // Debounce function
    debounce(func, delay = CONFIG.DEBOUNCE_DELAY) {
        let timeoutId;
        return function (...args) {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => func.apply(this, args), delay);
        };
    },
    
    // Throttle function
    throttle(func, delay) {
        let lastCall = 0;
        return function (...args) {
            const now = Date.now();
            if (now - lastCall >= delay) {
                lastCall = now;
                return func.apply(this, args);
            }
        };
    },
    
    // Formatação de dados
    formatCPF(cpf) {
        return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    },
    
    formatPhone(phone) {
        if (phone.length === 11) {
            return phone.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        }
        return phone.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
    },
    
    formatCEP(cep) {
        return cep.replace(/(\d{5})(\d{3})/, '$1-$2');
    },
    
    formatCurrency(value) {
        return new Intl.NumberFormat(CONFIG.CURRENCY_FORMAT, {
            style: 'currency',
            currency: 'BRL'
        }).format(value);
    },
    
    formatDate(date, format = CONFIG.DATE_FORMAT) {
        if (!date) return '';
        const d = new Date(date);
        if (format === 'DD/MM/YYYY') {
            return d.toLocaleDateString('pt-BR');
        }
        if (format === 'DD/MM/YYYY HH:mm') {
            return d.toLocaleString('pt-BR');
        }
        return d.toISOString();
    },
    
    // Validações
    validateCPF(cpf) {
        cpf = cpf.replace(/[^\d]/g, '');
        if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) return false;
        
        let sum = 0;
        for (let i = 0; i < 9; i++) {
            sum += parseInt(cpf.charAt(i)) * (10 - i);
        }
        let remainder = 11 - (sum % 11);
        if (remainder === 10 || remainder === 11) remainder = 0;
        if (remainder !== parseInt(cpf.charAt(9))) return false;
        
        sum = 0;
        for (let i = 0; i < 10; i++) {
            sum += parseInt(cpf.charAt(i)) * (11 - i);
        }
        remainder = 11 - (sum % 11);
        if (remainder === 10 || remainder === 11) remainder = 0;
        return remainder === parseInt(cpf.charAt(10));
    },
    
    validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    },
    
    validatePhone(phone) {
        const cleaned = phone.replace(/[^\d]/g, '');
        return cleaned.length === 10 || cleaned.length === 11;
    },
    
    // Manipulação de DOM
    createElement(tag, attributes = {}, children = []) {
        const element = document.createElement(tag);
        
        Object.entries(attributes).forEach(([key, value]) => {
            if (key === 'className') {
                element.className = value;
            } else if (key === 'innerHTML') {
                element.innerHTML = value;
            } else if (key.startsWith('data-')) {
                element.setAttribute(key, value);
            } else {
                element[key] = value;
            }
        });
        
        children.forEach(child => {
            if (typeof child === 'string') {
                element.appendChild(document.createTextNode(child));
            } else {
                element.appendChild(child);
            }
        });
        
        return element;
    },
    
    // Animações
    fadeIn(element, duration = CONFIG.ANIMATION_DURATION) {
        element.style.opacity = '0';
        element.style.display = 'block';
        
        const start = performance.now();
        
        function animate(currentTime) {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            
            element.style.opacity = progress;
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        }
        
        requestAnimationFrame(animate);
    },
    
    fadeOut(element, duration = CONFIG.ANIMATION_DURATION) {
        const start = performance.now();
        const initialOpacity = parseFloat(getComputedStyle(element).opacity);
        
        function animate(currentTime) {
            const elapsed = currentTime - start;
            const progress = Math.min(elapsed / duration, 1);
            
            element.style.opacity = initialOpacity * (1 - progress);
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                element.style.display = 'none';
            }
        }
        
        requestAnimationFrame(animate);
    },
    
    // Geração de IDs únicos
    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    },
    
    // Sanitização de strings
    sanitizeHTML(str) {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    },
    
    // Cópia para clipboard
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            Toast.success('Copiado para a área de transferência!');
            return true;
        } catch (error) {
            console.error('Erro ao copiar:', error);
            Toast.error('Erro ao copiar para a área de transferência');
            return false;
        }
    }
};

// ===== SISTEMA DE NOTIFICAÇÕES (TOAST) =====
const Toast = {
    container: null,
    
    init() {
        if (!this.container) {
            this.container = Utils.createElement('div', {
                className: 'toast-container position-fixed top-0 end-0 p-3',
                style: 'z-index: 1070;'
            });
            document.body.appendChild(this.container);
        }
    },
    
    show(message, type = 'info', duration = CONFIG.TOAST_DURATION) {
        this.init();
        
        const toastId = Utils.generateId();
        const toast = Utils.createElement('div', {
            className: `toast align-items-center text-white bg-${type} border-0 mb-2`,
            'data-toast-id': toastId,
            role: 'alert'
        });
        
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${Utils.sanitizeHTML(message)}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" 
                        onclick="Toast.hide('${toastId}')"></button>
            </div>
        `;
        
        this.container.appendChild(toast);
        
        // Animação de entrada
        Utils.fadeIn(toast);
        
        // Auto-hide
        if (duration > 0) {
            setTimeout(() => this.hide(toastId), duration);
        }
        
        return toastId;
    },
    
    hide(toastId) {
        const toast = document.querySelector(`[data-toast-id="${toastId}"]`);
        if (toast) {
            Utils.fadeOut(toast, 200);
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 200);
        }
    },
    
    success(message, duration) {
        return this.show(message, 'success', duration);
    },
    
    error(message, duration) {
        return this.show(message, 'danger', duration);
    },
    
    warning(message, duration) {
        return this.show(message, 'warning', duration);
    },
    
    info(message, duration) {
        return this.show(message, 'info', duration);
    }
};

// ===== SISTEMA DE MODAIS =====
const Modal = {
    show(modalId, options = {}) {
        const modal = document.getElementById(modalId);
        if (!modal) {
            console.error(`Modal ${modalId} não encontrado`);
            return;
        }
        
        // Configurações padrão
        const config = {
            backdrop: true,
            keyboard: true,
            focus: true,
            ...options
        };
        
        // Armazenar configurações
        AppState.modals.set(modalId, config);
        
        // Mostrar modal
        modal.style.display = 'block';
        modal.classList.add('show');
        document.body.classList.add('modal-open');
        
        // Criar backdrop se necessário
        if (config.backdrop) {
            this.createBackdrop(modalId);
        }
        
        // Focar no modal
        if (config.focus) {
            modal.focus();
        }
        
        // Event listeners
        if (config.keyboard) {
            document.addEventListener('keydown', this.handleKeydown);
        }
        
        // Trigger event
        modal.dispatchEvent(new CustomEvent('shown.modal'));
    },
    
    hide(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        
        modal.style.display = 'none';
        modal.classList.remove('show');
        document.body.classList.remove('modal-open');
        
        // Remover backdrop
        this.removeBackdrop(modalId);
        
        // Remover event listeners
        document.removeEventListener('keydown', this.handleKeydown);
        
        // Limpar configurações
        AppState.modals.delete(modalId);
        
        // Trigger event
        modal.dispatchEvent(new CustomEvent('hidden.modal'));
    },
    
    createBackdrop(modalId) {
        const backdrop = Utils.createElement('div', {
            className: 'modal-backdrop fade show',
            'data-modal-id': modalId
        });
        
        backdrop.addEventListener('click', () => {
            const config = AppState.modals.get(modalId);
            if (config && config.backdrop !== 'static') {
                this.hide(modalId);
            }
        });
        
        document.body.appendChild(backdrop);
    },
    
    removeBackdrop(modalId) {
        const backdrop = document.querySelector(`[data-modal-id="${modalId}"]`);
        if (backdrop) {
            backdrop.parentNode.removeChild(backdrop);
        }
    },
    
    handleKeydown(event) {
        if (event.key === 'Escape') {
            // Fechar o modal mais recente
            const modals = Array.from(AppState.modals.keys());
            if (modals.length > 0) {
                const lastModal = modals[modals.length - 1];
                Modal.hide(lastModal);
            }
        }
    }
};

// ===== SISTEMA DE FORMULÁRIOS =====
const FormHandler = {
    init() {
        // Auto-inicializar formulários com data-form
        document.querySelectorAll('[data-form]').forEach(form => {
            this.setupForm(form);
        });
    },
    
    setupForm(form) {
        const formId = form.getAttribute('data-form') || Utils.generateId();
        form.setAttribute('data-form', formId);
        
        // Configurações do formulário
        const config = {
            validate: form.hasAttribute('data-validate'),
            ajax: form.hasAttribute('data-ajax'),
            realtime: form.hasAttribute('data-realtime'),
            autosave: form.hasAttribute('data-autosave')
        };
        
        AppState.forms.set(formId, config);
        
        // Event listeners
        form.addEventListener('submit', (e) => this.handleSubmit(e, formId));
        
        if (config.realtime) {
            form.addEventListener('input', Utils.debounce((e) => this.handleInput(e, formId)));
        }
        
        if (config.autosave) {
            form.addEventListener('input', Utils.debounce(() => this.autosave(formId), 1000));
        }
        
        // Configurar validação em tempo real
        if (config.validate) {
            this.setupValidation(form);
        }
    },
    
    setupValidation(form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        
        inputs.forEach(input => {
            input.addEventListener('blur', () => this.validateField(input));
            input.addEventListener('input', Utils.debounce(() => this.validateField(input), 500));
        });
    },
    
    validateField(field) {
        const value = field.value.trim();
        const type = field.type;
        const required = field.hasAttribute('required');
        
        let isValid = true;
        let message = '';
        
        // Validação de campo obrigatório
        if (required && !value) {
            isValid = false;
            message = 'Este campo é obrigatório';
        }
        
        // Validações específicas por tipo
        if (value && isValid) {
            switch (type) {
                case 'email':
                    if (!Utils.validateEmail(value)) {
                        isValid = false;
                        message = 'Email inválido';
                    }
                    break;
                    
                case 'tel':
                    if (!Utils.validatePhone(value)) {
                        isValid = false;
                        message = 'Telefone inválido';
                    }
                    break;
            }
            
            // Validações customizadas
            if (field.hasAttribute('data-validate-cpf')) {
                if (!Utils.validateCPF(value)) {
                    isValid = false;
                    message = 'CPF inválido';
                }
            }
        }
        
        // Aplicar resultado da validação
        this.setFieldValidation(field, isValid, message);
        
        return isValid;
    },
    
    setFieldValidation(field, isValid, message = '') {
        const feedback = field.parentNode.querySelector('.invalid-feedback') || 
                        field.parentNode.querySelector('.valid-feedback');
        
        if (isValid) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            
            if (feedback) {
                feedback.textContent = '';
                feedback.className = 'valid-feedback';
            }
        } else {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            
            if (feedback) {
                feedback.textContent = message;
                feedback.className = 'invalid-feedback';
            } else {
                // Criar elemento de feedback
                const feedbackEl = Utils.createElement('div', {
                    className: 'invalid-feedback',
                    innerHTML: message
                });
                field.parentNode.appendChild(feedbackEl);
            }
        }
    },
    
    validateForm(form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        let isValid = true;
        
        inputs.forEach(input => {
            if (!this.validateField(input)) {
                isValid = false;
            }
        });
        
        return isValid;
    },
    
    handleSubmit(event, formId) {
        const form = event.target;
        const config = AppState.forms.get(formId);
        
        // Validar formulário se necessário
        if (config.validate && !this.validateForm(form)) {
            event.preventDefault();
            Toast.error('Por favor, corrija os erros no formulário');
            return;
        }
        
        // Submissão AJAX
        if (config.ajax) {
            event.preventDefault();
            this.submitAjax(form, formId);
        }
    },
    
    async submitAjax(form, formId) {
        const submitBtn = form.querySelector('[type="submit"]');
        const originalText = submitBtn ? submitBtn.textContent : '';
        
        try {
            // Loading state
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Enviando...';
            }
            
            const formData = new FormData(form);
            const response = await fetch(form.action || window.location.href, {
                method: form.method || 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            
            const result = await response.json();
            
            if (result.success) {
                Toast.success(result.message || 'Operação realizada com sucesso!');
                
                // Trigger custom event
                form.dispatchEvent(new CustomEvent('form.success', { detail: result }));
                
                // Reset form se especificado
                if (result.reset) {
                    form.reset();
                    this.clearValidation(form);
                }
                
                // Redirect se especificado
                if (result.redirect) {
                    setTimeout(() => {
                        window.location.href = result.redirect;
                    }, 1000);
                }
            } else {
                Toast.error(result.message || 'Erro ao processar solicitação');
                
                // Mostrar erros de campo
                if (result.errors) {
                    this.showFieldErrors(form, result.errors);
                }
            }
            
        } catch (error) {
            console.error('Erro na submissão:', error);
            Toast.error('Erro de conexão. Tente novamente.');
        } finally {
            // Restaurar botão
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            }
        }
    },
    
    showFieldErrors(form, errors) {
        Object.entries(errors).forEach(([fieldName, message]) => {
            const field = form.querySelector(`[name="${fieldName}"]`);
            if (field) {
                this.setFieldValidation(field, false, message);
            }
        });
    },
    
    clearValidation(form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.classList.remove('is-valid', 'is-invalid');
        });
        
        const feedbacks = form.querySelectorAll('.invalid-feedback, .valid-feedback');
        feedbacks.forEach(feedback => feedback.remove());
    },
    
    autosave(formId) {
        const form = document.querySelector(`[data-form="${formId}"]`);
        if (!form) return;
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        AppState.saveToStorage(`autosave_${formId}`, data);
        
        // Mostrar indicador de salvamento
        const indicator = form.querySelector('.autosave-indicator');
        if (indicator) {
            indicator.textContent = 'Salvo automaticamente';
            indicator.style.opacity = '1';
            setTimeout(() => {
                indicator.style.opacity = '0';
            }, 2000);
        }
    },
    
    loadAutosave(formId) {
        const data = AppState.loadFromStorage(`autosave_${formId}`);
        if (!data) return;
        
        const form = document.querySelector(`[data-form="${formId}"]`);
        if (!form) return;
        
        Object.entries(data).forEach(([name, value]) => {
            const field = form.querySelector(`[name="${name}"]`);
            if (field) {
                field.value = value;
            }
        });
    }
};

// ===== SISTEMA DE MÁSCARAS DE INPUT =====
const InputMask = {
    init() {
        // Auto-aplicar máscaras baseadas em data-mask
        document.querySelectorAll('[data-mask]').forEach(input => {
            const maskType = input.getAttribute('data-mask');
            this.applyMask(input, maskType);
        });
    },
    
    applyMask(input, maskType) {
        input.addEventListener('input', (e) => {
            const value = e.target.value.replace(/[^\d]/g, '');
            
            switch (maskType) {
                case 'cpf':
                    e.target.value = this.maskCPF(value);
                    break;
                case 'phone':
                    e.target.value = this.maskPhone(value);
                    break;
                case 'cep':
                    e.target.value = this.maskCEP(value);
                    break;
                case 'date':
                    e.target.value = this.maskDate(value);
                    break;
            }
        });
    },
    
    maskCPF(value) {
        return value
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d{1,2})/, '$1-$2')
            .replace(/(-\d{2})\d+?$/, '$1');
    },
    
    maskPhone(value) {
        if (value.length <= 10) {
            return value
                .replace(/(\d{2})(\d)/, '($1) $2')
                .replace(/(\d{4})(\d)/, '$1-$2')
                .replace(/(-\d{4})\d+?$/, '$1');
        } else {
            return value
                .replace(/(\d{2})(\d)/, '($1) $2')
                .replace(/(\d{5})(\d)/, '$1-$2')
                .replace(/(-\d{4})\d+?$/, '$1');
        }
    },
    
    maskCEP(value) {
        return value
            .replace(/(\d{5})(\d)/, '$1-$2')
            .replace(/(-\d{3})\d+?$/, '$1');
    },
    
    maskDate(value) {
        return value
            .replace(/(\d{2})(\d)/, '$1/$2')
            .replace(/(\d{2})(\d)/, '$1/$2')
            .replace(/(\d{4})\d+?$/, '$1');
    }
};

// ===== SISTEMA DE BUSCA EM TEMPO REAL =====
const LiveSearch = {
    init() {
        document.querySelectorAll('[data-live-search]').forEach(input => {
            this.setupSearch(input);
        });
    },
    
    setupSearch(input) {
        const targetSelector = input.getAttribute('data-live-search');
        const minLength = parseInt(input.getAttribute('data-min-length')) || 2;
        
        input.addEventListener('input', Utils.debounce((e) => {
            const query = e.target.value.trim();
            
            if (query.length >= minLength) {
                this.performSearch(query, targetSelector);
            } else {
                this.clearResults(targetSelector);
            }
        }));
    },
    
    async performSearch(query, targetSelector) {
        const container = document.querySelector(targetSelector);
        if (!container) return;
        
        try {
            // Mostrar loading
            this.showLoading(container);
            
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            });
            
            const results = await response.json();
            this.displayResults(container, results);
            
        } catch (error) {
            console.error('Erro na busca:', error);
            this.showError(container);
        }
    },
    
    showLoading(container) {
        container.innerHTML = `
            <div class="text-center p-3">
                <i class="fas fa-spinner fa-spin"></i>
                <span class="ms-2">Buscando...</span>
            </div>
        `;
    },
    
    showError(container) {
        container.innerHTML = `
            <div class="text-center p-3 text-muted">
                <i class="fas fa-exclamation-triangle"></i>
                <span class="ms-2">Erro na busca</span>
            </div>
        `;
    },
    
    clearResults(targetSelector) {
        const container = document.querySelector(targetSelector);
        if (container) {
            container.innerHTML = '';
        }
    },
    
    displayResults(container, results) {
        if (!results || results.length === 0) {
            container.innerHTML = `
                <div class="text-center p-3 text-muted">
                    <i class="fas fa-search"></i>
                    <span class="ms-2">Nenhum resultado encontrado</span>
                </div>
            `;
            return;
        }
        
        const html = results.map(item => `
            <div class="search-result-item p-2 border-bottom" data-id="${item.id}">
                <div class="fw-medium">${Utils.sanitizeHTML(item.name)}</div>
                <div class="text-muted small">${Utils.sanitizeHTML(item.description || '')}</div>
            </div>
        `).join('');
        
        container.innerHTML = html;
        
        // Adicionar event listeners aos resultados
        container.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', () => {
                const id = item.getAttribute('data-id');
                this.selectResult(id, item);
            });
        });
    },
    
    selectResult(id, element) {
        // Trigger custom event
        document.dispatchEvent(new CustomEvent('search.select', {
            detail: { id, element }
        }));
    }
};

// ===== INICIALIZAÇÃO =====
document.addEventListener('DOMContentLoaded', function() {
    console.log('🏥 CLÍNICA VIDA+ - Sistema Ordinix-123 iniciado');
    
    // Inicializar sistemas
    FormHandler.init();
    InputMask.init();
    LiveSearch.init();
    
    // Configurar Socket.IO se disponível
    if (typeof io !== 'undefined') {
        AppState.socket = io(CONFIG.SOCKET_NAMESPACE);
        
        AppState.socket.on('connect', () => {
            console.log('✅ Conectado ao servidor');
            AppState.isOnline = true;
        });
        
        AppState.socket.on('disconnect', () => {
            console.log('❌ Desconectado do servidor');
            AppState.isOnline = false;
        });
        
        // Eventos personalizados
        AppState.socket.on('notification', (data) => {
            Toast.info(data.message);
        });
        
        AppState.socket.on('patient_update', (data) => {
            // Atualizar interface quando paciente for modificado
            document.dispatchEvent(new CustomEvent('patient.updated', { detail: data }));
        });
    }
    
    // Monitorar status de conexão
    window.addEventListener('online', () => {
        AppState.isOnline = true;
        Toast.success('Conexão restaurada');
    });
    
    window.addEventListener('offline', () => {
        AppState.isOnline = false;
        Toast.warning('Sem conexão com a internet');
    });
    
    // Configurar event listeners globais
    document.addEventListener('click', (e) => {
        // Auto-fechar dropdowns
        if (!e.target.closest('.dropdown')) {
            document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
                menu.classList.remove('show');
            });
        }
        
        // Handlers para botões com data-action
        const actionBtn = e.target.closest('[data-action]');
        if (actionBtn) {
            const action = actionBtn.getAttribute('data-action');
            handleAction(action, actionBtn);
        }
    });
    
    // Handler para ações de botões
    function handleAction(action, element) {
        switch (action) {
            case 'modal-show':
                const modalId = element.getAttribute('data-target');
                if (modalId) Modal.show(modalId);
                break;
                
            case 'modal-hide':
                const closeModalId = element.getAttribute('data-target') || 
                                   element.closest('.modal')?.id;
                if (closeModalId) Modal.hide(closeModalId);
                break;
                
            case 'copy-text':
                const textToCopy = element.getAttribute('data-text') || 
                                 element.textContent;
                Utils.copyToClipboard(textToCopy);
                break;
                
            case 'toggle-password':
                const targetInput = document.querySelector(element.getAttribute('data-target'));
                if (targetInput) {
                    const isPassword = targetInput.type === 'password';
                    targetInput.type = isPassword ? 'text' : 'password';
                    element.innerHTML = isPassword ? 
                        '<i class="fas fa-eye-slash"></i>' : 
                        '<i class="fas fa-eye"></i>';
                }
                break;
        }
    }
    
    console.log('🚀 Sistema inicializado com sucesso!');
});

// ===== EXPORTAR PARA ESCOPO GLOBAL =====
window.ClinicaApp = {
    Utils,
    Toast,
    Modal,
    FormHandler,
    InputMask,
    LiveSearch,
    AppState,
    CONFIG
};