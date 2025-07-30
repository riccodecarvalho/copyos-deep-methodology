#!/usr/bin/env python3
"""
Script para conectar automaticamente o projeto COPYOS™ ao GitHub
"""

import os
import subprocess
import sys
import json
from pathlib import Path

class GitHubConnector:
    def __init__(self):
        self.project_name = "copyos-deep-methodology"
        self.description = "COPYOS™ - Sistema de Copywriting com Metodologia Profunda"
        self.current_dir = Path.cwd()
        
    def check_git_installed(self):
        """Verifica se o Git está instalado"""
        try:
            result = subprocess.run(['git', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Git encontrado: {result.stdout.strip()}")
                return True
            else:
                print("❌ Git não encontrado")
                return False
        except FileNotFoundError:
            print("❌ Git não está instalado")
            return False
    
    def check_github_cli(self):
        """Verifica se o GitHub CLI está instalado"""
        try:
            result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ GitHub CLI encontrado: {result.stdout.split()[2]}")
                return True
            else:
                print("❌ GitHub CLI não encontrado")
                return False
        except FileNotFoundError:
            print("❌ GitHub CLI não está instalado")
            return False
    
    def check_git_status(self):
        """Verifica o status atual do Git"""
        try:
            result = subprocess.run(['git', 'status'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Repositório Git inicializado")
                return True
            else:
                print("❌ Repositório Git não inicializado")
                return False
        except Exception as e:
            print(f"❌ Erro ao verificar status do Git: {e}")
            return False
    
    def check_github_auth(self):
        """Verifica se está autenticado no GitHub"""
        try:
            result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Autenticado no GitHub")
                return True
            else:
                print("❌ Não autenticado no GitHub")
                return False
        except Exception as e:
            print(f"❌ Erro ao verificar autenticação: {e}")
            return False
    
    def authenticate_github(self):
        """Autentica no GitHub"""
        print("\n🔐 Autenticando no GitHub...")
        try:
            subprocess.run(['gh', 'auth', 'login'], check=True)
            print("✅ Autenticação concluída!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro na autenticação: {e}")
            return False
    
    def create_repository(self):
        """Cria o repositório no GitHub"""
        print(f"\n🚀 Criando repositório: {self.project_name}")
        try:
            cmd = [
                'gh', 'repo', 'create', self.project_name,
                '--description', self.description,
                '--public',
                '--source', '.',
                '--remote', 'origin',
                '--push'
            ]
            subprocess.run(cmd, check=True)
            print("✅ Repositório criado e conectado!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao criar repositório: {e}")
            return False
    
    def push_to_github(self):
        """Faz push para o GitHub"""
        print("\n📤 Fazendo push para o GitHub...")
        try:
            # Adicionar todos os arquivos
            subprocess.run(['git', 'add', '.'], check=True)
            
            # Commit
            subprocess.run([
                'git', 'commit', '-m', 
                'Initial commit: COPYOS™ with deep methodology - 9 volumes processed with 100/100 QA score'
            ], check=True)
            
            # Push
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
            
            print("✅ Push realizado com sucesso!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro no push: {e}")
            return False
    
    def get_repository_url(self):
        """Obtém a URL do repositório"""
        try:
            result = subprocess.run(['gh', 'repo', 'view', '--json', 'url'], capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                return data.get('url')
            else:
                return None
        except Exception:
            return None
    
    def run_automatic_setup(self):
        """Executa o setup automático completo"""
        print("🚀 SETUP AUTOMÁTICO - COPYOS™ GITHUB")
        print("=" * 50)
        
        # 1. Verificar Git
        if not self.check_git_installed():
            print("\n❌ Instale o Git primeiro: https://git-scm.com/")
            return False
        
        # 2. Verificar GitHub CLI
        if not self.check_github_cli():
            print("\n❌ Instale o GitHub CLI primeiro: https://cli.github.com/")
            return False
        
        # 3. Verificar status do Git
        if not self.check_git_status():
            print("\n❌ Repositório Git não inicializado")
            return False
        
        # 4. Verificar autenticação
        if not self.check_github_auth():
            print("\n🔐 Autenticação necessária...")
            if not self.authenticate_github():
                return False
        
        # 5. Criar repositório
        if not self.create_repository():
            print("\n❌ Falha ao criar repositório")
            return False
        
        # 6. Obter URL
        repo_url = self.get_repository_url()
        if repo_url:
            print(f"\n🎉 REPOSITÓRIO CRIADO COM SUCESSO!")
            print(f"📋 URL: {repo_url}")
            print(f"📁 Nome: {self.project_name}")
            print(f"📝 Descrição: {self.description}")
        
        print("\n✅ SETUP COMPLETO!")
        print("\n📋 PRÓXIMOS PASSOS:")
        print("1. Acesse o repositório no GitHub")
        print("2. Configure o Cursor Agent:")
        print("   - Vá para https://cursor.sh")
        print("   - Clique em 'Open Repository'")
        print("   - Selecione o repositório criado")
        print("3. O .cursorrules será usado automaticamente")
        
        return True

def main():
    """Função principal"""
    connector = GitHubConnector()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--manual':
        print("📋 SETUP MANUAL:")
        print("1. Acesse: https://github.com/new")
        print("2. Nome: copyos-deep-methodology")
        print("3. Descrição: COPYOS™ - Sistema de Copywriting com Metodologia Profunda")
        print("4. Público")
        print("5. NÃO inicialize com README")
        print("6. Execute os comandos:")
        print("   git remote add origin https://github.com/SEU_USUARIO/copyos-deep-methodology.git")
        print("   git branch -M main")
        print("   git push -u origin main")
    else:
        connector.run_automatic_setup()

if __name__ == "__main__":
    main() 