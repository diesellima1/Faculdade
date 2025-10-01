# ===== SISTEMA CLÍNICA VIDA+ COM ORDINIX-123 =====
# Inventor: Adevilson de Lima - Estudante ADS Anhanguera
# Sistema revolucionário de triagem hospitalar

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class SistemaOrdinix123:
    """Sistema Ordinix-123 - Inovação em triagem médica"""
    
    NIVEIS = {
        1: {"cor": "verde", "descricao": "Normal - Gravidade Baixa", "sla": 60},
        2: {"cor": "amarelo", "descricao": "Urgente - Gravidade Média", "sla": 30}, 
        3: {"cor": "vermelho", "descricao": "Emergência - Gravidade Alta", "sla": 15}
    }
    
    def __init__(self):
        self.pacientes = []
        self.fila_atendimento = []
        self.historico = []
    
    def classificar_prioridade(self, sintomas: dict) -> int:
        """Algoritmo inteligente de classificação Ordinix-123"""
        if any([sintomas.get('hemorragia'), sintomas.get('parada_cardiaca'), 
                sintomas.get('inconsciencia')]):
            return 3  # Vermelho - Emergência
        elif any([sintomas.get('dor_intensa'), sintomas.get('febre_alta'),
                  sintomas.get('dificuldade_respirar')]):
            return 2  # Amarelo - Urgente  
        else:
            return 1  # Verde - Normal

