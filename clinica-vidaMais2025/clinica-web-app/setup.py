#!/usr/bin/env python3
"""
CLÍNICA VIDA+ - Sistema Ordinix-123
Script de Configuração e Inicialização
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class ClinicaSetup:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.python_executable = sys.executable
        self.is_windows = platform.system() == 'Windows'
        
    def print_banner(self):
        """Exibe banner do projeto"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🏥 CLÍNICA VIDA+                          ║
║                  Sistema Ordinix-123                         ║
║                                                              ║
║              Script de Configuração Automática              ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def check_python_version(self):
        """Verifica versão do Python"""
        print("🐍 Verificando versão do Python...")
        
        if sys.version_info < (3, 8):
            print("❌ Python 3.8 ou superior é necessário!")
            print(f"   Versão atual: {sys.version}")
            return False
        
        print(f"✅ Python {sys.version.split()[0]} - OK")
        return True
    
    def create_virtual_environment(self):
        """Cria ambiente virtual"""
        venv_path = self.project_root / 'venv'
        
        if venv_path.exists():
            print("📦 Ambiente virtual já existe")
            return True
        
        print("📦 Criando ambiente virtual...")
        try:
            subprocess.run([
                self.python_executable, '-m', 'venv', str(venv_path)
            ], check=True, capture_output=True)
            print("✅ Ambiente virtual criado com sucesso")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao criar ambiente virtual: {e}")
            return False
    
    def get_venv_python(self):
        """Retorna caminho do Python no ambiente virtual"""
        venv_path = self.project_root / 'venv'
        
        if self.is_windows:
            return venv_path / 'Scripts' / 'python.exe'
        else:
            return venv_path / 'bin' / 'python'
    
    def install_dependencies(self):
        """Instala dependências do projeto"""
        print("📚 Instalando dependências...")
        
        requirements_file = self.project_root / 'requirements.txt'
        if not requirements_file.exists():
            print("❌ Arquivo requirements.txt não encontrado!")
            return False
        
        venv_python = self.get_venv_python()
        
        try:
            # Atualizar pip primeiro
            subprocess.run([
                str(venv_python), '-m', 'pip', 'install', '--upgrade', 'pip'
            ], check=True, capture_output=True)
            
            # Instalar dependências
            subprocess.run([
                str(venv_python), '-m', 'pip', 'install', '-r', str(requirements_file)
            ], check=True)
            
            print("✅ Dependências instaladas com sucesso")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar dependências: {e}")
            return False
    
    def create_env_file(self):
        """Cria arquivo .env com configurações padrão"""
        env_file = self.project_root / '.env'
        
        if env_file.exists():
            print("⚙️  Arquivo .env já existe")
            return True
        
        print("⚙️  Criando arquivo de configuração (.env)...")
        
        env_content = """# CLÍNICA VIDA+ - Configurações
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///clinica.db

# Configurações do servidor
HOST=0.0.0.0
PORT=5000

# Configurações de segurança
WTF_CSRF_ENABLED=True
SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=True

# Configurações do Ordinix-123
ORDINIX_ENABLED=True
ORDINIX_DEBUG=True

# Configurações de cache
CACHE_TYPE=simple
CACHE_DEFAULT_TIMEOUT=300

# Configurações de upload
MAX_CONTENT_LENGTH=16777216
UPLOAD_FOLDER=uploads

# Configurações de log
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
"""
        
        try:
            env_file.write_text(env_content, encoding='utf-8')
            print("✅ Arquivo .env criado com sucesso")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar arquivo .env: {e}")
            return False
    
    def create_directories(self):
        """Cria diretórios necessários"""
        print("📁 Criando diretórios necessários...")
        
        directories = [
            'logs',
            'uploads',
            'instance',
            'backend/migrations',
            'static/uploads'
        ]
        
        for directory in directories:
            dir_path = self.project_root / directory
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print("✅ Diretórios criados com sucesso")
        return True
    
    def initialize_database(self):
        """Inicializa banco de dados"""
        print("🗄️  Inicializando banco de dados...")
        
        venv_python = self.get_venv_python()
        
        try:
            # Script para inicializar DB
            init_script = """
import sys
sys.path.append('.')
from backend.app import app, db

with app.app_context():
    db.create_all()
    print("Banco de dados inicializado com sucesso!")
"""
            
            result = subprocess.run([
                str(venv_python), '-c', init_script
            ], cwd=str(self.project_root), capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Banco de dados inicializado com sucesso")
                return True
            else:
                print(f"❌ Erro ao inicializar banco: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao inicializar banco de dados: {e}")
            return False
    
    def create_run_script(self):
        """Cria script para executar a aplicação"""
        print("🚀 Criando script de execução...")
        
        if self.is_windows:
            script_name = 'run.bat'
            script_content = f"""@echo off
echo 🏥 Iniciando CLÍNICA VIDA+ - Sistema Ordinix-123...
cd /d "{self.project_root}"
call venv\\Scripts\\activate
python backend\\app.py
pause
"""
        else:
            script_name = 'run.sh'
            script_content = f"""#!/bin/bash
echo "🏥 Iniciando CLÍNICA VIDA+ - Sistema Ordinix-123..."
cd "{self.project_root}"
source venv/bin/activate
python backend/app.py
"""
        
        script_path = self.project_root / script_name
        
        try:
            script_path.write_text(script_content, encoding='utf-8')
            
            if not self.is_windows:
                os.chmod(script_path, 0o755)
            
            print(f"✅ Script de execução criado: {script_name}")
            return True
        except Exception as e:
            print(f"❌ Erro ao criar script: {e}")
            return False
    
    def print_success_message(self):
        """Exibe mensagem de sucesso"""
        venv_activate = "venv\\Scripts\\activate" if self.is_windows else "source venv/bin/activate"
        run_command = "run.bat" if self.is_windows else "./run.sh"
        
        success_message = f"""
╔══════════════════════════════════════════════════════════════╗
║                    ✅ CONFIGURAÇÃO CONCLUÍDA!                ║
╚══════════════════════════════════════════════════════════════╝

🎉 O projeto CLÍNICA VIDA+ foi configurado com sucesso!

📋 PRÓXIMOS PASSOS:

1️⃣  Ativar ambiente virtual:
   {venv_activate}

2️⃣  Executar a aplicação:
   python backend/app.py
   
   OU usar o script criado:
   {run_command}

3️⃣  Acessar no navegador:
   http://localhost:5000

👥 CREDENCIAIS DE TESTE:
   • Admin: admin / admin123
   • Médico: medico / medico123  
   • Recepção: recepcao / recepcao123

📚 DOCUMENTAÇÃO:
   Consulte o arquivo README.md para mais informações

🆘 SUPORTE:
   Em caso de problemas, verifique os logs em logs/app.log

╔══════════════════════════════════════════════════════════════╗
║              🏥 CLÍNICA VIDA+ - Sistema Ordinix-123          ║
║                     Pronto para uso! 🚀                     ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(success_message)
    
    def run_setup(self):
        """Executa configuração completa"""
        self.print_banner()
        
        steps = [
            ("Verificando Python", self.check_python_version),
            ("Criando ambiente virtual", self.create_virtual_environment),
            ("Instalando dependências", self.install_dependencies),
            ("Criando configurações", self.create_env_file),
            ("Criando diretórios", self.create_directories),
            ("Inicializando banco", self.initialize_database),
            ("Criando scripts", self.create_run_script)
        ]
        
        for step_name, step_function in steps:
            print(f"\n🔄 {step_name}...")
            if not step_function():
                print(f"\n❌ Falha na etapa: {step_name}")
                print("🛑 Configuração interrompida!")
                return False
        
        self.print_success_message()
        return True

def main():
    """Função principal"""
    setup = ClinicaSetup()
    
    try:
        success = setup.run_setup()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n🛑 Configuração cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()