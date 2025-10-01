# ===== CLÍNICA VIDA+ WEB APP - FLASK BACKEND =====
# Inventor: Adevilson de Lima - Estudante ADS Anhanguera
# Stack Tecnológica Híbrida: Flask + HTML5 + CSS3 + JavaScript

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_socketio import SocketIO, emit
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import threading
import time

# Importar sistema original
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
try:
    from mainColabTeste import SistemaGestaoClinica, SistemaOrdinix123
except ImportError:
    print("Aviso: mainColabTeste não encontrado. Usando sistema mock.")
    
    class SistemaGestaoClinica:
        def __init__(self):
            self.pacientes = []
        
        def cadastrar_paciente(self, dados):
            return True
            
        def buscar_pacientes(self, termo=""):
            return []
            
        def listar_todos_pacientes(self):
            return []
    
    class SistemaOrdinix123:
        def __init__(self):
            pass
        
        def analisar_paciente(self, dados):
            return {"nivel": 2, "prioridade": "Média"}

# Configuração Flask
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')
app.config['SECRET_KEY'] = 'clinica-vida-plus-2025-ordinix-123'
socketio = SocketIO(app, cors_allowed_origins="*")

# Instâncias dos sistemas
sistema_gestao = SistemaGestaoClinica()
sistema_ordinix = SistemaOrdinix123()

# Dados de sessão e cache
usuarios_online = {}
estatisticas_cache = {}

class DesignSystemWeb:
    """Design System adaptado para web"""
    
    COLORS = {
        'primary': '#0066CC',
        'success': '#00CC66', 
        'warning': '#FFCC00',
        'danger': '#FF3333',
        'dark': '#2C3E50',
        'light': '#ECF0F1',
        'info': '#3498DB',
        'muted': '#95A5A6',
        'white': '#FFFFFF'
    }

# ===== ROTAS PRINCIPAIS =====

@app.route('/')
def index():
    """Página inicial - redireciona para login se não autenticado"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        data = request.get_json()
        usuario = data.get('usuario')
        senha = data.get('senha')
        lembrar = data.get('lembrar', False)
        
        # Validação de credenciais
        credenciais_validas = validar_credenciais(usuario, senha)
        
        if credenciais_validas:
            session['usuario'] = usuario
            session['tipo_usuario'] = credenciais_validas['tipo']
            session['nome_completo'] = credenciais_validas['nome']
            
            # Registrar usuário online
            usuarios_online[session.get('session_id', usuario)] = {
                'usuario': usuario,
                'login_time': datetime.now(),
                'tipo': credenciais_validas['tipo']
            }
            
            return jsonify({
                'success': True,
                'redirect': url_for('dashboard'),
                'usuario': credenciais_validas
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Credenciais inválidas'
            }), 401
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard principal"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', 
                         usuario=session.get('usuario'),
                         tipo_usuario=session.get('tipo_usuario'))

@app.route('/cadastro')
def cadastro():
    """Página de cadastro de pacientes"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template('cadastro.html',
                         usuario=session.get('usuario'))

@app.route('/busca')
def busca():
    """Página de busca de pacientes"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template('busca.html',
                         usuario=session.get('usuario'))

@app.route('/lista-pacientes')
def lista_pacientes():
    """Página de lista de pacientes"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template('lista_pacientes.html',
                         usuario=session.get('usuario'))

@app.route('/ordinix')
def ordinix():
    """Página do sistema Ordinix"""
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    return render_template('ordinix.html',
                         usuario=session.get('usuario'))

@app.route('/logout')
def logout():
    """Logout do sistema"""
    # Remover usuário online
    session_id = session.get('session_id', session.get('usuario'))
    if session_id in usuarios_online:
        del usuarios_online[session_id]
    
    session.clear()
    return redirect(url_for('login'))

# ===== APIs REST =====

