#!/usr/bin/env python3
"""
BLUEPRINT PROFUNDO COM METAS RÍGIDAS - COPYOS™
Implementação da metodologia de duas passadas para garantir profundidade máxima
Baseado no feedback do GPT e Gemini sobre densidade oscilante
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any

class BlueprintProfundo:
    def __init__(self):
        self.metas_minimas = {
            'objetivo_estrategico': {
                'min_frases': 2,
                'max_frases': 3,
                'requer': ['transformacao_prometida', 'contexto_volume']
            },
            'modelos_mentais': {
                'min_bullets': 7,
                'requer': ['explicacao_impacto_decisao_compra']
            },
            'voz_filosofia_autor': {
                'min_citacoes': 3,
                'requer': ['citacoes_literais', 'paragrafo_tom_estilo']
            },
            'frameworks_checklists': {
                'min_fluxos': 2,
                'requer': ['condicoes_entrada_saida', 'passo_a_passo']
            },
            'anti_exemplos_armadilhas': {
                'min_casos': 2,
                'requer': ['erro_comum', 'como_evitar']
            },
            'metricas_kpis': {
                'min_metricas': 5,
                'requer': ['como_medir', 'limiares']
            },
            'templates_prompts': {
                'min_templates': 3,
                'requer': ['placeholders', 'pronto_uso']
            },
            'estudos_caso_swipe': {
                'min_casos': 2,
                'requer': ['sucesso', 'falha', 'aprendizagens']
            },
            'checklist_implementacao': {
                'requer': ['quem_faz', 'ferramenta', 'dor', 'definicao_pronto']
            },
            'bibliografia_referencias': {
                'requer': ['mapeamento_bruto', 'volume_pagina_linha']
            }
        }
        
        self.blueprint_template = """
# VOLUME {numero}: {titulo}

## 🎯 OBJETIVO ESTRATÉGICO
**Transformação Prometida**: [2-3 frases sobre o que o usuário vai conseguir]
**Contexto do Volume**: [Contexto específico e aplicação prática]

## 🧠 MODELOS MENTAIS & FILOSOFIA
**≥7 bullets com explicação de impacto na decisão de compra:**

1. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
2. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
3. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
4. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
5. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
6. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]
7. **[Modelo Mental]**: [Explicação de como afeta decisão de compra]

## 🎭 VOZ E FILOSOFIA DO AUTOR
**≥3 citações literais (com aspas):**

> "[Citação literal 1 do autor]"
> "[Citação literal 2 do autor]"
> "[Citação literal 3 do autor]"

**Tom e Estilo**: [1 parágrafo descrevendo o tom, estilo e filosofia do autor]

## ⚙️ FRAMEWORKS/CHECKLISTS OPERACIONAIS
**≥2 fluxos passo-a-passo com condições de entrada/saída:**

### Framework 1: [Nome]
**Condições de Entrada**: [Quando usar]
**Passo 1**: [Ação específica]
**Passo 2**: [Ação específica]
**Passo 3**: [Ação específica]
**Condições de Saída**: [Como saber que está pronto]

### Framework 2: [Nome]
**Condições de Entrada**: [Quando usar]
**Passo 1**: [Ação específica]
**Passo 2**: [Ação específica]
**Passo 3**: [Ação específica]
**Condições de Saída**: [Como saber que está pronto]

## ⚠️ ANTI-EXEMPLOS E ARMADILHAS
**≥2 casos de erro comum + como evitar:**

### Armadilha 1: [Nome do erro]
**O que acontece**: [Descrição do erro]
**Por que acontece**: [Causa raiz]
**Como evitar**: [Solução específica]

### Armadilha 2: [Nome do erro]
**O que acontece**: [Descrição do erro]
**Por que acontece**: [Causa raiz]
**Como evitar**: [Solução específica]

## 📊 MÉTRICAS E KPIS
**≥5 métricas com "como medir" e "limiares":**

1. **[Métrica]**: [Fórmula/Como medir] | Limiar: [Valor]
2. **[Métrica]**: [Fórmula/Como medir] | Limiar: [Valor]
3. **[Métrica]**: [Fórmula/Como medir] | Limiar: [Valor]
4. **[Métrica]**: [Fórmula/Como medir] | Limiar: [Valor]
5. **[Métrica]**: [Fórmula/Como medir] | Limiar: [Valor]

