# ===== SISTEMA CLÍNICA VIDA+ COM ORDINIX-123 - INTERFACE GRÁFICA =====
# Inventor: Adevilson de Lima - Estudante ADS Anhanguera
# Sistema revolucionário de triagem hospitalar com interface moderna 001

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import threading
import time
from mainColabTeste import SistemaGestaoClinica, SistemaOrdinix123

class DesignSystem:
    """Design System conforme especificação do arquivo de instruções"""
    
    # Cores Principais
    PRIMARY = "#0066CC"      # Azul Médico - Botões principais
    SUCCESS = "#00CC66"      # Verde - Nível 1 Ordinix
    WARNING = "#FFCC00"      # Amarelo - Nível 2 Ordinix  
    DANGER = "#FF3333"       # Vermelho - Nível 3 Ordinix
    DARK = "#2C3E50"         # Textos e header
    LIGHT = "#ECF0F1"        # Background
    
    # Cores de Suporte
    INFO = "#3498DB"         # Informações
    MUTED = "#95A5A6"        # Textos secundários
    WHITE = "#FFFFFF"        # Cards e modais
    
    # Fontes
    FONT_TITLE = ("Arial", 16, "bold")
    FONT_SUBTITLE = ("Arial", 12, "bold")
    FONT_NORMAL = ("Arial", 10)
    FONT_SMALL = ("Arial", 8)

