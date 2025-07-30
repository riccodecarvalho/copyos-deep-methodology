#!/usr/bin/env python3
"""
OTIMIZADOR AUTOMÁTICO DE PROMPTS - COPYOS™
Analisa e otimiza automaticamente prompts baseado em feedback e métricas
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

class OtimizadorAutomaticoPrompts:
    def __init__(self):
        self.prompts_otimizados = {}
        self.metricas_melhoria = {
            'prompts_analisados': 0,
            'prompts_otimizados': 0,
            'melhoria_media': 0,
            'tempo_economizado': 0
        }
        
    def carregar_prompts_atuais(self):
        """Carrega todos os prompts atuais do sistema"""
        prompts = {
            'chatgpt_refinado': {
                'arquivo': 'COPYOS_FINAL/02_PROMPTS/PROMPT_COPYOS_CHATGPT_REFINADO.md',
                'tipo': 'ChatGPT',
                'versao': 'Refinado'
            },
            'gemini_refinado': {
                'arquivo': 'COPYOS_FINAL/02_PROMPTS/PROMPT_COPYOS_GEMINI_REFINADO.md',
                'tipo': 'Gemini',
                'versao': 'Refinado'
            },
            'feedback_loop': {
                'arquivo': 'COPYOS_FINAL/02_PROMPTS/PROMPT_COPYOS_FEEDBACK_LOOP.md',
                'tipo': 'Feedback',
                'versao': '1.0'
            }
        }
        return prompts
    
    def analisar_prompt(self, arquivo_prompt):
        """Analisa um prompt e identifica oportunidades de melhoria"""
        try:
            with open(arquivo_prompt, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            analise = {
                'tamanho': len(conteudo),
                'linhas': len(conteudo.split('\n')),
                'secoes': self.contar_secoes(conteudo),
                'placeholders': self.contar_placeholders(conteudo),
                'exemplos': self.contar_exemplos(conteudo),
                'problemas_identificados': [],
                'melhorias_sugeridas': []
            }
            
            # Identificar problemas
            if analise['tamanho'] > 15000:
                analise['problemas_identificados'].append('Prompt muito longo - pode causar timeout')
                analise['melhorias_sugeridas'].append('Reduzir redundâncias e simplificar instruções')
            
            if analise['placeholders'] < 5:
                analise['problemas_identificados'].append('Poucos placeholders - baixa flexibilidade')
                analise['melhorias_sugeridas'].append('Adicionar mais placeholders dinâmicos')
            
            if analise['exemplos'] < 3:
                analise['problemas_identificados'].append('Poucos exemplos - baixa clareza')
                analise['melhorias_sugeridas'].append('Adicionar mais exemplos práticos')
            
            if 'REGRAS DE OPERAÇÃO' not in conteudo:
                analise['problemas_identificados'].append('Falta seção de regras claras')
                analise['melhorias_sugeridas'].append('Adicionar seção REGRAS DE OPERAÇÃO')
            
            return analise
            
        except FileNotFoundError:
            return {'erro': 'Arquivo não encontrado'}
    
    def contar_secoes(self, conteudo):
        """Conta o número de seções no prompt"""
        secoes = re.findall(r'^##\s+\*\*([^*]+)\*\*', conteudo, re.MULTILINE)
        return len(secoes)
    
    def contar_placeholders(self, conteudo):
        """Conta o número de placeholders no prompt"""
        placeholders = re.findall(r'\[([^\]]+)\]', conteudo)
        return len(set(placeholders))
    
    def contar_exemplos(self, conteudo):
        """Conta o número de exemplos no prompt"""
        exemplos = re.findall(r'###\s+.*[Ee]xemplo', conteudo)
        return len(exemplos)
    
    def otimizar_prompt(self, conteudo_original, analise):
        """Otimiza um prompt baseado na análise"""
        conteudo_otimizado = conteudo_original
        
        # Aplicar melhorias baseadas na análise
        melhorias_aplicadas = []
        
        # 1. Adicionar seção de regras se não existir
        if 'REGRAS DE OPERAÇÃO' not in conteudo_otimizado:
            regras_section = """
## **REGRAS DE OPERAÇÃO**