## 📝 TEMPLATES/PROMPTS
**≥3 templates prontos (com placeholders):**

### Template 1: [Nome]
```
[Template com placeholders EXEMPLO]
```

### Template 2: [Nome]
```
[Template com placeholders EXEMPLO]
```

### Template 3: [Nome]
```
[Template com placeholders EXEMPLO]
```

## 📚 ESTUDOS DE CASO/SWIPE
**≥2 casos (melhor se 1 sucesso + 1 falha) com aprendizagens:**

### Caso de Sucesso: [Nome]
**Contexto**: [Situação inicial]
**Ação**: [O que foi feito]
**Resultado**: [Métricas de sucesso]
**Aprendizagens**: [3-5 insights chave]

### Caso de Falha: [Nome]
**Contexto**: [Situação inicial]
**Ação**: [O que foi feito]
**Resultado**: [O que deu errado]
**Aprendizagens**: [3-5 insights chave]

## ✅ CHECKLIST DE IMPLEMENTAÇÃO
**Lista executável (quem faz, ferramenta, DOR, definição de "pronto"):**

- [ ] **Tarefa 1**: [Descrição] | **Quem**: [Responsável] | **Ferramenta**: [Ferramenta] | **DOR**: [Definition of Ready] | **Pronto**: [Definition of Done]
- [ ] **Tarefa 2**: [Descrição] | **Quem**: [Responsável] | **Ferramenta**: [Ferramenta] | **DOR**: [Definition of Ready] | **Pronto**: [Definition of Done]
- [ ] **Tarefa 3**: [Descrição] | **Quem**: [Responsável] | **Ferramenta**: [Ferramenta] | **DOR**: [Definition of Ready] | **Pronto**: [Definition of Done]

## 📖 BIBLIOGRAFIA/REFERÊNCIAS
**Mapeamento para trechos do bruto + volume/página/linha quando possível:**

- [Referência 1]: Volume [X], Página [Y], Linha [Z] - [Descrição do conteúdo]
- [Referência 2]: Volume [X], Página [Y], Linha [Z] - [Descrição do conteúdo]
- [Referência 3]: Volume [X], Página [Y], Linha [Z] - [Descrição do conteúdo]

---

## 🔍 LACUNAS IDENTIFICADAS
**Seções que não atingiram metas mínimas:**

- [ ] **Seção**: [Nome] | **Meta**: [Meta não atingida] | **Ação**: [O que fazer]
- [ ] **Seção**: [Nome] | **Meta**: [Meta não atingida] | **Ação**: [O que fazer]

## ✅ VALIDAÇÃO DE QUALIDADE
**Critérios de aceite verificados:**

