#!/usr/bin/env python3
"""
EXECUTOR AUTOMÁTICO COMPLETO - COPYOS™
Executa automaticamente todo o processo de teste, otimização e validação
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class ExecutorAutomaticoCompleto:
    def __init__(self):
        self.resultados = {}
        self.metricas_gerais = {
            'inicio': datetime.now().isoformat(),
            'fim': None,
            'duracao_total': 0,
            'testes_executados': 0,
            'otimizacoes_aplicadas': 0,
            'status_geral': 'EM_EXECUCAO'
        }
        
    def executar_teste_volume09(self):
        """Executa teste automático do Volume 09"""
        print("🧪 EXECUTANDO TESTE AUTOMÁTICO - VOLUME 09")
        print("-" * 40)
        
        try:
            # Executar script de teste
            resultado = subprocess.run([
                sys.executable, 
                '03_SCRIPTS/teste_automatico_volume09.py'
            ], capture_output=True, text=True, timeout=300)
            
            if resultado.returncode == 0:
                print("✅ Teste do Volume 09 executado com sucesso!")
                self.resultados['teste_volume09'] = {
                    'status': 'SUCESSO',
                    'output': resultado.stdout,
                    'timestamp': datetime.now().isoformat()
                }
                self.metricas_gerais['testes_executados'] += 1
            else:
                print("❌ Erro no teste do Volume 09:")
                print(resultado.stderr)
                self.resultados['teste_volume09'] = {
                    'status': 'ERRO',
                    'error': resultado.stderr,
                    'timestamp': datetime.now().isoformat()
                }
                
        except subprocess.TimeoutExpired:
            print("⏰ Timeout no teste do Volume 09")
            self.resultados['teste_volume09'] = {
                'status': 'TIMEOUT',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            self.resultados['teste_volume09'] = {
                'status': 'ERRO',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def executar_otimizacao_prompts(self):
        """Executa otimização automática de prompts"""
        print("\n🔧 EXECUTANDO OTIMIZAÇÃO AUTOMÁTICA DE PROMPTS")
        print("-" * 40)
        
        try:
            # Executar script de otimização
            resultado = subprocess.run([
                sys.executable, 
                '03_SCRIPTS/otimizador_automatico_prompts.py'
            ], capture_output=True, text=True, timeout=300)
            
            if resultado.returncode == 0:
                print("✅ Otimização de prompts executada com sucesso!")
                self.resultados['otimizacao_prompts'] = {
                    'status': 'SUCESSO',
                    'output': resultado.stdout,
                    'timestamp': datetime.now().isoformat()
                }
                self.metricas_gerais['otimizacoes_aplicadas'] += 1
            else:
                print("❌ Erro na otimização de prompts:")
                print(resultado.stderr)
                self.resultados['otimizacao_prompts'] = {
                    'status': 'ERRO',
                    'error': resultado.stderr,
                    'timestamp': datetime.now().isoformat()
                }
                
        except subprocess.TimeoutExpired:
            print("⏰ Timeout na otimização de prompts")
            self.resultados['otimizacao_prompts'] = {
                'status': 'TIMEOUT',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            self.resultados['otimizacao_prompts'] = {
                'status': 'ERRO',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def validar_estrutura_projeto(self):
        """Valida a estrutura completa do projeto"""
        print("\n📁 VALIDANDO ESTRUTURA DO PROJETO")
        print("-" * 40)
        
        estrutura_esperada = {
            '01_BASE_DE_CONHECIMENTO': [
                'Volume_01_Fundamentos_e_Filosofia.md',
                'Volume_02_Pesquisa_e_Descoberta.md',
                'Volume_03_Mecanismos_e_Oferta.md',
                'Volume_04_VSLs_Teoria_e_Estrutura.md',
                'Volume_05_VSLs_Criacao_e_Execucao.md',
                'Volume_06_Copy_Meio_de_Funil.md',
                'Volume_07_Copy_Final_de_Funil.md',
                'Volume_08_Anuncios_e_Trafego.md',
                'Volume_09_CRO_e_Otimizacao.md'
            ],
            '02_PROMPTS': [
                'PROMPT_COPYOS_CHATGPT_REFINADO.md',
                'PROMPT_COPYOS_GEMINI_REFINADO.md',
                'PROMPT_COPYOS_FEEDBACK_LOOP.md'
            ],
            '03_SCRIPTS': [
                'teste_automatico_volume09.py',
                'otimizador_automatico_prompts.py',
                'executor_automatico_completo.py'
            ]
        }
        
        validacao = {
            'status': 'SUCESSO',
            'pastas_verificadas': 0,
            'arquivos_verificados': 0,
            'arquivos_faltando': [],
            'timestamp': datetime.now().isoformat()
        }
        
        for pasta, arquivos_esperados in estrutura_esperada.items():
            caminho_pasta = f"{pasta}"
            
            if os.path.exists(caminho_pasta):
                print(f"✅ Pasta {pasta} existe")
                validacao['pastas_verificadas'] += 1
                
                for arquivo in arquivos_esperados:
                    caminho_arquivo = f"{caminho_pasta}/{arquivo}"
                    if os.path.exists(caminho_arquivo):
                        print(f"   ✅ {arquivo}")
                        validacao['arquivos_verificados'] += 1
                    else:
                        print(f"   ❌ {arquivo} - FALTANDO")
                        validacao['arquivos_faltando'].append(caminho_arquivo)
            else:
                print(f"❌ Pasta {pasta} - FALTANDO")
                validacao['arquivos_faltando'].extend([f"{caminho_pasta}/{arq}" for arq in arquivos_esperados])
        
        self.resultados['validacao_estrutura'] = validacao
        
        if validacao['arquivos_faltando']:
            print(f"\n⚠️ {len(validacao['arquivos_faltando'])} arquivos estão faltando!")
        else:
            print(f"\n✅ Estrutura completa validada! ({validacao['arquivos_verificados']} arquivos)")
    
    def calcular_metricas_finais(self):
        """Calcula métricas finais do sistema"""
        print("\n📊 CALCULANDO MÉTRICAS FINAIS")
        print("-" * 40)
        
        # Calcular tamanho total da base de conhecimento
        tamanho_total = 0
        arquivos_base = []
        
        for arquivo in os.listdir('01_BASE_DE_CONHECIMENTO'):
            if arquivo.endswith('.md'):
                caminho = f"01_BASE_DE_CONHECIMENTO/{arquivo}"
                tamanho = os.path.getsize(caminho)
                tamanho_total += tamanho
                arquivos_base.append({
                    'arquivo': arquivo,
                    'tamanho': tamanho,
                    'tamanho_kb': tamanho / 1024
                })
        
        # Calcular métricas de qualidade
        sucessos = sum(1 for r in self.resultados.values() if r.get('status') == 'SUCESSO')
        total_testes = len(self.resultados)
        taxa_sucesso = (sucessos / total_testes * 100) if total_testes > 0 else 0
        
        self.metricas_gerais.update({
            'fim': datetime.now().isoformat(),
            'duracao_total': (datetime.now() - datetime.fromisoformat(self.metricas_gerais['inicio'])).total_seconds(),
            'tamanho_base_conhecimento': tamanho_total,
            'tamanho_base_conhecimento_kb': tamanho_total / 1024,
            'arquivos_base_conhecimento': len(arquivos_base),
            'taxa_sucesso': taxa_sucesso,
            'status_geral': 'SUCESSO' if taxa_sucesso >= 80 else 'PRECISA_AJUSTE'
        })
        
        print(f"📈 MÉTRICAS FINAIS:")
        print(f"   • Tamanho da base: {self.metricas_gerais['tamanho_base_conhecimento_kb']:.1f} KB")
        print(f"   • Arquivos na base: {self.metricas_gerais['arquivos_base_conhecimento']}")
        print(f"   • Testes executados: {self.metricas_gerais['testes_executados']}")
        print(f"   • Otimizações aplicadas: {self.metricas_gerais['otimizacoes_aplicadas']}")
        print(f"   • Taxa de sucesso: {self.metricas_gerais['taxa_sucesso']:.1f}%")
        print(f"   • Duração total: {self.metricas_gerais['duracao_total']:.1f} segundos")
    
    def gerar_recomendacoes_finais(self):
        """Gera recomendações finais baseadas nos resultados"""
        print("\n💡 RECOMENDAÇÕES FINAIS")
        print("-" * 40)
        
        recomendacoes = []
        
        # Análise da base de conhecimento
        if self.metricas_gerais['tamanho_base_conhecimento_kb'] >= 180:
            recomendacoes.append("✅ Base de conhecimento está completa e robusta")
        else:
            recomendacoes.append("⚠️ Base de conhecimento pode precisar de expansão")
        
        # Análise dos testes
        if self.metricas_gerais['taxa_sucesso'] >= 80:
            recomendacoes.append("✅ Sistema funcionando em excelente estado")
        elif self.metricas_gerais['taxa_sucesso'] >= 60:
            recomendacoes.append("⚠️ Sistema funcionando bem, mas pode ser otimizado")
        else:
            recomendacoes.append("❌ Sistema precisa de revisão significativa")
        
        # Análise das otimizações
        if self.metricas_gerais['otimizacoes_aplicadas'] > 0:
            recomendacoes.append("✅ Otimizações aplicadas com sucesso")
        else:
            recomendacoes.append("ℹ️ Sistema já estava otimizado")
        
        # Recomendações específicas
        if self.metricas_gerais['taxa_sucesso'] >= 80:
            recomendacoes.append("🚀 Pode prosseguir para implementação em produção")
            recomendacoes.append("📈 Sistema pronto para uso com ChatGPT e Gemini")
        else:
            recomendacoes.append("🔧 Recomenda-se revisar prompts antes de implementar")
            recomendacoes.append("📝 Execute testes adicionais antes de usar em produção")
        
        # Exibir recomendações
        for i, recomendacao in enumerate(recomendacoes, 1):
            print(f"   {i}. {recomendacao}")
        
        return recomendacoes
    
    def salvar_relatorio_final(self):
        """Salva relatório final completo"""
        relatorio_final = {
            'metricas_gerais': self.metricas_gerais,
            'resultados': self.resultados,
            'recomendacoes': self.gerar_recomendacoes_finais(),
            'timestamp': datetime.now().isoformat()
        }
        
        arquivo_relatorio = f"relatorio_execucao_completa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(arquivo_relatorio, 'w', encoding='utf-8') as f:
            json.dump(relatorio_final, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório final salvo em: {arquivo_relatorio}")
        return arquivo_relatorio
    
    def executar_processo_completo(self):
        """Executa todo o processo automaticamente"""
        print("🤖 EXECUTOR AUTOMÁTICO COMPLETO - COPYOS™")
        print("Executando processo completo de validação e otimização")
        print("=" * 60)
        
        # 1. Validar estrutura do projeto
        self.validar_estrutura_projeto()
        
        # 2. Executar teste do Volume 09
        self.executar_teste_volume09()
        
        # 3. Executar otimização de prompts
        self.executar_otimizacao_prompts()
        
        # 4. Calcular métricas finais
        self.calcular_metricas_finais()
        
        # 5. Gerar recomendações
        self.gerar_recomendacoes_finais()
        
        # 6. Salvar relatório final
        arquivo_relatorio = self.salvar_relatorio_final()
        
        print("\n" + "=" * 60)
        print("✅ EXECUÇÃO AUTOMÁTICA COMPLETA CONCLUÍDA!")
        print(f"📊 Relatório salvo em: {arquivo_relatorio}")
        
        # Status final
        if self.metricas_gerais['status_geral'] == 'SUCESSO':
            print("🎉 SISTEMA PRONTO PARA USO EM PRODUÇÃO!")
        else:
            print("⚠️ SISTEMA PRECISA DE AJUSTES ANTES DE USAR EM PRODUÇÃO")

def main():
    """Função principal"""
    executor = ExecutorAutomaticoCompleto()
    executor.executar_processo_completo()

if __name__ == "__main__":
    main() 