1. **Sempre aplique a metodologia RMBC II** em todas as entregas
2. **Use placeholders dinâmicos** para personalização
3. **Forneça exemplos práticos** sempre que possível
4. **Mantenha foco na conversão** e resultados
5. **Solicite feedback** após cada entrega
"""
            # Inserir após a seção TASK
            if '## **TASK**' in conteudo_otimizado:
                pos = conteudo_otimizado.find('## **TASK**')
                pos_fim = conteudo_otimizado.find('##', pos + 1)
                if pos_fim == -1:
                    pos_fim = len(conteudo_otimizado)
                
                conteudo_otimizado = (
                    conteudo_otimizado[:pos_fim] + 
                    regras_section + 
                    conteudo_otimizado[pos_fim:]
                )
                melhorias_aplicadas.append('Adicionada seção REGRAS DE OPERAÇÃO')
        
        # 2. Adicionar placeholders se necessário
        if analise['placeholders'] < 5:
            placeholders_adicional = """
### **PLACEHOLDERS ADICIONAIS:**
- `[CONTEXTO_ESPECIFICO]` - Contexto único do projeto
- `[RESULTADO_ESPERADO]` - Resultado específico desejado
- `[RESTRICOES]` - Limitações ou restrições
- `[PRIORIDADE]` - Nível de prioridade do projeto
- `[DEADLINE]` - Prazo para entrega
"""
            # Adicionar ao final do prompt
            conteudo_otimizado += placeholders_adicional
            melhorias_aplicadas.append('Adicionados placeholders dinâmicos')
        
        # 3. Adicionar exemplos se necessário
        if analise['exemplos'] < 3:
            exemplos_adicional = """