- [ ] Todas as seções preenchidas
- [ ] ≥3 citações literais presentes
- [ ] ≥2 anti-exemplos/armadilhas
- [ ] ≥5 KPIs com fórmula/onde medir
- [ ] ≥3 templates com placeholders
- [ ] Links internos para modelos/templates
- [ ] Checklist executável com DOR/DOD
- [ ] Mapeamento bibliográfico completo
"""

    def extrair_evidencias_canonicas(self, arquivo_bruto: str) -> Dict[str, Any]:
        """
        PASSADA 1: Extração Canônica
        Extrai evidências brutas sem interpretar ou resumir
        """
        print(f"🔍 PASSADA 1: Extraindo evidências canônicas de {arquivo_bruto}")
        
        try:
            with open(arquivo_bruto, 'r', encoding='utf-8') as f:
                conteudo = f.read()
        except FileNotFoundError:
            print(f"❌ Arquivo {arquivo_bruto} não encontrado")
            return {}
        
        evidencias = {
            'citacoes_literais': [],
            'listas_numeros': [],
            'exemplos_casos': [],
            'anti_exemplos': [],
            'frameworks_processos': [],
            'metricas_kpis': [],
            'templates_prompts': [],
            'armadilhas_erros': [],
            'checklists': [],
            'referencias_paginas': []
        }
        
        # Extrair citações literais (texto entre aspas)
        import re
        citacoes = re.findall(r'"([^"]*)"', conteudo)
        evidencias['citacoes_literais'] = [c for c in citacoes if len(c) > 20]
        
        # Extrair listas e números
        linhas = conteudo.split('\n')
        for i, linha in enumerate(linhas):
            # Listas numeradas
            if re.match(r'^\d+\.', linha.strip()):
                evidencias['listas_numeros'].append({
                    'linha': i + 1,
                    'conteudo': linha.strip()
                })
            
            # Números e métricas
            numeros = re.findall(r'\d+(?:\.\d+)?%?', linha)
            if numeros and any(palavra in linha.lower() for palavra in ['ctr', 'cpa', 'roas', 'conversao', 'venda']):
                evidencias['metricas_kpis'].append({
                    'linha': i + 1,
                    'conteudo': linha.strip(),
                    'numeros': numeros
                })
            
            # Anti-exemplos e armadilhas
            if any(palavra in linha.lower() for palavra in ['nao faca', 'evite', 'erro', 'problema', 'falha']):
                evidencias['anti_exemplos'].append({
                    'linha': i + 1,
                    'conteudo': linha.strip()
                })
            
            # Templates e prompts
            if any(palavra in linha.lower() for palavra in ['template', 'prompt', 'modelo', 'exemplo']):
                evidencias['templates_prompts'].append({
                    'linha': i + 1,
                    'conteudo': linha.strip()
                })
        
        print(f"✅ Extraídas {len(evidencias['citacoes_literais'])} citações literais")
        print(f"✅ Extraídos {len(evidencias['listas_numeros'])} itens de lista")
        print(f"✅ Extraídos {len(evidencias['metricas_kpis'])} KPIs")
        print(f"✅ Extraídos {len(evidencias['anti_exemplos'])} anti-exemplos")
        
        return evidencias
    
    def validar_metas_minimas(self, volume_gerado: str) -> Dict[str, Any]:
        """
        QA Automático: Valida se o volume atende às metas mínimas
        """
        print("🔍 Validando metas mínimas...")
        
        validacao = {
            'aprovado': True,
            'lacunas': [],
            'metricas': {}
        }
        
        # Contar citações literais
        citacoes = volume_gerado.count('> "')
        validacao['metricas']['citacoes'] = citacoes
        if citacoes < 3:
            validacao['aprovado'] = False
            validacao['lacunas'].append(f"Citações literais: {citacoes}/3")
        
        # Contar anti-exemplos
        anti_exemplos = volume_gerado.count('### Armadilha')
        validacao['metricas']['anti_exemplos'] = anti_exemplos
        if anti_exemplos < 2:
            validacao['aprovado'] = False
            validacao['lacunas'].append(f"Anti-exemplos: {anti_exemplos}/2")
        
        # Contar KPIs
        kpis = volume_gerado.count('**[Métrica]**:')
        validacao['metricas']['kpis'] = kpis
        if kpis < 5:
            validacao['aprovado'] = False
            validacao['lacunas'].append(f"KPIs: {kpis}/5")
        
        # Contar templates
        templates = volume_gerado.count('### Template')
        validacao['metricas']['templates'] = templates
        if templates < 3:
            validacao['aprovado'] = False
            validacao['lacunas'].append(f"Templates: {templates}/3")
        
        # Verificar seções obrigatórias
        secoes_obrigatorias = [
            'OBJETIVO ESTRATÉGICO',
            'MODELOS MENTAIS',
            'VOZ E FILOSOFIA',
            'FRAMEWORKS/CHECKLISTS',
            'ANTI-EXEMPLOS',
            'MÉTRICAS E KPIS',
            'TEMPLATES/PROMPTS',
            'ESTUDOS DE CASO',
            'CHECKLIST DE IMPLEMENTAÇÃO',
            'BIBLIOGRAFIA/REFERÊNCIAS'
        ]
        
        for secao in secoes_obrigatorias:
            if secao not in volume_gerado:
                validacao['aprovado'] = False
                validacao['lacunas'].append(f"Seção ausente: {secao}")
        
        return validacao
    
    def gerar_relatorio_qa(self, validacao: Dict[str, Any], volume: str) -> str:
        """
        Gera relatório detalhado de QA
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        relatorio = f"""
# RELATÓRIO DE QA - VOLUME {volume}
**Data**: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

## 📊 RESULTADO DA VALIDAÇÃO
**Status**: {'✅ APROVADO' if validacao['aprovado'] else '❌ REPROVADO'}

## 📈 MÉTRICAS ATINGIDAS
- **Citações literais**: {validacao['metricas'].get('citacoes', 0)}/3
- **Anti-exemplos**: {validacao['metricas'].get('anti_exemplos', 0)}/2
- **KPIs**: {validacao['metricas'].get('kpis', 0)}/5
- **Templates**: {validacao['metricas'].get('templates', 0)}/3

## ⚠️ LACUNAS IDENTIFICADAS
"""
        
        if validacao['lacunas']:
            for lacuna in validacao['lacunas']:
                relatorio += f"- ❌ {lacuna}\n"
        else:
            relatorio += "- ✅ Nenhuma lacuna identificada\n"
        
        relatorio += f"""
## 🎯 PRÓXIMOS PASSOS
"""
        
        if validacao['aprovado']:
            relatorio += "- ✅ Volume aprovado para produção\n"
            relatorio += "- ✅ Pode ser usado em ChatGPT/Gemini\n"
        else:
            relatorio += "- 🔄 Revisar e complementar seções com lacunas\n"
            relatorio += "- 🔄 Re-executar validação após correções\n"
        
        return relatorio
    
    def processar_volume_profundo(self, numero_volume: str, titulo: str, arquivo_bruto: str) -> Dict[str, Any]:
        """
        Processa volume completo com metodologia de duas passadas
        """
        print(f"🚀 PROCESSANDO VOLUME {numero_volume}: {titulo}")
        print("=" * 60)
        
        # PASSADA 1: Extração Canônica
        evidencias = self.extrair_evidencias_canonicas(arquivo_bruto)
        
        # Salvar evidências em JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_evidencias = f"evidencias_volume{numero_volume}_{timestamp}.json"
        
        with open(json_evidencias, 'w', encoding='utf-8') as f:
            json.dump(evidencias, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Evidências salvas em: {json_evidencias}")
        
        # PASSADA 2: Síntese com Metas (simulada)
        print("🔧 PASSADA 2: Síntese com metas (requer interação manual)")
        print("📝 Use o template do blueprint com as evidências extraídas")
        
        # Template do blueprint
        blueprint = self.blueprint_template.format(
            numero=numero_volume,
            titulo=titulo
        )
        
        # Salvar blueprint
        arquivo_blueprint = f"blueprint_volume{numero_volume}_{timestamp}.md"
        with open(arquivo_blueprint, 'w', encoding='utf-8') as f:
            f.write(blueprint)
        
        print(f"📋 Blueprint salvo em: {arquivo_blueprint}")
        
        return {
            'evidencias': evidencias,
            'json_evidencias': json_evidencias,
            'blueprint': arquivo_blueprint,
            'timestamp': timestamp
        }

def main():
    """
    Função principal para processar Volume 01 como piloto
    """
    print("🎯 BLUEPRINT PROFUNDO COM METAS RÍGIDAS - COPYOS™")
    print("Implementação da metodologia de duas passadas")
    print("=" * 60)
    
    blueprint = BlueprintProfundo()
    
    # Processar Volume 01 como piloto
    resultado = blueprint.processar_volume_profundo(
        numero_volume="01",
        titulo="Fundamentos e Filosofia",
        arquivo_bruto="04_DADOS_BRUTOS/texto_bruto/Volume_01_Fundamentos_e_Filosofia_BRUTO.txt"
    )
    
    print("\n" + "=" * 60)
    print("✅ PROCESSAMENTO CONCLUÍDO!")
    print(f"📊 Evidências extraídas: {resultado['json_evidencias']}")
    print(f"📋 Blueprint gerado: {resultado['blueprint']}")
    print("\n🎯 PRÓXIMOS PASSOS:")
    print("1. Revisar evidências extraídas")
    print("2. Preencher blueprint com evidências")
    print("3. Executar validação de QA")
    print("4. Aprovar ou corrigir lacunas")

if __name__ == "__main__":
    main() 