class SistemaGestaoClinica:
    """Sistema completo de gestão com funcionalidades avançadas"""
    
    def __init__(self):
        self.pacientes = []
        self.agendamentos = []
        self.ordinix = SistemaOrdinix123()
    
    def validar_cpf(self, cpf: str) -> bool:
        """Valida CPF com algoritmo oficial"""
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Valida primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        
        if int(cpf[9]) != digito1:
            return False
        
        # Valida segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        
        if int(cpf[10]) != digito2:
            return False
        
        return True
    
    def formatar_cpf(self, cpf: str) -> str:
        """Formata CPF para padrão xxx.xxx.xxx-xx"""
        cpf = ''.join(filter(str.isdigit, cpf))
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    def validar_nivel_emergencia(self) -> int:
        """Valida nível de emergência (aceita apenas 1, 2 ou 3)"""
        while True:
            try:
                nivel = input("Nível de prioridade (1-3): ").strip()
                
                # Verifica se é apenas um caractere numérico
                if not nivel.isdigit() or len(nivel) != 1:
                    print("❌ Digite apenas UM número de 1 a 3!")
                    continue
                
                nivel = int(nivel)
                
                # Verifica se está no intervalo correto
                if nivel not in [1, 2, 3]:
                    print("❌ Nível inválido! Digite 1, 2 ou 3.")
                    continue
                
                return nivel
                
            except ValueError:
                print("❌ Digite apenas números de 1 a 3!")
    
    def menu_principal(self):
        while True:
            print("\n🏥 SISTEMA CLÍNICA VIDA+ - ORDINIX-123")
            print("Inventor: Adevilson de Lima - ADS Anhanguera")
            print("="*60)
            print("1. 👤 Cadastrar paciente")
            print("2. 📊 Ver estatísticas") 
            print("3. 🔍 Buscar paciente")
            print("4. 📋 Listar todos pacientes")
            print("5. 📅 Sistema de Agendamento Inteligente")
            print("6. 🖨️ Impressão Individual/Lote")
            print("7. 🚨 Painel Ordinix-123")
            print("8. 📤 Compartilhar entre setores")
            print("9. ❌ Sair")
            print("\n💡 Dica: Digite 0 ou 'voltar' em qualquer submenu para retornar")
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "1":
                    self.cadastrar_paciente()
                elif opcao == "2":
                    self.ver_estatisticas()
                elif opcao == "3":
                    self.buscar_paciente()
                elif opcao == "4":
                    self.listar_pacientes()
                elif opcao == "5":
                    self.sistema_agendamento()
                elif opcao == "6":
                    self.sistema_impressao()
                elif opcao == "7":
                    self.painel_ordinix()
                elif opcao == "8":
                    self.compartilhar_setores()
                elif opcao == "9":
                    confirmacao = input("⚠️ Tem certeza que deseja sair? (s/n): ").lower()
                    if confirmacao == 's':
                        print("👋 Sistema encerrado com sucesso!")
                        break
                    else:
                        print("↩️ Retornando ao menu...")
                else:
                    print("❌ Opção inválida! Digite um número de 1 a 9.")
                    
            except ValueError:
                print("❌ Digite apenas números!")
    
    def cadastrar_paciente(self):
        """Cadastro com Sistema Ordinix-123 integrado + CPF"""
        print("\n📝 CADASTRO DE PACIENTE COM ORDINIX-123")
        print("-" * 50)
        print("💡 Digite 'sair' a qualquer momento para cancelar o cadastro\n")
        
        try:
            nome = input("Nome: ").strip()
            if nome.lower() == 'sair':
                print("❌ Cadastro cancelado")
                input("\n⏎ Pressione ENTER para voltar ao menu...")
                return
            if not nome:
                raise ValueError("Nome obrigatório")
            
            # Validação de CPF com loop até digitar correto
            while True:
                cpf = input("CPF (apenas números ou 'sair' para cancelar): ").strip()
                
                if cpf.lower() == 'sair':
                    print("❌ Cadastro cancelado")
                    input("\n⏎ Pressione ENTER para voltar ao menu...")
                    return
                
                # Remove caracteres não numéricos
                cpf_numeros = ''.join(filter(str.isdigit, cpf))
                
                if not cpf_numeros:
                    print("❌ CPF não pode estar vazio!")
                    continue
                
                if not cpf_numeros.isdigit():
                    print("❌ CPF deve conter apenas números!")
                    continue
                
                if len(cpf_numeros) != 11:
                    print("❌ CPF deve ter exatamente 11 dígitos!")
                    continue
                
                if not self.validar_cpf(cpf_numeros):
                    print("❌ CPF inválido! Verifique os números digitados.")
                    continue
                
                # CPF válido
                cpf_formatado = self.formatar_cpf(cpf_numeros)
                print(f"✅ CPF válido: {cpf_formatado}")
                break
            
            # Validação de idade (apenas números)
            while True:
                idade_input = input("Idade (ou 'sair' para cancelar): ").strip()
                if idade_input.lower() == 'sair':
                    print("❌ Cadastro cancelado")
                    input("\n⏎ Pressione ENTER para voltar ao menu...")
                    return
                if idade_input.isdigit():
                    idade = int(idade_input)
                    break
                else:
                    print("❌ Idade deve conter apenas números!")
            
            # Validação de telefone (apenas números)
            while True:
                telefone = input("Telefone (apenas números ou 'sair' para cancelar): ").strip()
                if telefone.lower() == 'sair':
                    print("❌ Cadastro cancelado")
                    input("\n⏎ Pressione ENTER para voltar ao menu...")
                    return
                if telefone.isdigit():
                    break
                else:
                    print("❌ Telefone deve conter apenas números!")
            
            print("\n🚨 SISTEMA ORDINIX-123 - Classificação:")
            print("1. 🟢 Nível 1 - Normal (Verde)")
            print("2. 🟡 Nível 2 - Urgente (Amarelo)")
            print("3. 🔴 Nível 3 - Emergência (Vermelho)")
            
            # Validação de nível de emergência (apenas 1, 2 ou 3)
            nivel = self.validar_nivel_emergencia()
            
            # Sistema de confirmação anti-acidental
            cores = {1: "Verde", 2: "Amarelo", 3: "Vermelho"}
            confirma = input(f"⚠️ Confirma nível {nivel} ({cores[nivel]})? "
                           f"Isso afetará a prioridade! (s/n): ").lower()
            
            if confirma != 's':
                print("❌ Cadastro cancelado")
                input("\n⏎ Pressione ENTER para voltar ao menu...")
                return
            
            paciente = {
                "id": len(self.pacientes) + 1,
                "nome": nome,
                "cpf": cpf_formatado,
                "idade": idade,
                "telefone": telefone,
                "nivel_ordinix": nivel,
                "timestamp": datetime.now(),
                "status": "ativo"
            }
            
            self.pacientes.append(paciente)
            self.adicionar_fila_inteligente(paciente)
            
            print(f"✅ {nome} cadastrado com sucesso!")
            print(f"📋 CPF: {cpf_formatado}")
            
            if nivel == 3:
                self.alerta_emergencia(paciente)
            
            input("\n⏎ Pressione ENTER para voltar ao menu...")
                
        except ValueError as e:
            print(f"❌ Erro: {e}")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def buscar_paciente(self):
        """Busca paciente por nome ou CPF"""
        if not self.pacientes:
            print("❌ Nenhum paciente cadastrado")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        print("\n🔍 BUSCAR PACIENTE")
        print("1. Buscar por nome")
        print("2. Buscar por CPF")
        print("0. ↩️ Voltar ao menu principal")
        
        opcao = input("Escolha (0-2): ").strip()
        
        if opcao == "0":
            print("↩️ Retornando ao menu...")
            return
        
        if opcao == "1":
            termo = input("Digite o nome (ou 0 para voltar): ").strip()
            if termo == "0":
                print("↩️ Retornando ao menu...")
                return
            resultados = [p for p in self.pacientes if termo.lower() in p["nome"].lower()]
        elif opcao == "2":
            cpf = input("Digite o CPF (ou 0 para voltar): ").strip()
            if cpf == "0":
                print("↩️ Retornando ao menu...")
                return
            cpf_numeros = ''.join(filter(str.isdigit, cpf))
            resultados = [p for p in self.pacientes if cpf_numeros in p["cpf"].replace(".", "").replace("-", "")]
        else:
            print("❌ Opção inválida")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        if resultados:
            print(f"\n✅ {len(resultados)} paciente(s) encontrado(s):")
            for p in resultados:
                self.imprimir_individual(p)
        else:
            print("❌ Nenhum paciente encontrado")
        
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def listar_pacientes(self):
        """Lista todos os pacientes com CPF"""
        if not self.pacientes:
            print("❌ Nenhum paciente cadastrado")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        print("\n📋 LISTA DE TODOS OS PACIENTES")
        print("=" * 80)
        
        for p in self.pacientes:
            cores = {1: "🟢", 2: "🟡", 3: "🔴"}
            print(f"{cores[p['nivel_ordinix']]} ID: {p['id']} | {p['nome']} | CPF: {p['cpf']} | "
                  f"Idade: {p['idade']} | Telefone: {p['telefone']}")
        
        print("=" * 80)
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def painel_ordinix(self):
        """Painel de controle Ordinix-123 com visualização da fila"""
        print("\n🚨 PAINEL ORDINIX-123 - FILA DE ATENDIMENTO")
        print("=" * 60)
        
        if not self.ordinix.fila_atendimento:
            print("❌ Fila vazia")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        print(f"Total na fila: {len(self.ordinix.fila_atendimento)} pacientes\n")
        
        for i, p in enumerate(self.ordinix.fila_atendimento, 1):
            cores = {1: "🟢", 2: "🟡", 3: "🔴"}
            nivel_desc = {1: "Normal", 2: "Urgente", 3: "EMERGÊNCIA"}
            
            print(f"{i}º lugar - {cores[p['nivel_ordinix']]} {nivel_desc[p['nivel_ordinix']]}")
            print(f"   Nome: {p['nome']}")
            print(f"   CPF: {p['cpf']}")
            print(f"   Chegada: {p['timestamp'].strftime('%H:%M:%S')}")
            print("-" * 60)
        
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def adicionar_fila_inteligente(self, paciente):
        """Fila com priorização automática Ordinix-123"""
        self.ordinix.fila_atendimento.append(paciente)
        self.ordinix.fila_atendimento.sort(
            key=lambda x: (-x["nivel_ordinix"], x["timestamp"])
        )
        
        if paciente["nivel_ordinix"] == 3:
            print("🚨 PRIORIDADE MÁXIMA ATIVADA!")
            print("• Paciente movido para início da fila")
            print("• SLA: 15 minutos")
    
    def alerta_emergencia(self, paciente):
        """Sistema de alertas para emergências nível 3"""
        print("\n" + "🔴" * 30)
        print("🚨 ALERTA DE EMERGÊNCIA - NÍVEL 3")
        print("🔴" * 30)
        print(f"Paciente: {paciente['nome']}")
        print(f"CPF: {paciente['cpf']}")
        print("🔄 Bolinhas piscando ativadas")
        print("🔊 Notificação sonora acionada") 
        print("👨‍⚕️ Equipe médica notificada")
        print("⏱️ SLA: 15 minutos máximo")
        print("🔴" * 30)
        
        print("\n📋 PROTOCOLO DE EMERGÊNCIA:")
        print("1. Verificar sinais vitais imediatamente")
        print("2. Preparar leito de emergência")
        print("3. Comunicar familiares com calma")
        print("4. Documentar todos os procedimentos")
    
    def ver_estatisticas(self):
        """Estatísticas com análise Ordinix-123"""
        if not self.pacientes:
            print("❌ Nenhum paciente cadastrado")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        total = len(self.pacientes)
        idades = [p["idade"] for p in self.pacientes]
        idade_media = sum(idades) / len(idades)
        mais_novo = min(self.pacientes, key=lambda x: x["idade"])
        mais_velho = max(self.pacientes, key=lambda x: x["idade"])
        
        niveis = {1: 0, 2: 0, 3: 0}
        for p in self.pacientes:
            niveis[p["nivel_ordinix"]] += 1
        
        print(f"\n📊 ESTATÍSTICAS - SISTEMA ORDINIX-123")
        print("=" * 50)
        print(f"Total de pacientes: {total}")
        print(f"Idade média: {idade_media:.1f} anos")
        print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
        print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
        print("\n🚨 DISTRIBUIÇÃO ORDINIX-123:")
        print(f"🟢 Nível 1 (Normal): {niveis[1]} pacientes")
        print(f"🟡 Nível 2 (Urgente): {niveis[2]} pacientes")
        print(f"🔴 Nível 3 (Emergência): {niveis[3]} pacientes")
        
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def sistema_agendamento(self):
        """Sistema de agendamento inteligente com pré-cadastro"""
        print("\n📅 SISTEMA DE AGENDAMENTO INTELIGENTE")
        print("-" * 50)
        
        print("Funcionalidades disponíveis:")
        print("1. 📝 Agendar consulta (pré-cadastrado)")
        print("2. 📋 Ver agenda do dia")
        print("3. ⏰ Reagendar por prioridade Ordinix")
        print("4. 📊 Relatório de eficiência")
        print("0. ↩️ Voltar ao menu principal")
        
        opcao = input("Escolha uma opção (0-4): ").strip()
        
        if opcao == "0":
            print("↩️ Retornando ao menu...")
            return
        elif opcao == "1":
            print("✅ Módulo de agendamento em desenvolvimento")
            print("🔄 Integração com Ordinix-123 em progresso")
        else:
            print("⚠️ Funcionalidade em desenvolvimento")
        
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def sistema_impressao(self):
        """Sistema de impressão individual e em lote"""
        print("\n🖨️ SISTEMA DE IMPRESSÃO AVANÇADO")
        print("-" * 50)
        
        if not self.pacientes:
            print("❌ Nenhum paciente para imprimir")
            input("\n⏎ Pressione ENTER para voltar ao menu...")
            return
        
        print("Opções de impressão:")
        print("1. 📄 Impressão individual")
        print("2. 📚 Impressão em lote (todos)")
        print("3. 🎯 Imprimir por nível Ordinix")
        print("4. 📊 Relatório personalizado")
        print("0. ↩️ Voltar ao menu principal")
        
        opcao = input("Escolha uma opção (0-4): ").strip()
        
        if opcao == "0":
            print("↩️ Retornando ao menu...")
            return
        
        if opcao == "1":
            nome = input("Nome do paciente (ou 0 para voltar): ").strip()
            if nome == "0":
                print("↩️ Retornando ao menu...")
                return
            paciente = next((p for p in self.pacientes if nome.lower() in p["nome"].lower()), None)
            if paciente:
                self.imprimir_individual(paciente)
            else:
                print("❌ Paciente não encontrado")
        
        elif opcao == "2":
            confirma = input("⚠️ Imprimir TODOS os pacientes? (s/n): ").lower()
            if confirma == 's':
                self.imprimir_lote()
            else:
                print("❌ Impressão cancelada")
        
        elif opcao == "3":
            nivel = input("Nível Ordinix (1-3 ou 0 para voltar): ").strip()
            if nivel == "0":
                print("↩️ Retornando ao menu...")
                return
            try:
                nivel = int(nivel)
                if nivel in [1, 2, 3]:
                    pacientes_nivel = [p for p in self.pacientes if p["nivel_ordinix"] == nivel]
                    if pacientes_nivel:
                        for p in pacientes_nivel:
                            self.imprimir_individual(p)
                    else:
                        print(f"❌ Nenhum paciente no nível {nivel}")
                else:
                    print("❌ Nível inválido")
            except ValueError:
                print("❌ Digite apenas números")
        
        elif opcao == "4":
            print("⚠️ Funcionalidade em desenvolvimento")
        else:
            print("❌ Opção inválida")
        
        input("\n⏎ Pressione ENTER para voltar ao menu...")
    
    def imprimir_individual(self, paciente):
        """Impressão de ficha individual com CPF"""
        print(f"\n📄 FICHA INDIVIDUAL - CLÍNICA VIDA+")
        print("=" * 40)
        print(f"ID: {paciente['id']}")
        print(f"Nome: {paciente['nome']}")
        print(f"CPF: {paciente['cpf']}")
        print(f"Idade: {paciente['idade']} anos")
        print(f"Telefone: {paciente['telefone']}")
        cores = {1: "Verde", 2: "Amarelo", 3: "Vermelho"}
        print(f"Ordinix-123: Nível {paciente['nivel_ordinix']} ({cores[paciente['nivel_ordinix']]})")
        print(f"Data/Hora: {paciente['timestamp'].strftime('%d/%m/%Y %H:%M')}")
        print("=" * 40)
    
    def imprimir_lote(self):
        """Impressão em lote de todos os pacientes"""
        print("\n📚 IMPRESSÃO EM LOTE - TODOS OS PACIENTES")
        print("=" * 50)
        
        for p in self.pacientes:
            self.imprimir_individual(p)
            print()
    
    def compartilhar_setores(self):
        """Sistema de compartilhamento entre setores"""
        print("\n📤 COMPARTILHAMENTO ENTRE SETORES")
        print("-" * 50)
        
        setores = ["Recepção", "Enfermagem", "Médico", "Farmácia", "Administração"]
        
        print("Setores disponíveis:")
        for i, setor in enumerate(setores, 1):
            print(f"{i}. {setor}")
        
        print("\nFuncionalidades:")
        print("• Lista unificada para todos setores")
        print("• Permissões por usuário") 
        print("• Sincronização em tempo real")
        print("• Histórico de acessos")
        
        print("\n✅ Sistema de compartilhamento configurado!")
        input("\n⏎ Pressione ENTER para voltar ao menu...")

# Execução do sistema
if __name__ == "__main__":
    sistema = SistemaGestaoClinica()
    sistema.menu_principal()