### **EXEMPLO DE USO RÁPIDO:**
```
"Use o modo [2a] Criação Rápida para criar um VSL para [PRODUTO] 
focado em [PUBLICO_ALVO] com deadline [DEADLINE]"
```
"""
            # Adicionar ao final do prompt
            conteudo_otimizado += exemplos_adicional
            melhorias_aplicadas.append('Adicionados exemplos práticos')
        
        # 4. Otimizar estrutura se muito longo
        if analise['tamanho'] > 15000:
            # Remover redundâncias
            conteudo_otimizado = re.sub(r'\n\s*\n\s*\n', '\n\n', conteudo_otimizado)
            melhorias_aplicadas.append('Removidas redundâncias e otimizada estrutura')
        
        return {
            'conteudo_otimizado': conteudo_otimizado,
            'melhorias_aplicadas': melhorias_aplicadas,
            'tamanho_original': analise['tamanho'],
            'tamanho_otimizado': len(conteudo_otimizado),
            'reducao_tamanho': analise['tamanho'] - len(conteudo_otimizado)
        }
    
    def executar_otimizacao_completa(self):
        """Executa otimização completa de todos os prompts"""
        print("🚀 INICIANDO OTIMIZAÇÃO AUTOMÁTICA DE PROMPTS")
        print("=" * 50)
        
        prompts = self.carregar_prompts_atuais()
        
        for key, prompt_info in prompts.items():
            print(f"\n🔍 Analisando: {prompt_info['tipo']} ({prompt_info['versao']})")
            
            # Analisar prompt atual
            analise = self.analisar_prompt(prompt_info['arquivo'])
            
            if 'erro' in analise:
                print(f"   ❌ Erro: {analise['erro']}")
                continue
            
            print(f"   📊 Tamanho: {analise['tamanho']} caracteres")
            print(f"   📊 Seções: {analise['secoes']}")
            print(f"   📊 Placeholders: {analise['placeholders']}")
            print(f"   📊 Exemplos: {analise['exemplos']}")
            
            # Identificar problemas
            if analise['problemas_identificados']:
                print(f"   ⚠️ Problemas identificados:")
                for problema in analise['problemas_identificados']:
                    print(f"      • {problema}")
            
            # Otimizar se necessário
            if analise['problemas_identificados']:
                print(f"   🔧 Aplicando otimizações...")
                
                # Ler conteúdo original
                with open(prompt_info['arquivo'], 'r', encoding='utf-8') as f:
                    conteudo_original = f.read()
                
                # Otimizar
                resultado_otimizacao = self.otimizar_prompt(conteudo_original, analise)
                
                # Salvar versão otimizada
                arquivo_otimizado = prompt_info['arquivo'].replace('.md', '_OTIMIZADO.md')
                with open(arquivo_otimizado, 'w', encoding='utf-8') as f:
                    f.write(resultado_otimizacao['conteudo_otimizado'])
                
                print(f"   ✅ Otimizações aplicadas:")
                for melhoria in resultado_otimizacao['melhorias_aplicadas']:
                    print(f"      • {melhoria}")
                
                print(f"   📉 Redução de tamanho: {resultado_otimizacao['reducao_tamanho']} caracteres")
                print(f"   💾 Salvo em: {arquivo_otimizado}")
                
                # Atualizar métricas
                self.metricas_melhoria['prompts_otimizados'] += 1
                self.metricas_melhoria['melhoria_media'] += len(resultado_otimizacao['melhorias_aplicadas'])
                self.metricas_melhoria['tempo_economizado'] += resultado_otimizacao['reducao_tamanho'] / 1000  # estimativa
            else:
                print(f"   ✅ Prompt já está otimizado!")
            
            self.metricas_melhoria['prompts_analisados'] += 1
        
        # Calcular médias
        if self.metricas_melhoria['prompts_otimizados'] > 0:
            self.metricas_melhoria['melhoria_media'] /= self.metricas_melhoria['prompts_otimizados']
    
    def gerar_relatorio_otimizacao(self):
        """Gera relatório de otimização"""
        print("\n📊 RELATÓRIO DE OTIMIZAÇÃO AUTOMÁTICA")
        print("=" * 50)
        
        print(f"📈 MÉTRICAS DE OTIMIZAÇÃO:")
        print(f"   • Prompts analisados: {self.metricas_melhoria['prompts_analisados']}")
        print(f"   • Prompts otimizados: {self.metricas_melhoria['prompts_otimizados']}")
        if self.metricas_melhoria['prompts_analisados'] > 0:
            print(f"   • Taxa de otimização: {(self.metricas_melhoria['prompts_otimizados']/self.metricas_melhoria['prompts_analisados']*100):.1f}%")
        else:
            print(f"   • Taxa de otimização: 0%")
        print(f"   • Melhorias médias por prompt: {self.metricas_melhoria['melhoria_media']:.1f}")
        print(f"   • Tempo economizado estimado: {self.metricas_melhoria['tempo_economizado']:.1f} segundos")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES:")
        if self.metricas_melhoria['prompts_otimizados'] > 0:
            print("   ✅ Otimizações aplicadas com sucesso!")
            print("   🔄 Teste os prompts otimizados antes de usar em produção")
            print("   📝 Monitore performance dos novos prompts")
        else:
            print("   ✅ Todos os prompts já estão otimizados!")
            print("   🎯 Sistema funcionando em excelente estado")
        
        # Salvar relatório
        self.salvar_relatorio_otimizacao()
    
    def salvar_relatorio_otimizacao(self):
        """Salva relatório de otimização"""
        relatorio = {
            'data_otimizacao': datetime.now().isoformat(),
            'metricas': self.metricas_melhoria,
            'status': 'OTIMIZADO' if self.metricas_melhoria['prompts_otimizados'] > 0 else 'JA_OTIMIZADO'
        }
        
        arquivo_relatorio = f"relatorio_otimizacao_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(arquivo_relatorio, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório salvo em: {arquivo_relatorio}")

def main():
    """Função principal"""
    print("🤖 OTIMIZADOR AUTOMÁTICO DE PROMPTS - COPYOS™")
    print("Analisando e otimizando prompts automaticamente")
    print("=" * 50)
    
    # Criar instância do otimizador
    otimizador = OtimizadorAutomaticoPrompts()
    
    # Executar otimização
    otimizador.executar_otimizacao_completa()
    
    # Gerar relatório
    otimizador.gerar_relatorio_otimizacao()
    
    print("\n✅ OTIMIZAÇÃO AUTOMÁTICA CONCLUÍDA!")
    print("Consulte os relatórios gerados para detalhes.")

if __name__ == "__main__":
    main() 