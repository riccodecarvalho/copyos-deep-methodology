#!/usr/bin/env python3
"""
Script para limpar e padronizar a estrutura do projeto COPYOS™
"""

import os
import shutil
import re
from pathlib import Path
from datetime import datetime

class ProjetoLimpeza:
    def __init__(self):
        self.root_dir = Path.cwd()
        self.backup_dir = self.root_dir / "BACKUP_LIMPEZA"
        
    def criar_backup(self):
        """Cria backup antes da limpeza"""
        print("📦 Criando backup...")
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        self.backup_dir.mkdir()
        
        # Copiar arquivos importantes
        for item in self.root_dir.iterdir():
            if item.name not in ['.git', 'BACKUP_LIMPEZA', '.DS_Store']:
                if item.is_file():
                    shutil.copy2(item, self.backup_dir)
                elif item.is_dir():
                    shutil.copytree(item, self.backup_dir / item.name)
        
        print("✅ Backup criado em BACKUP_LIMPEZA/")
    
    def remover_arquivos_sistema(self):
        """Remove arquivos de sistema"""
        print("🧹 Removendo arquivos de sistema...")
        
        # Remover .DS_Store
        for ds_file in self.root_dir.rglob('.DS_Store'):
            ds_file.unlink()
            print(f"   Removido: {ds_file}")
        
        # Remover outros arquivos de sistema
        system_files = ['.DS_Store', 'Thumbs.db', 'desktop.ini']
        for sys_file in system_files:
            for file_path in self.root_dir.rglob(sys_file):
                file_path.unlink()
                print(f"   Removido: {file_path}")
    
    def limpar_arquivos_redundantes(self):
        """Remove arquivos redundantes"""
        print("🗑️ Removendo arquivos redundantes...")
        
        # Arquivos redundantes na raiz
        redundant_files = [
            'GITHUB_SETUP_RAPIDO.md',  # Redundante com SETUP.md
            'ESTRUTURA_FINAL_LIMPA.md',  # Redundante com README.md
            'CORRECOES_VOLUME_09.md',  # Arquivo vazio
        ]
        
        for file_name in redundant_files:
            file_path = self.root_dir / file_name
            if file_path.exists():
                file_path.unlink()
                print(f"   Removido: {file_name}")
    
    def limpar_prompts_redundantes(self):
        """Mantém apenas as versões mais recentes dos prompts"""
        print("📝 Limpando prompts redundantes...")
        
        prompts_dir = self.root_dir / "02_PROMPTS"
        if not prompts_dir.exists():
            return
        
        # Definir quais versões manter
        keep_patterns = [
            r'PROMPT_COPYOS_CHATGPT_REFINADO_OTIMIZADO\.md$',
            r'PROMPT_COPYOS_GEMINI_REFINADO_OTIMIZADO\.md$',
            r'PROMPT_COPYOS_FEEDBACK_LOOP_OTIMIZADO\.md$',
            r'CHANGELOG_MELHORIAS\.md$'
        ]
        
        # Remover versões antigas
        for file_path in prompts_dir.iterdir():
            if file_path.is_file() and file_path.suffix == '.md':
                should_keep = any(re.match(pattern, file_path.name) for pattern in keep_patterns)
                if not should_keep:
                    file_path.unlink()
                    print(f"   Removido: {file_path.name}")
    
    def limpar_scripts_temporarios(self):
        """Remove arquivos temporários dos scripts"""
        print("🔧 Limpando scripts temporários...")
        
        scripts_dir = self.root_dir / "03_SCRIPTS"
        if not scripts_dir.exists():
            return
        
        # Padrões de arquivos temporários
        temp_patterns = [
            r'blueprint_.*_\d{8}_\d{6}\.md$',
            r'evidencias_.*_\d{8}_\d{6}\.json$',
            r'debug_.*\.py$',
            r'testar_.*\.py$',
            r'consolidar_.*\.py$',  # Scripts antigos
        ]
        
        for file_path in scripts_dir.iterdir():
            if file_path.is_file():
                should_remove = any(re.match(pattern, file_path.name) for pattern in temp_patterns)
                if should_remove:
                    file_path.unlink()
                    print(f"   Removido: {file_path.name}")
    
    def renomear_arquivos_finais(self):
        """Renomeia os arquivos finais para nomenclatura limpa"""
        print("🏷️ Renomeando arquivos finais...")
        
        # Renomear prompts finais
        prompts_dir = self.root_dir / "02_PROMPTS"
        if prompts_dir.exists():
            rename_map = {
                'PROMPT_COPYOS_CHATGPT_REFINADO_OTIMIZADO.md': 'PROMPT_COPYOS_CHATGPT.md',
                'PROMPT_COPYOS_GEMINI_REFINADO_OTIMIZADO.md': 'PROMPT_COPYOS_GEMINI.md',
                'PROMPT_COPYOS_FEEDBACK_LOOP_OTIMIZADO.md': 'PROMPT_COPYOS_FEEDBACK_LOOP.md',
            }
            
            for old_name, new_name in rename_map.items():
                old_path = prompts_dir / old_name
                new_path = prompts_dir / new_name
                if old_path.exists():
                    old_path.rename(new_path)
                    print(f"   Renomeado: {old_name} → {new_name}")
    
    def verificar_estrutura_final(self):
        """Verifica a estrutura final"""
        print("\n📋 ESTRUTURA FINAL:")
        print("=" * 50)
        
        for item in sorted(self.root_dir.iterdir()):
            if item.is_dir() and not item.name.startswith('.'):
                print(f"📁 {item.name}/")
                try:
                    for subitem in sorted(item.iterdir()):
                        if subitem.is_file():
                            size = subitem.stat().st_size
                            print(f"   📄 {subitem.name} ({size:,} bytes)")
                except PermissionError:
                    print(f"   ⚠️ Erro de permissão ao listar {item.name}")
            elif item.is_file() and not item.name.startswith('.'):
                size = item.stat().st_size
                print(f"📄 {item.name} ({size:,} bytes)")
    
    def executar_limpeza_completa(self):
        """Executa a limpeza completa"""
        print("🚀 INICIANDO LIMPEZA E PADRONIZAÇÃO")
        print("=" * 50)
        
        # 1. Backup
        self.criar_backup()
        
        # 2. Limpeza
        self.remover_arquivos_sistema()
        self.limpar_arquivos_redundantes()
        self.limpar_prompts_redundantes()
        self.limpar_scripts_temporarios()
        
        # 3. Renomeação
        self.renomear_arquivos_finais()
        
        # 4. Verificação
        self.verificar_estrutura_final()
        
        print("\n✅ LIMPEZA CONCLUÍDA!")
        print("📦 Backup salvo em: BACKUP_LIMPEZA/")

def main():
    """Função principal"""
    limpeza = ProjetoLimpeza()
    limpeza.executar_limpeza_completa()

if __name__ == "__main__":
    main() 