@app.route('/api/estatisticas')
def api_estatisticas():
    """API para estatísticas do dashboard"""
    if 'usuario' not in session:
        return jsonify({'error': 'Não autorizado'}), 401
    
    try:
        pacientes = sistema_gestao.listar_todos_pacientes()
        
        # Calcular estatísticas
        total_pacientes = len(pacientes)
        pacientes_hoje = len([p for p in pacientes if p.get('data_cadastro', '').startswith(datetime.now().strftime('%Y-%m-%d'))])
        
        # Estatísticas Ordinix
        nivel_1 = len([p for p in pacientes if p.get('nivel_ordinix') == 1])
        nivel_2 = len([p for p in pacientes if p.get('nivel_ordinix') == 2])
        nivel_3 = len([p for p in pacientes if p.get('nivel_ordinix') == 3])
        
        usuarios_online_count = len(usuarios_online)
        
        return jsonify({
            'total_pacientes': total_pacientes,
            'pacientes_hoje': pacientes_hoje,
            'nivel_1': nivel_1,
            'nivel_2': nivel_2,
            'nivel_3': nivel_3,
            'usuarios_online': usuarios_online_count,
            'ultima_atualizacao': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/cadastrar-paciente', methods=['POST'])
def api_cadastrar_paciente():
    """API para cadastrar novo paciente"""
    if 'usuario' not in session:
        return jsonify({'error': 'Não autorizado'}), 401
    
    try:
        dados = request.get_json()
        
        # Validações básicas
        if not dados.get('nome') or not dados.get('cpf'):
            return jsonify({'error': 'Nome e CPF são obrigatórios'}), 400
        
        # Análise Ordinix
        analise_ordinix = sistema_ordinix.analisar_paciente(dados)
        dados['nivel_ordinix'] = analise_ordinix.get('nivel', 2)
        dados['prioridade_ordinix'] = analise_ordinix.get('prioridade', 'Média')
        
        # Adicionar metadados
        dados['data_cadastro'] = datetime.now().isoformat()
        dados['usuario_cadastro'] = session.get('usuario')
        
        # Cadastrar no sistema
        sucesso = sistema_gestao.cadastrar_paciente(dados)
        
        if sucesso:
            # Emitir evento WebSocket
            socketio.emit('novo_paciente', dados, broadcast=True)
            
            return jsonify({
                'success': True,
                'message': 'Paciente cadastrado com sucesso',
                'paciente': dados
            })
        else:
            return jsonify({'error': 'Erro ao cadastrar paciente'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buscar-pacientes')
def api_buscar_pacientes():
    """API para buscar pacientes"""
    if 'usuario' not in session:
        return jsonify({'error': 'Não autorizado'}), 401
    
    try:
        termo = request.args.get('termo', '')
        filtros = {
            'prioridade': request.args.get('prioridade'),
            'genero': request.args.get('genero'),
            'idade_min': request.args.get('idade_min'),
            'idade_max': request.args.get('idade_max'),
            'cidade': request.args.get('cidade')
        }
        
        pacientes = sistema_gestao.buscar_pacientes(termo)
        
        # Aplicar filtros adicionais
        if filtros['prioridade']:
            pacientes = [p for p in pacientes if p.get('nivel_ordinix') == int(filtros['prioridade'])]
        
        if filtros['genero']:
            pacientes = [p for p in pacientes if p.get('genero') == filtros['genero']]
        
        # Filtros de idade, cidade, etc.
        
        return jsonify({
            'pacientes': pacientes,
            'total': len(pacientes)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/listar-pacientes')
def api_listar_pacientes():
    """API para listar todos os pacientes"""
    if 'usuario' not in session:
        return jsonify({'error': 'Não autorizado'}), 401
    
    try:
        pacientes = sistema_gestao.listar_todos_pacientes()
        
        # Paginação
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        start = (page - 1) * per_page
        end = start + per_page
        
        pacientes_paginados = pacientes[start:end]
        
        return jsonify({
            'pacientes': pacientes_paginados,
            'total': len(pacientes),
            'page': page,
            'per_page': per_page,
            'total_pages': (len(pacientes) + per_page - 1) // per_page
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ===== WEBSOCKET EVENTS =====

@socketio.on('connect')
def handle_connect():
    """Usuário conectado via WebSocket"""
    print(f'Cliente conectado: {request.sid}')
    emit('status', {'message': 'Conectado ao sistema'})

@socketio.on('disconnect')
def handle_disconnect():
    """Usuário desconectado"""
    print(f'Cliente desconectado: {request.sid}')

@socketio.on('join_room')
def handle_join_room(data):
    """Usuário entrou em uma sala específica"""
    room = data.get('room', 'geral')
    join_room(room)
    emit('status', {'message': f'Entrou na sala: {room}'})

# ===== FUNÇÕES AUXILIARES =====

def validar_credenciais(usuario, senha):
    """Valida credenciais do usuário"""
    credenciais_file = os.path.join(os.path.dirname(__file__), '..', '..', 'credenciais.json')
    
    try:
        with open(credenciais_file, 'r', encoding='utf-8') as f:
            credenciais = json.load(f)
        
        for cred in credenciais.get('usuarios', []):
            if cred['usuario'] == usuario and cred['senha'] == senha:
                return cred
        
        return None
    
    except FileNotFoundError:
        # Retorna None se arquivo não existir - apenas credenciais do arquivo são válidas
        return None

def carregar_pacientes():
    """Carrega lista de pacientes do arquivo"""
    arquivo_pacientes = os.path.join(os.path.dirname(__file__), '..', '..', 'lista_paciente.txt')
    
    try:
        with open(arquivo_pacientes, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_pacientes(pacientes):
    """Salva lista de pacientes no arquivo"""
    arquivo_pacientes = os.path.join(os.path.dirname(__file__), '..', '..', 'lista_paciente.txt')
    
    with open(arquivo_pacientes, 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=2)

# ===== INICIALIZAÇÃO =====

if __name__ == '__main__':
    print("🏥 CLÍNICA VIDA+ WEB APP - Iniciando servidor...")
    print("📱 Stack: Flask + HTML5 + CSS3 + JavaScript")
    print("🚀 Sistema Ordinix-123 integrado")
    print("🌐 Acesso local: http://localhost:5000")
    print("🔗 Compartilhamento: http://SEU_IP:5000")
    
    socketio.run(app, 
                host='0.0.0.0', 
                port=5000, 
                debug=True,
                allow_unsafe_werkzeug=True)