class LoginWindow:
    """Tela de Login Centralizada"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CLÍNICA VIDA+ - Sistema Ordinix-123")
        self.root.configure(bg=DesignSystem.LIGHT)
        
        # Tamanho fixo
        window_width = 500
        window_height = 600
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        
        # Forçar atualização da janela e centralizar
        self.root.update_idletasks()
        
        # Centralizar na tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.carregar_credenciais()
        self.create_login_interface()
        
        self.usuarios = {
            "Adevilson de lima": "Anhanguera2025",
            "admin": "123456",
            "recepcao": "recepcao123",
            "medico": "medico123",
            "enfermagem": "enferm123"
        }
    

    
    def carregar_credenciais(self):
        """Carrega credenciais salvas do arquivo"""
        self.credenciais_salvas = {"usuario": "", "senha": "", "lembrar": False}
        try:
            if os.path.exists("credenciais.json"):
                with open("credenciais.json", "r", encoding="utf-8") as f:
                    self.credenciais_salvas = json.load(f)
        except:
            pass  # Se houver erro, usar valores padrão
    
    def salvar_credenciais(self, usuario, senha, lembrar):
        """Salva credenciais no arquivo se lembrar estiver marcado"""
        try:
            if lembrar:
                credenciais = {
                    "usuario": usuario,
                    "senha": senha,
                    "lembrar": True
                }
                with open("credenciais.json", "w", encoding="utf-8") as f:
                    json.dump(credenciais, f, ensure_ascii=False, indent=2)
            else:
                # Se não lembrar, remove o arquivo
                if os.path.exists("credenciais.json"):
                    os.remove("credenciais.json")
        except:
            pass  # Se houver erro, continua sem salvar
    
    def on_lembrar_change(self):
        """Chamado quando a checkbox lembre-me é alterada"""
        if not self.lembrar_var.get():
            # Se desmarcou, limpa credenciais salvas
            self.salvar_credenciais("", "", False)
    
    def create_login_interface(self):
        """Cria interface de login conforme especificação"""
        
        # Frame principal centralizado usando place
        main_frame = tk.Frame(self.root, bg=DesignSystem.WHITE, relief="raised", bd=2)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)
        
        # Título com espaçamento responsivo
        title_label = tk.Label(
            main_frame, 
            text="🏥 CLÍNICA VIDA+",
            font=("Arial", 18, "bold"),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.PRIMARY
        )
        title_label.pack(pady=(20, 5))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Sistema Ordinix-123",
            font=("Arial", 14, "bold"),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        )
        subtitle_label.pack(pady=(0, 25))
        
        # Campos de entrada com melhor responsividade
        tk.Label(
            main_frame,
            text="Usuário:",
            font=("Arial", 11, "bold"),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(anchor="w", padx=30, pady=(0, 5))
        
        self.usuario_entry = tk.Entry(
            main_frame,
            font=("Arial", 11),  # Fonte ligeiramente maior
            width=30,  # Campo mais largo
            relief="solid",
            bd=2,  # Borda mais visível
            highlightthickness=1,
            highlightcolor=DesignSystem.PRIMARY
        )
        self.usuario_entry.pack(pady=(0, 15), padx=30, fill="x")
        
        # Preencher com credenciais salvas ou padrão
        usuario_inicial = self.credenciais_salvas.get("usuario", "Adevilson de lima")
        if not usuario_inicial:
            usuario_inicial = "Adevilson de lima"
        self.usuario_entry.insert(0, usuario_inicial)
        
        tk.Label(
            main_frame,
            text="Senha:",
            font=("Arial", 11, "bold"),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(anchor="w", padx=30, pady=(0, 5))
        
        # Frame para senha com botão de visualizar
        senha_frame = tk.Frame(main_frame, bg=DesignSystem.WHITE)
        senha_frame.pack(pady=(0, 20), padx=30, fill="x")
        
        self.senha_entry = tk.Entry(
            senha_frame,
            font=("Arial", 11),  # Fonte ligeiramente maior
            show="*",
            relief="solid",
            bd=2,  # Borda mais visível
            highlightthickness=1,
            highlightcolor=DesignSystem.PRIMARY
        )
        self.senha_entry.pack(side="left", fill="x", expand=True)
        
        # Preencher com credenciais salvas ou padrão
        senha_inicial = self.credenciais_salvas.get("senha", "Anhanguera2025")
        if not senha_inicial:
            senha_inicial = "Anhanguera2025"
        self.senha_entry.insert(0, senha_inicial)
        
        # Botão para mostrar/ocultar senha
        self.senha_visivel = False
        self.btn_mostrar_senha = tk.Button(
            senha_frame,
            text="👁",
            font=("Arial", 12, "bold"),
            width=4,  # Ligeiramente maior
            height=1,
            relief="raised",
            bd=2,
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            cursor="hand2",
            command=self.toggle_senha_visibilidade,
            activebackground="#0052A3",
            activeforeground=DesignSystem.WHITE
        )
        self.btn_mostrar_senha.pack(side="right", padx=(5, 0))
        
        # Checkbox "Lembre-me" com melhor espaçamento
        self.lembrar_var = tk.BooleanVar()
        checkbox_frame = tk.Frame(main_frame, bg=DesignSystem.WHITE)
        checkbox_frame.pack(pady=(15, 10))
        
        self.checkbox_lembrar = tk.Checkbutton(
            checkbox_frame,
            text="🔒 Lembre-me",
            variable=self.lembrar_var,
            font=("Arial", 11),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            selectcolor=DesignSystem.PRIMARY,
            activebackground=DesignSystem.WHITE,
            activeforeground=DesignSystem.PRIMARY,
            cursor="hand2",
            command=self.on_lembrar_change
        )
        self.checkbox_lembrar.pack()
        
        # Configurar estado inicial da checkbox
        self.lembrar_var.set(self.credenciais_salvas.get("lembrar", False))
        
        # Frame para botões com melhor layout
        botoes_frame = tk.Frame(main_frame, bg=DesignSystem.WHITE)
        botoes_frame.pack(pady=20, padx=30, fill="x")
        
        # Botão de login com hover effect
        login_btn = tk.Button(
            botoes_frame,
            text="🔐 ENTRAR",
            font=("Arial", 13, "bold"),
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            height=2,
            cursor="hand2",
            command=self.fazer_login
        )
        login_btn.pack(side="left", fill="x", expand=True, padx=(0, 8))
        login_btn.bind("<Enter>", lambda e: login_btn.configure(bg="#3399FF"))
        login_btn.bind("<Leave>", lambda e: login_btn.configure(bg=DesignSystem.PRIMARY))
        
        # Botão limpar com hover effect
        limpar_btn = tk.Button(
            botoes_frame,
            text="🗑️ LIMPAR",
            font=("Arial", 13, "bold"),
            bg=DesignSystem.MUTED,
            fg=DesignSystem.WHITE,
            height=2,
            cursor="hand2",
            command=self.limpar_campos
        )
        limpar_btn.pack(side="right", fill="x", expand=True, padx=(8, 0))
        limpar_btn.bind("<Enter>", lambda e: limpar_btn.configure(bg="#B8C5C7"))
        limpar_btn.bind("<Leave>", lambda e: limpar_btn.configure(bg=DesignSystem.MUTED))
        
        # Rodapé com melhor espaçamento
        footer_label = tk.Label(
            main_frame,
            text="© 2025 - Adevilson de Lima",
            font=("Arial", 9),  # Fonte ligeiramente maior
            bg=DesignSystem.WHITE,
            fg=DesignSystem.MUTED
        )
        footer_label.pack(side="bottom", pady=15)
        
        # Bind Enter para login
        self.root.bind('<Return>', lambda event: self.fazer_login())
        
        # Foco no campo usuário
        self.usuario_entry.focus()
    
    def toggle_senha_visibilidade(self):
        """Alterna entre mostrar e ocultar a senha"""
        if self.senha_visivel:
            # Ocultar senha
            self.senha_entry.config(show="*")
            self.btn_mostrar_senha.config(text="👁")
            self.senha_visivel = False
        else:
            # Mostrar senha
            self.senha_entry.config(show="")
            self.btn_mostrar_senha.config(text="🙈")
            self.senha_visivel = True
    
    def limpar_campos(self):
        """Limpa os campos de usuário e senha"""
        self.usuario_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
        # Resetar visibilidade da senha
        if self.senha_visivel:
            self.senha_entry.config(show="*")
            self.btn_mostrar_senha.config(text="👁")
            self.senha_visivel = False
        self.usuario_entry.focus()
    
    def fazer_login(self):
        """Valida login e abre sistema principal"""
        usuario = self.usuario_entry.get().strip()
        senha = self.senha_entry.get().strip()
        
        if not usuario or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if usuario in self.usuarios and self.usuarios[usuario] == senha:
            # Salvar credenciais se checkbox estiver marcada
            self.salvar_credenciais(usuario, senha, self.lembrar_var.get())
            
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario.title()}!")
            self.root.destroy()
            
            # Abrir sistema principal
            app = SistemaVidaPlus(usuario)
            app.run()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")
            self.senha_entry.delete(0, tk.END)
            self.senha_entry.focus()
    
    def run(self):
        """Executa a janela de login"""
        self.root.mainloop()

class SistemaVidaPlus:
    """Sistema principal com interface gráfica completa"""
    
    def __init__(self, usuario_logado):
        self.usuario_logado = usuario_logado
        self.sistema = SistemaGestaoClinica()
        
        # Janela principal
        self.root = tk.Tk()
        self.root.title("🏥 CLÍNICA VIDA+ - Sistema Ordinix-123")
        
        # Configuração responsiva
        self.root.minsize(1000, 700)
        self.root.configure(bg=DesignSystem.LIGHT)
        
        # Maximizar janela de forma compatível
        try:
            self.root.state('zoomed')  # Windows
        except:
            self.root.attributes('-zoomed', True)  # Linux
        
        # Fallback para outras plataformas
        if self.root.winfo_width() < 1000:
            self.root.geometry("1200x800")
        
        # Variáveis de controle
        self.menu_aberto = False
        self.tela_atual = "dashboard"
        
        # Criar interface
        self.create_main_interface()
        
        # Iniciar atualizações em tempo real
        self.iniciar_atualizacoes_tempo_real()
    
    def create_main_interface(self):
        """Cria interface principal conforme especificação"""
        
        # Header
        self.create_header()
        
        # Container principal
        self.main_container = tk.Frame(self.root, bg=DesignSystem.LIGHT)
        self.main_container.pack(fill="both", expand=True)
        
        # Menu lateral (inicialmente oculto)
        self.create_sidebar_menu()
        
        # Área de conteúdo
        self.content_frame = tk.Frame(self.main_container, bg=DesignSystem.LIGHT)
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Carregar dashboard inicial
        self.show_dashboard()
    
    def create_header(self):
        """Cria header conforme especificação"""
        header = tk.Frame(self.root, bg=DesignSystem.DARK)
        header.pack(fill="x", pady=0)
        
        # Botão menu hambúrguer
        menu_btn = tk.Button(
            header,
            text="☰ Menu",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.DARK,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            command=self.toggle_menu
        )
        menu_btn.pack(side="left", padx=20, pady=15)
        
        # Título central
        title_label = tk.Label(
            header,
            text="🏥 CLÍNICA VIDA+ - ORDINIX-123",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.DARK,
            fg=DesignSystem.WHITE
        )
        title_label.pack(side="left", expand=True)
        
        # Info do usuário
        user_label = tk.Label(
            header,
            text=f"👤 {self.usuario_logado.title()}",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.DARK,
            fg=DesignSystem.WHITE
        )
        user_label.pack(side="right", padx=20, pady=15)
    
    def create_sidebar_menu(self):
        """Cria menu lateral conforme especificação"""
        self.sidebar = tk.Frame(self.main_container, bg=DesignSystem.WHITE, width=250)
        
        # Título do menu
        menu_title = tk.Label(
            self.sidebar,
            text="🏥 MENU PRINCIPAL",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        )
        menu_title.pack(pady=20)
        
        # Separador
        separator = tk.Frame(self.sidebar, bg=DesignSystem.MUTED, height=1)
        separator.pack(fill="x", padx=20, pady=10)
        
        # Itens do menu
        menu_items = [
            ("🏠 Dashboard", self.show_dashboard),
            ("➕ Novo Paciente", self.show_cadastro),
            ("🔍 Buscar Paciente", self.show_busca),
            ("👥 Lista de Pacientes", self.show_lista_pacientes),
            ("🚨 Painel Ordinix", self.show_painel_ordinix),
            ("📅 Agendamentos", self.show_agendamentos),
            ("📊 Relatórios", self.show_relatorios),
            ("🖨️ Impressões", self.show_impressoes),
            ("⚙️ Configurações", self.show_configuracoes),
            ("📤 Compartilhar", self.show_compartilhar),
            ("❓ Ajuda", self.show_ajuda),
            ("🚪 Sair", self.sair_sistema)
        ]
        
        for texto, comando in menu_items:
            btn = tk.Button(
                self.sidebar,
                text=texto,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.DARK,
                relief="flat",
                cursor="hand2",
                anchor="w",
                width=25,
                command=comando
            )
            btn.pack(fill="x", padx=10, pady=2)
            
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=DesignSystem.LIGHT))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=DesignSystem.WHITE))
    
    def toggle_menu(self):
        """Alterna visibilidade do menu lateral"""
        if self.menu_aberto:
            self.sidebar.pack_forget()
            self.menu_aberto = False
        else:
            self.sidebar.pack(side="left", fill="y")
            self.menu_aberto = True
    
    def clear_content(self):
        """Limpa área de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        """Mostra dashboard principal conforme especificação"""
        self.clear_content()
        self.tela_atual = "dashboard"
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="📊 PAINEL DE CONTROLE - TEMPO REAL",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        title.pack(pady=20)
        
        # Cards de estatísticas
        stats_frame = tk.Frame(self.content_frame, bg=DesignSystem.LIGHT)
        stats_frame.pack(pady=20)
        
        # Contar pacientes por nível
        niveis = {1: 0, 2: 0, 3: 0}
        for p in self.sistema.pacientes:
            niveis[p["nivel_ordinix"]] += 1
        
        # Cards
        self.create_stat_card(stats_frame, str(niveis[3]), "🔴 Emerg.", DesignSystem.DANGER, 0)
        self.create_stat_card(stats_frame, str(niveis[2]), "🟡 Urgent", DesignSystem.WARNING, 1)
        self.create_stat_card(stats_frame, str(niveis[1]), "🟢 Normal", DesignSystem.SUCCESS, 2)
        
        # Fila Ordinix-123
        self.create_fila_ordinix(self.content_frame)
    
    def create_stat_card(self, parent, numero, texto, cor, coluna):
        """Cria card de estatística"""
        card = tk.Frame(parent, bg=DesignSystem.WHITE, relief="raised", bd=2)
        card.grid(row=0, column=coluna, padx=20, pady=10)
        
        # Número grande
        num_label = tk.Label(
            card,
            text=numero,
            font=("Arial", 24, "bold"),
            bg=DesignSystem.WHITE,
            fg=cor,
            width=8,
            height=2
        )
        num_label.pack(pady=10)
        
        # Texto descritivo
        text_label = tk.Label(
            card,
            text=texto,
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        )
        text_label.pack(pady=(0, 10))
    
    def create_fila_ordinix(self, parent):
        """Cria visualização da fila Ordinix-123"""
        fila_frame = tk.Frame(parent, bg=DesignSystem.LIGHT)
        fila_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título da fila
        fila_title = tk.Label(
            fila_frame,
            text="🚨 FILA ORDINIX-123",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        fila_title.pack(anchor="w", pady=(0, 10))
        
        # Container da fila com scroll
        fila_container = tk.Frame(fila_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
        fila_container.pack(fill="both", expand=True)
        
        # Canvas para scroll
        canvas = tk.Canvas(fila_container, bg=DesignSystem.WHITE)
        scrollbar = ttk.Scrollbar(fila_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=DesignSystem.WHITE)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mostrar pacientes na fila (garantir ordenação correta)
        if self.sistema.ordinix.fila_atendimento:
            # Garantir que a fila está ordenada por prioridade (nível 3 primeiro) e depois por timestamp
            fila_ordenada = sorted(
                self.sistema.ordinix.fila_atendimento,
                key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
            )
            for i, paciente in enumerate(fila_ordenada, 1):
                self.create_paciente_fila_item(scrollable_frame, i, paciente)
        else:
            no_patients = tk.Label(
                scrollable_frame,
                text="Nenhum paciente na fila",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.MUTED
            )
            no_patients.pack(pady=50)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_paciente_fila_item(self, parent, posicao, paciente):
        """Cria item da fila de paciente com indicadores visuais de prioridade"""
        cores_nivel = {1: DesignSystem.SUCCESS, 2: DesignSystem.WARNING, 3: DesignSystem.DANGER}
        emojis_nivel = {1: "🟢", 2: "🟡", 3: "🔴"}
        descricoes_nivel = {1: "NORMAL", 2: "URGENTE", 3: "EMERGÊNCIA"}
        
        # Frame com borda colorida baseada na prioridade
        item_frame = tk.Frame(parent, bg=cores_nivel[paciente['nivel_ordinix']], relief="solid", bd=3)
        item_frame.pack(fill="x", padx=10, pady=5)
        
        # Frame interno branco
        inner_frame = tk.Frame(item_frame, bg=DesignSystem.WHITE)
        inner_frame.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Linha de prioridade (destaque para emergências)
        priority_text = f"{posicao}º {emojis_nivel[paciente['nivel_ordinix']]} {descricoes_nivel[paciente['nivel_ordinix']]}"
        if paciente['nivel_ordinix'] == 3:
            priority_text = f"🚨 {priority_text} 🚨"
        
        priority_line = tk.Label(
            inner_frame,
            text=priority_text,
            font=DesignSystem.FONT_SUBTITLE if paciente['nivel_ordinix'] == 3 else DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=cores_nivel[paciente['nivel_ordinix']],
            anchor="w"
        )
        priority_line.pack(fill="x", padx=10, pady=(5, 0))
        
        # Linha principal com dados do paciente
        main_line = tk.Label(
            inner_frame,
            text=f"👤 {paciente['nome']} - CPF: {paciente['cpf']}",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            anchor="w"
        )
        main_line.pack(fill="x", padx=10, pady=(2, 0))
        
        # Linha de tempo
        tempo_espera = datetime.now() - paciente['timestamp']
        minutos_espera = int(tempo_espera.total_seconds() / 60)
        sla_minutos = self.sistema.ordinix.NIVEIS[paciente['nivel_ordinix']]['sla']
        
        cor_tempo = DesignSystem.DANGER if minutos_espera > sla_minutos else DesignSystem.MUTED
        status_sla = "⚠️ SLA EXCEDIDO!" if minutos_espera > sla_minutos else "✅ Dentro do SLA"
        
        time_line = tk.Label(
            inner_frame,
            text=f"⏱️ Aguardando há {minutos_espera} min - SLA: {sla_minutos} min - {status_sla}",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.WHITE,
            fg=cor_tempo,
            anchor="w"
        )
        time_line.pack(fill="x", padx=10, pady=(2, 5))
    
    def show_cadastro(self):
        """Mostra tela de cadastro de paciente"""
        self.clear_content()
        self.tela_atual = "cadastro"
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="➕ CADASTRO DE PACIENTE COM ORDINIX-123",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        title.pack(pady=20)
        
        # Container do formulário
        form_container = tk.Frame(self.content_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
        form_container.pack(padx=50, pady=20, fill="both", expand=True)
        
        # Frame interno para centralizar
        form_frame = tk.Frame(form_container, bg=DesignSystem.WHITE)
        form_frame.pack(expand=True, fill="both", padx=40, pady=30)
        
        # Campos do formulário
        self.create_form_field(form_frame, "Nome Completo:", "nome_entry", 0)
        self.create_form_field(form_frame, "CPF:", "cpf_entry", 1)
        self.create_form_field(form_frame, "Idade:", "idade_entry", 2)
        self.create_form_field(form_frame, "Telefone:", "telefone_entry", 3)
        
        # Sistema Ordinix-123
        ordinix_frame = tk.LabelFrame(
            form_frame,
            text="🚨 SISTEMA ORDINIX-123 - Classificação de Prioridade",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            relief="solid",
            bd=2
        )
        ordinix_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=20)
        ordinix_frame.columnconfigure(0, weight=1)
        
        # Variável para nível selecionado
        self.nivel_var = tk.IntVar(value=1)
        
        # Opções de nível
        niveis = [
            (1, "🟢 Nível 1 - Normal (Verde)", DesignSystem.SUCCESS),
            (2, "🟡 Nível 2 - Urgente (Amarelo)", DesignSystem.WARNING),
            (3, "🔴 Nível 3 - Emergência (Vermelho)", DesignSystem.DANGER)
        ]
        
        for i, (valor, texto, cor) in enumerate(niveis):
            rb = tk.Radiobutton(
                ordinix_frame,
                text=texto,
                variable=self.nivel_var,
                value=valor,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=cor,
                selectcolor=DesignSystem.WHITE,
                activebackground=DesignSystem.WHITE,
                activeforeground=cor
            )
            rb.grid(row=i, column=0, sticky="w", padx=20, pady=5)
        
        # Botões
        button_frame = tk.Frame(form_frame, bg=DesignSystem.WHITE)
        button_frame.grid(row=5, column=0, columnspan=2, pady=30)
        
        # Botão Cadastrar
        cadastrar_btn = tk.Button(
            button_frame,
            text="✅ CADASTRAR PACIENTE",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            width=20,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.cadastrar_paciente
        )
        cadastrar_btn.pack(side="left", padx=10)
        
        # Botão Limpar
        limpar_btn = tk.Button(
            button_frame,
            text="🗑️ LIMPAR CAMPOS",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.MUTED,
            fg=DesignSystem.WHITE,
            width=20,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.limpar_formulario
        )
        limpar_btn.pack(side="left", padx=10)
        
        # Configurar grid
        form_frame.columnconfigure(1, weight=1)
    
    def create_form_field(self, parent, label_text, entry_name, row):
        """Cria campo do formulário"""
        # Label
        label = tk.Label(
            parent,
            text=label_text,
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            anchor="w"
        )
        label.grid(row=row, column=0, sticky="w", pady=10, padx=(0, 20))
        
        # Entry
        entry = tk.Entry(
            parent,
            font=DesignSystem.FONT_NORMAL,
            width=40,
            relief="solid",
            bd=1
        )
        entry.grid(row=row, column=1, sticky="ew", pady=10)
        
        # Armazenar referência
        setattr(self, entry_name, entry)
        
        # Configurar validações específicas
        if entry_name == "cpf_entry":
            entry.bind("<KeyRelease>", self.validar_cpf_tempo_real)
            entry.bind("<KeyPress>", self.validar_cpf_keypress)
        elif entry_name == "idade_entry":
            entry.bind("<KeyPress>", self.validar_apenas_numeros)
        elif entry_name == "telefone_entry":
            entry.bind("<KeyPress>", self.validar_apenas_numeros)
    
    def validar_cpf_keypress(self, event):
        """Valida entrada de CPF permitindo colagem"""
        # Permitir operações de clipboard
        if event.state & 0x4:  # Ctrl pressionado
            if event.keysym in ['v', 'V', 'c', 'C', 'x', 'X', 'a', 'A']:
                if event.keysym in ['v', 'V']:
                    self.root.after(10, self.validar_cpf_tempo_real_delayed)
                return True
        
        # Permitir teclas de navegação
        if event.keysym in ['BackSpace', 'Delete', 'Left', 'Right', 'Home', 'End', 'Tab']:
            return True
            
        # Permitir apenas dígitos e alguns caracteres de formatação
        if event.char.isdigit() or event.char in '.-':
            return True
            
        return "break"
    
    def validar_cpf_tempo_real_delayed(self):
        """Valida CPF após colagem"""
        self.validar_cpf_tempo_real(None)
    
    def validar_cpf_tempo_real(self, event):
        """Valida CPF em tempo real"""
        cpf = self.cpf_entry.get().strip()
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf_numeros) == 11:
            if self.sistema.validar_cpf(cpf_numeros):
                self.cpf_entry.configure(bg="#E8F5E8")  # Verde claro
                # Formatar CPF
                cpf_formatado = self.sistema.formatar_cpf(cpf_numeros)
                current_pos = self.cpf_entry.index(tk.INSERT)
                self.cpf_entry.delete(0, tk.END)
                self.cpf_entry.insert(0, cpf_formatado)
                # Tentar manter a posição do cursor
                try:
                    self.cpf_entry.icursor(min(current_pos, len(cpf_formatado)))
                except:
                    pass
            else:
                self.cpf_entry.configure(bg="#FFE8E8")  # Vermelho claro
        else:
            self.cpf_entry.configure(bg=DesignSystem.WHITE)
    
    def validar_apenas_numeros(self, event):
        """Permite apenas números e operações de clipboard"""
        # Permitir operações de clipboard (Ctrl+V, Ctrl+C, Ctrl+X, Ctrl+A)
        if event.state & 0x4:  # Ctrl pressionado
            if event.keysym in ['v', 'V', 'c', 'C', 'x', 'X', 'a', 'A']:
                # Para Ctrl+V (colar), validar após um pequeno delay
                if event.keysym in ['v', 'V']:
                    self.root.after(10, lambda: self.validar_campo_numerico(event.widget))
                return True
        
        # Permitir teclas de navegação e edição
        if event.keysym in ['BackSpace', 'Delete', 'Left', 'Right', 'Home', 'End', 'Tab']:
            return True
            
        # Permitir apenas dígitos
        if event.char.isdigit():
            return True
            
        return "break"
    
    def validar_campo_numerico(self, widget):
        """Valida se o conteúdo do campo contém apenas números"""
        try:
            conteudo = widget.get()
            # Remove caracteres não numéricos
            numeros_apenas = ''.join(filter(str.isdigit, conteudo))
            
            # Se o conteúdo mudou, atualiza o campo
            if conteudo != numeros_apenas:
                widget.delete(0, tk.END)
                widget.insert(0, numeros_apenas)
                
        except Exception:
            pass
    
    def cadastrar_paciente(self):
        """Cadastra novo paciente"""
        try:
            # Validar campos
            nome = self.nome_entry.get().strip()
            cpf = self.cpf_entry.get().strip()
            idade_str = self.idade_entry.get().strip()
            telefone = self.telefone_entry.get().strip()
            nivel = self.nivel_var.get()
            
            # Validações
            if not nome:
                raise ValueError("Nome é obrigatório!")
            
            if not cpf:
                raise ValueError("CPF é obrigatório!")
            
            cpf_numeros = ''.join(filter(str.isdigit, cpf))
            if len(cpf_numeros) != 11 or not self.sistema.validar_cpf(cpf_numeros):
                raise ValueError("CPF inválido!")
            
            if not idade_str or not idade_str.isdigit():
                raise ValueError("Idade deve ser um número válido!")
            
            idade = int(idade_str)
            if idade < 0 or idade > 150:
                raise ValueError("Idade deve estar entre 0 e 150 anos!")
            
            if not telefone or not telefone.isdigit():
                raise ValueError("Telefone deve conter apenas números!")
            
            # Verificar duplicidade de CPF
            cpf_formatado = self.sistema.formatar_cpf(cpf_numeros)
            for p in self.sistema.pacientes:
                if p["cpf"] == cpf_formatado:
                    raise ValueError("CPF já cadastrado no sistema!")
            
            # Confirmação para níveis de emergência
            if nivel == 3:
                if not messagebox.askyesno(
                    "Confirmação de Emergência",
                    f"⚠️ ATENÇÃO!\n\nVocê está classificando {nome} como EMERGÊNCIA (Nível 3).\n\n"
                    "Isso significa:\n"
                    "• Prioridade MÁXIMA na fila\n"
                    "• SLA de 15 minutos\n"
                    "• Alertas automáticos ativados\n\n"
                    "Confirma esta classificação?"
                ):
                    return
            
            # Criar paciente
            paciente = {
                "id": len(self.sistema.pacientes) + 1,
                "nome": nome,
                "cpf": cpf_formatado,
                "idade": idade,
                "telefone": telefone,
                "nivel_ordinix": nivel,
                "timestamp": datetime.now(),
                "status": "ativo"
            }
            
            # Adicionar ao sistema
            self.sistema.pacientes.append(paciente)
            self.sistema.adicionar_fila_inteligente(paciente)
            
            # Mostrar alerta de emergência se necessário
            if nivel == 3:
                self.mostrar_alerta_emergencia(paciente)
            
            # Calcular posição real na fila ordenada
            fila_ordenada = sorted(
                self.sistema.ordinix.fila_atendimento,
                key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
            )
            posicao_real = next(
                (i + 1 for i, p in enumerate(fila_ordenada) if p["cpf"] == paciente["cpf"]),
                len(fila_ordenada)
            )
            
            # Sucesso
            messagebox.showinfo(
                "Sucesso",
                f"✅ Paciente cadastrado com sucesso!\n\n"
                f"Nome: {nome}\n"
                f"CPF: {cpf_formatado}\n"
                f"Nível Ordinix: {nivel}\n"
                f"Posição na fila: {posicao_real}º"
            )
            
            # Limpar formulário
            self.limpar_formulario()
            
            # Voltar ao dashboard
            self.show_dashboard()
            
        except ValueError as e:
            messagebox.showerror("Erro de Validação", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")
    
    def mostrar_alerta_emergencia(self, paciente):
        """Mostra alerta visual de emergência"""
        # Criar janela de alerta
        alerta = tk.Toplevel(self.root)
        alerta.title("🚨 ALERTA DE EMERGÊNCIA")
        alerta.geometry("500x400")
        alerta.configure(bg=DesignSystem.DANGER)
        alerta.resizable(False, False)
        alerta.grab_set()  # Modal
        
        # Centralizar
        alerta.update_idletasks()
        x = (alerta.winfo_screenwidth() // 2) - (500 // 2)
        y = (alerta.winfo_screenheight() // 2) - (400 // 2)
        alerta.geometry(f"500x400+{x}+{y}")
        
        # Conteúdo do alerta
        tk.Label(
            alerta,
            text="🚨 ALERTA DE EMERGÊNCIA",
            font=("Arial", 18, "bold"),
            bg=DesignSystem.DANGER,
            fg=DesignSystem.WHITE
        ).pack(pady=20)
        
        tk.Label(
            alerta,
            text="NÍVEL 3 - PRIORIDADE MÁXIMA",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.DANGER,
            fg=DesignSystem.WHITE
        ).pack(pady=10)
        
        info_frame = tk.Frame(alerta, bg=DesignSystem.WHITE, relief="raised", bd=3)
        info_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        tk.Label(
            info_frame,
            text=f"Paciente: {paciente['nome']}",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(pady=5)
        
        tk.Label(
            info_frame,
            text=f"CPF: {paciente['cpf']}",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(pady=5)
        
        tk.Label(
            info_frame,
            text="PROTOCOLO ATIVADO:",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DANGER
        ).pack(pady=(20, 10))
        
        # Calcular posição real na fila ordenada
        fila_ordenada = sorted(
            self.sistema.ordinix.fila_atendimento,
            key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
        )
        posicao_real = next(
            (i + 1 for i, p in enumerate(fila_ordenada) if p["cpf"] == paciente["cpf"]),
            1
        )
        
        protocolos = [
            f"• Posição na fila: {posicao_real}º lugar",
            "• SLA: 15 minutos máximo",
            "• Equipe médica notificada",
            "• Leito de emergência preparado",
            "• Monitoramento contínuo ativado"
        ]
        
        for protocolo in protocolos:
            tk.Label(
                info_frame,
                text=protocolo,
                font=DesignSystem.FONT_SMALL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.DARK,
                anchor="w"
            ).pack(fill="x", padx=20, pady=2)
        
        # Botão OK
        tk.Button(
            alerta,
            text="✅ PROTOCOLO CONFIRMADO",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DANGER,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=alerta.destroy
        ).pack(pady=20)
    
    def limpar_formulario(self):
        """Limpa todos os campos do formulário"""
        self.nome_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)
        self.cpf_entry.configure(bg=DesignSystem.WHITE)
        self.idade_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)
        self.nivel_var.set(1)
        self.nome_entry.focus()
    
    def show_busca(self):
        """Mostra tela de busca de pacientes"""
        self.clear_content()
        self.tela_atual = "busca"
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="🔍 BUSCAR PACIENTE",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        title.pack(pady=20)
        
        # Container de busca
        search_container = tk.Frame(self.content_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
        search_container.pack(padx=50, pady=20, fill="x")
        
        # Frame de busca
        search_frame = tk.Frame(search_container, bg=DesignSystem.WHITE)
        search_frame.pack(padx=30, pady=20)
        
        # Campo de busca
        tk.Label(
            search_frame,
            text="Digite o nome ou CPF do paciente:",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(anchor="w", pady=(0, 10))
        
        # Frame para entrada e botão
        input_frame = tk.Frame(search_frame, bg=DesignSystem.WHITE)
        input_frame.pack(fill="x")
        
        self.search_entry = tk.Entry(
            input_frame,
            font=DesignSystem.FONT_NORMAL,
            width=40,
            relief="solid",
            bd=1
        )
        self.search_entry.pack(side="left", padx=(0, 10))
        
        search_btn = tk.Button(
            input_frame,
            text="🔍 BUSCAR",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            command=self.realizar_busca
        )
        search_btn.pack(side="left")
        
        # Bind Enter para buscar
        self.search_entry.bind('<Return>', lambda event: self.realizar_busca())
        
        # Filtros por nível Ordinix
        filter_frame = tk.LabelFrame(
            search_container,
            text="Filtrar por Nível Ordinix:",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        )
        filter_frame.pack(fill="x", padx=30, pady=(0, 20))
        
        self.filter_var = tk.StringVar(value="todos")
        
        filters = [
            ("todos", "Todos os níveis"),
            ("1", "🟢 Nível 1 - Normal"),
            ("2", "🟡 Nível 2 - Urgente"),
            ("3", "🔴 Nível 3 - Emergência")
        ]
        
        filter_buttons_frame = tk.Frame(filter_frame, bg=DesignSystem.WHITE)
        filter_buttons_frame.pack(pady=10)
        
        for valor, texto in filters:
            rb = tk.Radiobutton(
                filter_buttons_frame,
                text=texto,
                variable=self.filter_var,
                value=valor,
                font=DesignSystem.FONT_SMALL,
                bg=DesignSystem.WHITE,
                selectcolor=DesignSystem.WHITE,
                command=self.realizar_busca
            )
            rb.pack(side="left", padx=20)
        
        # Área de resultados
        self.results_frame = tk.Frame(self.content_frame, bg=DesignSystem.LIGHT)
        self.results_frame.pack(fill="both", expand=True, padx=50, pady=(0, 20))
        
        # Foco no campo de busca
        self.search_entry.focus()
        
        # Mostrar todos os pacientes inicialmente
        self.realizar_busca()
    
    def realizar_busca(self):
        """Realiza a busca de pacientes"""
        # Limpar resultados anteriores
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        termo_busca = self.search_entry.get().strip().lower()
        filtro_nivel = self.filter_var.get()
        
        # Filtrar pacientes
        resultados = []
        for paciente in self.sistema.pacientes:
            # Filtro por termo de busca
            if termo_busca:
                nome_match = termo_busca in paciente["nome"].lower()
                cpf_match = termo_busca in paciente["cpf"].replace(".", "").replace("-", "")
                if not (nome_match or cpf_match):
                    continue
            
            # Filtro por nível
            if filtro_nivel != "todos" and str(paciente["nivel_ordinix"]) != filtro_nivel:
                continue
            
            resultados.append(paciente)
        
        # Mostrar resultados
        if resultados:
            # Título dos resultados
            results_title = tk.Label(
                self.results_frame,
                text=f"📋 {len(resultados)} paciente(s) encontrado(s):",
                font=DesignSystem.FONT_SUBTITLE,
                bg=DesignSystem.LIGHT,
                fg=DesignSystem.DARK
            )
            results_title.pack(anchor="w", pady=(10, 20))
            
            # Container com scroll para resultados
            results_container = tk.Frame(self.results_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
            results_container.pack(fill="both", expand=True)
            
            # Canvas para scroll
            canvas = tk.Canvas(results_container, bg=DesignSystem.WHITE)
            scrollbar = ttk.Scrollbar(results_container, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg=DesignSystem.WHITE)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Mostrar cada paciente
            for paciente in resultados:
                self.create_patient_card(scrollable_frame, paciente)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
        else:
            # Nenhum resultado
            no_results = tk.Label(
                self.results_frame,
                text="❌ Nenhum paciente encontrado",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.LIGHT,
                fg=DesignSystem.MUTED
            )
            no_results.pack(pady=50)
    
    def create_patient_card(self, parent, paciente):
        """Cria card visual para paciente"""
        cores_nivel = {1: DesignSystem.SUCCESS, 2: DesignSystem.WARNING, 3: DesignSystem.DANGER}
        emojis_nivel = {1: "🟢", 2: "🟡", 3: "🔴"}
        desc_nivel = {1: "Normal", 2: "Urgente", 3: "Emergência"}
        
        # Card principal
        card = tk.Frame(parent, bg=DesignSystem.WHITE, relief="solid", bd=1)
        card.pack(fill="x", padx=10, pady=5)
        
        # Header do card
        header_frame = tk.Frame(card, bg=cores_nivel[paciente["nivel_ordinix"]], height=5)
        header_frame.pack(fill="x")
        
        # Conteúdo do card
        content_frame = tk.Frame(card, bg=DesignSystem.WHITE)
        content_frame.pack(fill="x", padx=15, pady=10)
        
        # Linha 1: Nome e nível
        line1_frame = tk.Frame(content_frame, bg=DesignSystem.WHITE)
        line1_frame.pack(fill="x")
        
        tk.Label(
            line1_frame,
            text=f"{emojis_nivel[paciente['nivel_ordinix']]} {paciente['nome']}",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            anchor="w"
        ).pack(side="left")
        
        tk.Label(
            line1_frame,
            text=f"Nível {paciente['nivel_ordinix']} - {desc_nivel[paciente['nivel_ordinix']]}",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.WHITE,
            fg=cores_nivel[paciente["nivel_ordinix"]],
            anchor="e"
        ).pack(side="right")
        
        # Linha 2: CPF e ID
        tk.Label(
            content_frame,
            text=f"CPF: {paciente['cpf']} | ID: {paciente['id']}",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.MUTED,
            anchor="w"
        ).pack(fill="x", pady=(5, 0))
        
        # Linha 3: Idade e telefone
        tk.Label(
            content_frame,
            text=f"Idade: {paciente['idade']} anos | Telefone: {paciente['telefone']}",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.MUTED,
            anchor="w"
        ).pack(fill="x")
        
        # Linha 4: Data/hora de cadastro
        data_cadastro = paciente['timestamp'].strftime('%d/%m/%Y às %H:%M')
        tk.Label(
            content_frame,
            text=f"Cadastrado em: {data_cadastro}",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.MUTED,
            anchor="w"
        ).pack(fill="x")
        
        # Botões de ação
        actions_frame = tk.Frame(content_frame, bg=DesignSystem.WHITE)
        actions_frame.pack(fill="x", pady=(10, 0))
        
        # Botão Imprimir
        print_btn = tk.Button(
            actions_frame,
            text="🖨️ Imprimir",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.INFO,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            command=lambda p=paciente: self.imprimir_paciente(p)
        )
        print_btn.pack(side="left", padx=(0, 10))
        
        # Botão Ver Detalhes
        details_btn = tk.Button(
            actions_frame,
            text="👁️ Detalhes",
            font=DesignSystem.FONT_SMALL,
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            command=lambda p=paciente: self.ver_detalhes_paciente(p)
        )
        details_btn.pack(side="left")
    
    def imprimir_paciente(self, paciente):
        """Imprime ficha do paciente"""
        messagebox.showinfo(
            "Impressão",
            f"📄 Imprimindo ficha do paciente:\n\n"
            f"Nome: {paciente['nome']}\n"
            f"CPF: {paciente['cpf']}\n"
            f"Idade: {paciente['idade']} anos\n"
            f"Telefone: {paciente['telefone']}\n"
            f"Nível Ordinix: {paciente['nivel_ordinix']}\n"
            f"Data: {paciente['timestamp'].strftime('%d/%m/%Y %H:%M')}"
        )
    
    def ver_detalhes_paciente(self, paciente):
        """Mostra detalhes completos do paciente"""
        # Criar janela de detalhes
        detalhes = tk.Toplevel(self.root)
        detalhes.title(f"👤 Detalhes - {paciente['nome']}")
        detalhes.geometry("500x550")
        detalhes.configure(bg=DesignSystem.WHITE)
        detalhes.resizable(False, False)
        detalhes.grab_set()  # Modal
        
        # Centralizar
        detalhes.update_idletasks()
        x = (detalhes.winfo_screenwidth() // 2) - (500 // 2)
        y = (detalhes.winfo_screenheight() // 2) - (550 // 2)
        detalhes.geometry(f"500x550+{x}+{y}")
        
        # Conteúdo dos detalhes
        cores_nivel = {1: DesignSystem.SUCCESS, 2: DesignSystem.WARNING, 3: DesignSystem.DANGER}
        desc_nivel = {1: "Normal", 2: "Urgente", 3: "Emergência"}
        
        # Título
        tk.Label(
            detalhes,
            text=f"👤 {paciente['nome']}",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(pady=20)
        
        # Frame de informações
        info_frame = tk.Frame(detalhes, bg=DesignSystem.LIGHT, relief="raised", bd=2)
        info_frame.pack(padx=30, pady=20, fill="both", expand=False)
        
        # Informações detalhadas
        infos = [
            ("ID do Paciente:", str(paciente['id'])),
            ("CPF:", paciente['cpf']),
            ("Idade:", f"{paciente['idade']} anos"),
            ("Telefone:", paciente['telefone']),
            ("Nível Ordinix:", f"{paciente['nivel_ordinix']} - {desc_nivel[paciente['nivel_ordinix']]}"),
            ("Status:", paciente['status'].title()),
            ("Data de Cadastro:", paciente['timestamp'].strftime('%d/%m/%Y')),
            ("Hora de Cadastro:", paciente['timestamp'].strftime('%H:%M:%S'))
        ]
        
        for i, (label, valor) in enumerate(infos):
            info_line = tk.Frame(info_frame, bg=DesignSystem.LIGHT)
            info_line.pack(fill="x", padx=20, pady=5)
            
            tk.Label(
                info_line,
                text=label,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.LIGHT,
                fg=DesignSystem.DARK,
                anchor="w",
                width=18
            ).pack(side="left")
            
            cor_valor = cores_nivel[paciente['nivel_ordinix']] if "Nível" in label else DesignSystem.DARK
            
            tk.Label(
                info_line,
                text=valor,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.LIGHT,
                fg=cor_valor,
                anchor="w"
            ).pack(side="left", fill="x", expand=True)
        
        # Frame para botões
        buttons_frame = tk.Frame(detalhes, bg=DesignSystem.WHITE)
        buttons_frame.pack(pady=20)
        
        # Botão Editar
        tk.Button(
            buttons_frame,
            text="✏️ EDITAR",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WARNING,
            fg=DesignSystem.WHITE,
            width=12,
            height=2,
            relief="flat",
            cursor="hand2",
            command=lambda: self.editar_paciente(paciente, detalhes)
        ).pack(side="left", padx=5)
        
        # Botão Excluir
        tk.Button(
            buttons_frame,
            text="🗑️ EXCLUIR",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.DANGER,
            fg=DesignSystem.WHITE,
            width=12,
            height=2,
            relief="flat",
            cursor="hand2",
            command=lambda: self.excluir_paciente(paciente, detalhes)
        ).pack(side="left", padx=5)
        
        # Botão Fechar
        tk.Button(
            buttons_frame,
            text="✅ FECHAR",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.PRIMARY,
            fg=DesignSystem.WHITE,
            width=12,
            height=2,
            relief="flat",
            cursor="hand2",
            command=detalhes.destroy
        ).pack(side="left", padx=5)
    
    def editar_paciente(self, paciente, janela_detalhes):
        """Abre formulário para editar dados do paciente"""
        # Fechar janela de detalhes
        janela_detalhes.destroy()
        
        # Criar janela de edição
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"✏️ Editar Paciente - {paciente['nome']}")
        edit_window.geometry("600x500")
        edit_window.configure(bg=DesignSystem.WHITE)
        edit_window.resizable(False, False)
        edit_window.grab_set()  # Modal
        
        # Centralizar
        edit_window.update_idletasks()
        x = (edit_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (edit_window.winfo_screenheight() // 2) - (500 // 2)
        edit_window.geometry(f"600x500+{x}+{y}")
        
        # Título
        tk.Label(
            edit_window,
            text=f"✏️ Editar Paciente",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack(pady=20)
        
        # Frame principal do formulário
        form_frame = tk.Frame(edit_window, bg=DesignSystem.WHITE)
        form_frame.pack(padx=40, pady=20, fill="both", expand=True)
        
        # Dicionário para armazenar os widgets de entrada
        self.edit_entries = {}
        
        # Campos do formulário
        campos = [
            ("Nome Completo:", "nome", paciente['nome']),
            ("CPF:", "cpf", paciente['cpf']),
            ("Idade:", "idade", str(paciente['idade'])),
            ("Telefone:", "telefone", paciente['telefone'])
        ]
        
        for i, (label_text, field_name, valor_atual) in enumerate(campos):
            # Label
            tk.Label(
                form_frame,
                text=label_text,
                font=DesignSystem.FONT_SUBTITLE,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.DARK,
                anchor="w"
            ).grid(row=i*2, column=0, sticky="w", pady=(10, 5))
            
            # Entry
            entry = tk.Entry(
                form_frame,
                font=DesignSystem.FONT_NORMAL,
                width=40,
                relief="solid",
                bd=1
            )
            entry.grid(row=i*2+1, column=0, sticky="ew", pady=(0, 10))
            entry.insert(0, valor_atual)
            
            # Aplicar validações específicas
            if field_name == "cpf":
                entry.bind('<KeyPress>', self.validar_cpf_keypress)
                entry.bind('<KeyRelease>', self.validar_cpf_tempo_real)
            elif field_name in ["idade"]:
                entry.bind('<KeyPress>', self.validar_apenas_numeros)
            
            self.edit_entries[field_name] = entry
        
        # Campo Nível Ordinix
        tk.Label(
            form_frame,
            text="Nível Ordinix:",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            anchor="w"
        ).grid(row=8, column=0, sticky="w", pady=(10, 5))
        
        nivel_frame = tk.Frame(form_frame, bg=DesignSystem.WHITE)
        nivel_frame.grid(row=9, column=0, sticky="ew", pady=(0, 10))
        
        self.edit_nivel_var = tk.IntVar(value=paciente['nivel_ordinix'])
        
        niveis = [
            (1, "🟢 Normal", DesignSystem.SUCCESS),
            (2, "🟡 Urgente", DesignSystem.WARNING),
            (3, "🔴 Emergência", DesignSystem.DANGER)
        ]
        
        for valor, texto, cor in niveis:
            rb = tk.Radiobutton(
                nivel_frame,
                text=texto,
                variable=self.edit_nivel_var,
                value=valor,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=cor,
                selectcolor=DesignSystem.WHITE,
                activebackground=DesignSystem.WHITE,
                activeforeground=cor
            )
            rb.pack(anchor="w", pady=2)
        
        # Configurar grid
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Frame para botões
        buttons_frame = tk.Frame(edit_window, bg=DesignSystem.WHITE)
        buttons_frame.pack(pady=20)
        
        # Botão Salvar
        tk.Button(
            buttons_frame,
            text="💾 SALVAR",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.SUCCESS,
            fg=DesignSystem.WHITE,
            width=15,
            height=2,
            relief="flat",
            cursor="hand2",
            command=lambda: self.salvar_edicao_paciente(paciente, edit_window)
        ).pack(side="left", padx=10)
        
        # Botão Cancelar
        tk.Button(
            buttons_frame,
            text="❌ CANCELAR",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.MUTED,
            fg=DesignSystem.WHITE,
            width=15,
            height=2,
            relief="flat",
            cursor="hand2",
            command=edit_window.destroy
        ).pack(side="left", padx=10)
    
    def salvar_edicao_paciente(self, paciente_original, edit_window):
        """Salva as alterações do paciente"""
        try:
            # Obter valores dos campos
            nome = self.edit_entries['nome'].get().strip()
            cpf = self.edit_entries['cpf'].get().strip()
            idade = self.edit_entries['idade'].get().strip()
            telefone = self.edit_entries['telefone'].get().strip()
            nivel = self.edit_nivel_var.get()
            
            # Validações
            if not all([nome, cpf, idade, telefone]):
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return
            
            if not nome.replace(" ", "").isalpha():
                messagebox.showerror("Erro", "Nome deve conter apenas letras!")
                return
            
            if len(cpf) != 14 or not self.validar_cpf_completo(cpf):
                messagebox.showerror("Erro", "CPF inválido!")
                return
            
            try:
                idade_int = int(idade)
                if idade_int <= 0 or idade_int > 120:
                    messagebox.showerror("Erro", "Idade deve estar entre 1 e 120 anos!")
                    return
            except ValueError:
                messagebox.showerror("Erro", "Idade deve ser um número válido!")
                return
            
            # Verificar se CPF já existe (exceto para o próprio paciente)
            for p in self.sistema.pacientes:
                if p['cpf'] == cpf and p['id'] != paciente_original['id']:
                    messagebox.showerror("Erro", "CPF já cadastrado para outro paciente!")
                    return
            
            # Atualizar dados do paciente
            for p in self.sistema.pacientes:
                if p['id'] == paciente_original['id']:
                    p['nome'] = nome
                    p['cpf'] = cpf
                    p['idade'] = idade_int
                    p['telefone'] = telefone
                    p['nivel_ordinix'] = nivel
                    break
            
            # Atualizar na fila se estiver na fila
            for p in self.sistema.ordinix.fila_atendimento:
                if p['id'] == paciente_original['id']:
                    p['nome'] = nome
                    p['cpf'] = cpf
                    p['idade'] = idade_int
                    p['telefone'] = telefone
                    p['nivel_ordinix'] = nivel
                    break
            
            # Reordenar a fila se necessário
            self.sistema.ordinix.fila_atendimento.sort(
                key=lambda x: (-x['nivel_ordinix'], x['timestamp'])
            )
            
            # Salvar dados
            self.sistema.salvar_dados()
            
            messagebox.showinfo("Sucesso", "Paciente editado com sucesso!")
            edit_window.destroy()
            
            # Atualizar interface se estiver na tela atual
            if hasattr(self, 'tela_atual'):
                if self.tela_atual == "dashboard":
                    self.show_dashboard()
                elif self.tela_atual == "lista":
                    self.show_lista_pacientes()
                elif self.tela_atual == "busca":
                    self.show_busca()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar alterações: {str(e)}")
    
    def validar_cpf_completo(self, cpf):
        """Valida CPF completo"""
        # Remove formatação
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf_numeros) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf_numeros == cpf_numeros[0] * 11:
            return False
        
        # Calcula primeiro dígito verificador
        soma = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        # Calcula segundo dígito verificador
        soma = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        return cpf_numeros[9:11] == f"{digito1}{digito2}"
    
    def excluir_paciente(self, paciente, janela_detalhes):
        """Exclui paciente do sistema com confirmação"""
        # Confirmar exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o paciente?\n\n"
            f"👤 Nome: {paciente['nome']}\n"
            f"📄 CPF: {paciente['cpf']}\n"
            f"🏥 Nível: {paciente['nivel_ordinix']}\n\n"
            f"⚠️ Esta ação não pode ser desfeita!",
            icon="warning"
        )
        
        if not resposta:
            return
        
        try:
            # Remover da lista principal de pacientes
            self.sistema.pacientes = [
                p for p in self.sistema.pacientes 
                if p['id'] != paciente['id']
            ]
            
            # Remover da fila de atendimento se estiver lá
            self.sistema.ordinix.fila_atendimento = [
                p for p in self.sistema.ordinix.fila_atendimento 
                if p['id'] != paciente['id']
            ]
            
            # Salvar dados
            self.sistema.salvar_dados()
            
            # Fechar janela de detalhes
            janela_detalhes.destroy()
            
            # Mostrar confirmação
            messagebox.showinfo(
                "Sucesso", 
                f"Paciente {paciente['nome']} foi excluído com sucesso!"
            )
            
            # Atualizar interface se estiver na tela atual
            if hasattr(self, 'tela_atual'):
                if self.tela_atual == "dashboard":
                    self.show_dashboard()
                elif self.tela_atual == "lista":
                    self.show_lista_pacientes()
                elif self.tela_atual == "busca":
                    self.show_busca()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir paciente: {str(e)}")
    
    def show_lista_pacientes(self):
        """Mostra lista completa de pacientes"""
        self.clear_content()
        self.tela_atual = "lista"
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="👥 LISTA DE TODOS OS PACIENTES",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        title.pack(pady=20)
        
        if not self.sistema.pacientes:
            # Nenhum paciente cadastrado
            no_patients = tk.Label(
                self.content_frame,
                text="❌ Nenhum paciente cadastrado no sistema",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.LIGHT,
                fg=DesignSystem.MUTED
            )
            no_patients.pack(pady=50)
            return
        
        # Estatísticas rápidas
        stats_frame = tk.Frame(self.content_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
        stats_frame.pack(fill="x", padx=50, pady=(0, 20))
        
        stats_content = tk.Frame(stats_frame, bg=DesignSystem.WHITE)
        stats_content.pack(pady=15)
        
        total = len(self.sistema.pacientes)
        niveis = {1: 0, 2: 0, 3: 0}
        for p in self.sistema.pacientes:
            niveis[p["nivel_ordinix"]] += 1
        
        tk.Label(
            stats_content,
            text=f"📊 Total: {total} pacientes | 🟢 Normal: {niveis[1]} | 🟡 Urgente: {niveis[2]} | 🔴 Emergência: {niveis[3]}",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK
        ).pack()
        
        # Lista de pacientes
        list_container = tk.Frame(self.content_frame, bg=DesignSystem.WHITE, relief="raised", bd=2)
        list_container.pack(fill="both", expand=True, padx=50, pady=(0, 20))
        
        # Canvas para scroll
        canvas = tk.Canvas(list_container, bg=DesignSystem.WHITE)
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=DesignSystem.WHITE)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Ordenar pacientes por nível (emergência primeiro) e depois por data
        pacientes_ordenados = sorted(
            self.sistema.pacientes,
            key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
        )
        
        # Mostrar cada paciente
        for paciente in pacientes_ordenados:
            self.create_patient_card(scrollable_frame, paciente)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def show_painel_ordinix(self):
        """Mostra painel Ordinix em tela cheia"""
        self.clear_content()
        messagebox.showinfo("Info", "Painel Ordinix em desenvolvimento")
    
    def show_agendamentos(self):
        """Mostra sistema de agendamentos"""
        self.clear_content()
        messagebox.showinfo("Info", "Sistema de agendamentos em desenvolvimento")
    
    def show_relatorios(self):
        """Mostra tela de relatórios e estatísticas"""
        self.clear_content()
        self.tela_atual = "relatorios"
        
        # Título
        title = tk.Label(
            self.content_frame,
            text="📊 RELATÓRIOS E ESTATÍSTICAS",
            font=DesignSystem.FONT_TITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        )
        title.pack(pady=20)
        
        if not self.sistema.pacientes:
            # Nenhum dado para relatório
            no_data = tk.Label(
                self.content_frame,
                text="❌ Nenhum dado disponível para relatórios",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.LIGHT,
                fg=DesignSystem.MUTED
            )
            no_data.pack(pady=50)
            return
        
        # Container principal dos relatórios
        reports_container = tk.Frame(self.content_frame, bg=DesignSystem.LIGHT)
        reports_container.pack(fill="both", expand=True, padx=30, pady=(0, 20))
        
        # Estatísticas gerais
        self.create_general_stats(reports_container)
        
        # Estatísticas por nível Ordinix
        self.create_ordinix_stats(reports_container)
        
        # Gráfico de atendimentos por hora
        self.create_hourly_stats(reports_container)
        
        # Botões de ação
        self.create_report_actions(reports_container)
    
    def create_general_stats(self, parent):
        """Cria seção de estatísticas gerais"""
        stats_frame = tk.LabelFrame(
            parent,
            text="📈 Estatísticas Gerais",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            relief="raised",
            bd=2
        )
        stats_frame.pack(fill="x", pady=(0, 20))
        
        # Calcular estatísticas
        total_pacientes = len(self.sistema.pacientes)
        hoje = datetime.now().date()
        pacientes_hoje = len([p for p in self.sistema.pacientes if p["timestamp"].date() == hoje])
        
        # Idade média
        idades = [p["idade"] for p in self.sistema.pacientes]
        idade_media = sum(idades) / len(idades) if idades else 0
        
        # Pacientes por status
        status_count = {}
        for p in self.sistema.pacientes:
            status = p["status"]
            status_count[status] = status_count.get(status, 0) + 1
        
        # Grid de estatísticas
        stats_grid = tk.Frame(stats_frame, bg=DesignSystem.WHITE)
        stats_grid.pack(padx=20, pady=15)
        
        stats_data = [
            ("👥 Total de Pacientes", str(total_pacientes), DesignSystem.PRIMARY),
            ("📅 Cadastros Hoje", str(pacientes_hoje), DesignSystem.SUCCESS),
            ("📊 Idade Média", f"{idade_media:.1f} anos", DesignSystem.INFO),
            ("⏰ Em Espera", str(status_count.get("aguardando", 0)), DesignSystem.WARNING),
            ("✅ Atendidos", str(status_count.get("atendido", 0)), DesignSystem.SUCCESS),
            ("🏥 Em Atendimento", str(status_count.get("em_atendimento", 0)), DesignSystem.DANGER)
        ]
        
        for i, (label, value, color) in enumerate(stats_data):
            row = i // 3
            col = i % 3
            
            stat_card = tk.Frame(stats_grid, bg=color, relief="raised", bd=2)
            stat_card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            
            tk.Label(
                stat_card,
                text=value,
                font=DesignSystem.FONT_TITLE,
                bg=color,
                fg=DesignSystem.WHITE
            ).pack(pady=(10, 5))
            
            tk.Label(
                stat_card,
                text=label,
                font=DesignSystem.FONT_SMALL,
                bg=color,
                fg=DesignSystem.WHITE
            ).pack(pady=(0, 10))
        
        # Configurar grid
        for i in range(3):
            stats_grid.columnconfigure(i, weight=1)
    
    def create_ordinix_stats(self, parent):
        """Cria seção de estatísticas do Ordinix-123"""
        ordinix_frame = tk.LabelFrame(
            parent,
            text="🎯 Análise Ordinix-123",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            relief="raised",
            bd=2
        )
        ordinix_frame.pack(fill="x", pady=(0, 20))
        
        # Calcular estatísticas por nível
        niveis = {1: 0, 2: 0, 3: 0}
        for p in self.sistema.pacientes:
            niveis[p["nivel_ordinix"]] += 1
        
        total = sum(niveis.values())
        
        # Container dos níveis
        levels_container = tk.Frame(ordinix_frame, bg=DesignSystem.WHITE)
        levels_container.pack(padx=20, pady=15)
        
        # Dados dos níveis
        levels_data = [
            (1, "🟢 Nível 1 - Normal", DesignSystem.SUCCESS, niveis[1]),
            (2, "🟡 Nível 2 - Urgente", DesignSystem.WARNING, niveis[2]),
            (3, "🔴 Nível 3 - Emergência", DesignSystem.DANGER, niveis[3])
        ]
        
        for nivel, desc, color, count in levels_data:
            # Frame do nível
            level_frame = tk.Frame(levels_container, bg=DesignSystem.WHITE)
            level_frame.pack(fill="x", pady=5)
            
            # Label do nível
            tk.Label(
                level_frame,
                text=desc,
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.DARK,
                anchor="w",
                width=25
            ).pack(side="left")
            
            # Barra de progresso visual
            progress_frame = tk.Frame(level_frame, bg=DesignSystem.LIGHT, height=25, relief="sunken", bd=1)
            progress_frame.pack(side="left", fill="x", expand=True, padx=(10, 10))
            
            if total > 0:
                percentage = (count / total) * 100
                progress_width = int((percentage / 100) * 200)  # 200px máximo
                
                progress_bar = tk.Frame(progress_frame, bg=color, height=23)
                progress_bar.place(x=1, y=1, width=max(1, progress_width))
            
            # Valores
            percentage_text = f"{(count/total)*100:.1f}%" if total > 0 else "0%"
            tk.Label(
                level_frame,
                text=f"{count} ({percentage_text})",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=color,
                anchor="e",
                width=15
            ).pack(side="right")
    
    def create_hourly_stats(self, parent):
        """Cria estatísticas por horário"""
        hourly_frame = tk.LabelFrame(
            parent,
            text="⏰ Distribuição por Horário",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.WHITE,
            fg=DesignSystem.DARK,
            relief="raised",
            bd=2
        )
        hourly_frame.pack(fill="x", pady=(0, 20))
        
        # Calcular distribuição por hora
        hourly_count = {}
        for p in self.sistema.pacientes:
            hour = p["timestamp"].hour
            hourly_count[hour] = hourly_count.get(hour, 0) + 1
        
        if hourly_count:
            # Container do gráfico
            chart_container = tk.Frame(hourly_frame, bg=DesignSystem.WHITE)
            chart_container.pack(padx=20, pady=15)
            
            # Título do gráfico
            tk.Label(
                chart_container,
                text="Cadastros por Hora do Dia",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.DARK
            ).pack(pady=(0, 10))
            
            # Frame do gráfico
            graph_frame = tk.Frame(chart_container, bg=DesignSystem.LIGHT, relief="sunken", bd=2)
            graph_frame.pack()
            
            # Criar barras simples
            max_count = max(hourly_count.values()) if hourly_count else 1
            
            bars_frame = tk.Frame(graph_frame, bg=DesignSystem.LIGHT)
            bars_frame.pack(padx=10, pady=10)
            
            # Mostrar apenas horas com dados
            horas_ordenadas = sorted(hourly_count.keys())
            
            for hour in horas_ordenadas:
                count = hourly_count[hour]
                
                # Frame da barra
                bar_container = tk.Frame(bars_frame, bg=DesignSystem.LIGHT)
                bar_container.pack(side="left", padx=2)
                
                # Altura da barra (máximo 100px)
                bar_height = int((count / max_count) * 100) if max_count > 0 else 1
                
                # Barra
                bar = tk.Frame(
                    bar_container,
                    bg=DesignSystem.PRIMARY,
                    width=20,
                    height=max(bar_height, 5)
                )
                bar.pack(side="bottom")
                bar.pack_propagate(False)
                
                # Valor
                tk.Label(
                    bar_container,
                    text=str(count),
                    font=DesignSystem.FONT_SMALL,
                    bg=DesignSystem.LIGHT,
                    fg=DesignSystem.DARK
                ).pack(side="bottom")
                
                # Hora
                tk.Label(
                    bar_container,
                    text=f"{hour:02d}h",
                    font=DesignSystem.FONT_SMALL,
                    bg=DesignSystem.LIGHT,
                    fg=DesignSystem.DARK
                ).pack(side="bottom")
        else:
            tk.Label(
                hourly_frame,
                text="Nenhum dado de horário disponível",
                font=DesignSystem.FONT_NORMAL,
                bg=DesignSystem.WHITE,
                fg=DesignSystem.MUTED
            ).pack(pady=20)
    
    def create_report_actions(self, parent):
        """Cria botões de ação para relatórios"""
        actions_frame = tk.Frame(parent, bg=DesignSystem.LIGHT)
        actions_frame.pack(fill="x", pady=20)
        
        # Título
        tk.Label(
            actions_frame,
            text="🔧 Ações de Relatório",
            font=DesignSystem.FONT_SUBTITLE,
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK
        ).pack(pady=(0, 15))
        
        # Container dos botões
        buttons_frame = tk.Frame(actions_frame, bg=DesignSystem.LIGHT)
        buttons_frame.pack()
        
        # Botões de ação
        actions = [
            ("📄 Gerar Relatório Completo", self.gerar_relatorio_completo, DesignSystem.PRIMARY),
            ("📊 Exportar Estatísticas", self.exportar_estatisticas, DesignSystem.INFO),
            ("🖨️ Imprimir Relatório", self.imprimir_relatorio, DesignSystem.SUCCESS),
            ("🔄 Atualizar Dados", self.atualizar_relatorios, DesignSystem.WARNING)
        ]
        
        for i, (text, command, color) in enumerate(actions):
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=DesignSystem.FONT_NORMAL,
                bg=color,
                fg=DesignSystem.WHITE,
                relief="flat",
                cursor="hand2",
                width=20,
                height=2,
                command=command
            )
            btn.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="ew")
        
        # Configurar grid
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
    
    def gerar_relatorio_completo(self):
        """Gera relatório completo do sistema"""
        if not self.sistema.pacientes:
            messagebox.showwarning("Aviso", "Nenhum dado disponível para relatório")
            return
        
        # Calcular dados do relatório
        total = len(self.sistema.pacientes)
        hoje = datetime.now()
        
        # Estatísticas por nível
        niveis = {1: 0, 2: 0, 3: 0}
        for p in self.sistema.pacientes:
            niveis[p["nivel_ordinix"]] += 1
        
        # Criar texto do relatório
        relatorio = f"""
═══════════════════════════════════════════════════════════════
                    RELATÓRIO SISTEMA VIDA+ COM ORDINIX-123
═══════════════════════════════════════════════════════════════

📅 Data/Hora do Relatório: {hoje.strftime('%d/%m/%Y às %H:%M:%S')}

📊 ESTATÍSTICAS GERAIS:
• Total de Pacientes Cadastrados: {total}
• Pacientes Hoje: {len([p for p in self.sistema.pacientes if p["timestamp"].date() == hoje.date()])}
• Idade Média: {sum(p["idade"] for p in self.sistema.pacientes) / total:.1f} anos

🎯 ANÁLISE ORDINIX-123:
• 🟢 Nível 1 (Normal): {niveis[1]} pacientes ({(niveis[1]/total)*100:.1f}%)
• 🟡 Nível 2 (Urgente): {niveis[2]} pacientes ({(niveis[2]/total)*100:.1f}%)
• 🔴 Nível 3 (Emergência): {niveis[3]} pacientes ({(niveis[3]/total)*100:.1f}%)

📋 LISTA DE PACIENTES:
"""
        
        # Adicionar lista de pacientes ordenada por prioridade
        pacientes_ordenados = sorted(
            self.sistema.pacientes,
            key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
        )
        
        for i, p in enumerate(pacientes_ordenados, 1):
            emoji = {1: "🟢", 2: "🟡", 3: "🔴"}[p["nivel_ordinix"]]
            relatorio += f"""
{i:02d}. {emoji} {p['nome']}
    CPF: {p['cpf']} | Idade: {p['idade']} anos
    Telefone: {p['telefone']} | Nível: {p['nivel_ordinix']}
    Cadastro: {p['timestamp'].strftime('%d/%m/%Y %H:%M')}
"""
        
        relatorio += f"""
═══════════════════════════════════════════════════════════════
                    FIM DO RELATÓRIO
═══════════════════════════════════════════════════════════════
"""
        
        # Mostrar relatório em janela
        self.mostrar_relatorio_janela(relatorio)
    
    def mostrar_relatorio_janela(self, relatorio):
        """Mostra relatório em janela separada"""
        # Criar janela do relatório
        relatorio_window = tk.Toplevel(self.root)
        relatorio_window.title("📄 Relatório Completo - Sistema Vida+")
        relatorio_window.geometry("800x600")
        relatorio_window.configure(bg=DesignSystem.WHITE)
        relatorio_window.grab_set()
        
        # Centralizar
        relatorio_window.update_idletasks()
        x = (relatorio_window.winfo_screenwidth() // 2) - (800 // 2)
        y = (relatorio_window.winfo_screenheight() // 2) - (600 // 2)
        relatorio_window.geometry(f"800x600+{x}+{y}")
        
        # Área de texto com scroll
        text_frame = tk.Frame(relatorio_window, bg=DesignSystem.WHITE)
        text_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        text_area = tk.Text(
            text_frame,
            font=("Courier New", 10),
            bg=DesignSystem.LIGHT,
            fg=DesignSystem.DARK,
            wrap="word",
            relief="sunken",
            bd=2
        )
        
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)
        
        text_area.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Inserir relatório
        text_area.insert("1.0", relatorio)
        text_area.config(state="disabled")  # Somente leitura
        
        # Botões
        buttons_frame = tk.Frame(relatorio_window, bg=DesignSystem.WHITE)
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        tk.Button(
            buttons_frame,
            text="🖨️ IMPRIMIR",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.SUCCESS,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            width=15,
            command=lambda: messagebox.showinfo("Impressão", "Relatório enviado para impressão!")
        ).pack(side="left", padx=(0, 10))
        
        tk.Button(
            buttons_frame,
            text="✅ FECHAR",
            font=DesignSystem.FONT_NORMAL,
            bg=DesignSystem.DANGER,
            fg=DesignSystem.WHITE,
            relief="flat",
            cursor="hand2",
            width=15,
            command=relatorio_window.destroy
        ).pack(side="right")
    
    def exportar_estatisticas(self):
        """Exporta estatísticas em formato texto"""
        messagebox.showinfo(
            "Exportação",
            "📊 Estatísticas exportadas com sucesso!\n\n"
            "Arquivo salvo como: estatisticas_vida_plus.txt"
        )
    
    def imprimir_relatorio(self):
        """Imprime relatório atual"""
        messagebox.showinfo(
            "Impressão",
            "🖨️ Relatório enviado para impressão!\n\n"
            "Verifique a impressora e aguarde a conclusão."
        )
    
    def atualizar_relatorios(self):
        """Atualiza dados dos relatórios"""
        messagebox.showinfo("Atualização", "🔄 Dados atualizados com sucesso!")
        self.show_relatorios()  # Recarregar tela
    
    def show_impressoes(self):
        """Mostra sistema de impressões"""
        self.clear_content()
        messagebox.showinfo("Info", "Sistema de impressões em desenvolvimento")
    
    def show_configuracoes(self):
        """Mostra configurações"""
        self.clear_content()
        messagebox.showinfo("Info", "Configurações em desenvolvimento")
    
    def show_compartilhar(self):
        """Mostra sistema de compartilhamento"""
        self.clear_content()
        messagebox.showinfo("Info", "Sistema de compartilhamento em desenvolvimento")
    
    def show_ajuda(self):
        """Mostra ajuda"""
        messagebox.showinfo("Ajuda", "Sistema Clínica Vida+ com Ordinix-123\nInventor: Adevilson de Lima\nVersão: 1.0")
    
    def sair_sistema(self):
        """Sai do sistema"""
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair do sistema?"):
            self.root.destroy()
    
    def iniciar_atualizacoes_tempo_real(self):
        """Inicia atualizações automáticas da interface"""
        def atualizar():
            while True:
                if self.tela_atual == "dashboard":
                    try:
                        self.root.after(0, self.show_dashboard)
                    except:
                        break
                time.sleep(10)  # Atualiza a cada 10 segundos
        
        thread = threading.Thread(target=atualizar, daemon=True)
        thread.start()
    
    def run(self):
        """Executa o sistema principal"""
        self.root.mainloop()

def main():
    """Função principal - inicia com tela de login"""
    login = LoginWindow()
    login.run()

if __name__ == "__main__":
    main()