# 📋 Padronização de Nomenclatura - COPYOS™

## 🎯 **PRINCÍPIOS GERAIS**

### **1. Estrutura de Diretórios**
- **Numeração**: `01_`, `02_`, `03_` para ordem lógica
- **Nomes Descritivos**: Em português, claros e específicos
- **Consistência**: Mesmo padrão em todo o projeto

### **2. Nomenclatura de Arquivos**
- **CamelCase**: Para nomes compostos
- **Underscore**: Para separação de palavras
- **Extensões**: `.md` para documentação, `.py` para scripts, `.json` para dados

## 📁 **ESTRUTURA PADRONIZADA**

### **Diretórios Principais**
```
COPYOS_FINAL/
├── 01_BASE_DE_CONHECIMENTO/     # Base de conhecimento estruturada
├── 02_PROMPTS/                  # Prompts para diferentes LLMs
├── 03_SCRIPTS/                  # Scripts de automação
├── 04_BLUEPRINTS/               # Blueprints processados
├── 05_EVIDENCIAS/               # Evidências extraídas
├── 06_QA/                       # Relatórios de QA
├── 07_BACKUP_LIMPEZA/           # Backup da limpeza (temporário)
├── 08_DADOS_BRUTOS/             # Dados brutos (ignorados pelo Git)
└── 09_MATERIAL_ORIGINAL/        # Material original (ignorado pelo Git)
```

### **Arquivos de Configuração**
```
COPYOS_FINAL/
├── README.md                   # Documentação principal
├── SETUP.md                    # Guia de configuração
├── RELATORIO_FINAL.md          # Relatório de validação
├── .gitignore                  # Configuração do Git
├── .cursorrules                # Configuração do Cursor Agent
└── PADRONIZACAO_NOMENCLATURA.md # Este arquivo
```

## 📚 **Base de Conhecimento (01_BASE_DE_CONHECIMENTO/)**

### **Padrão de Nomenclatura**
```
Volume_XX_Titulo_Principal.md
```

### **Exemplos**
- `Volume_01_Fundamentos_e_Filosofia.md`
- `Volume_02_Pesquisa_e_Descoberta.md`
- `Volume_03_Mecanismos_e_Oferta.md`
- `Volume_04_VSLs_Teoria_e_Estrutura.md`
- `Volume_05_VSLs_Criacao_e_Execucao.md`
- `Volume_06_Copy_Meio_de_Funil.md`
- `Volume_07_Copy_Final_de_Funil.md`
- `Volume_08_Anuncios_e_Trafego.md`
- `Volume_09_CRO_e_Otimizacao.md`

### **Regras**
- **XX**: Número com zero à esquerda (01, 02, 03...)
- **Titulo**: Nome descritivo em português
- **Underscore**: Separação entre palavras
- **Extensão**: `.md` para Markdown

## 🤖 **Prompts (02_PROMPTS/)**

### **Padrão de Nomenclatura**
```
PROMPT_COPYOS_[PLATAFORMA]_[TIPO].md
```

### **Exemplos**
- `PROMPT_COPYOS_CHATGPT.md` - Prompt para ChatGPT
- `PROMPT_COPYOS_GEMINI.md` - Prompt para Gemini
- `PROMPT_COPYOS_FEEDBACK_LOOP.md` - Sistema de feedback
- `CHANGELOG_MELHORIAS.md` - Histórico de melhorias

### **Regras**
- **PROMPT_COPYOS**: Prefixo padrão
- **[PLATAFORMA]**: Nome da plataforma (CHATGPT, GEMINI)
- **[TIPO]**: Tipo específico (FEEDBACK_LOOP)
- **Extensão**: `.md` para Markdown

## 🔧 **Scripts (03_SCRIPTS/)**

### **Padrão de Nomenclatura**
```
[acao]_[objeto]_[tipo].py
```

### **Exemplos**
- `conectar_github.py` - Conectar ao GitHub
- `limpeza_padronizacao.py` - Limpeza e padronização
- `processador_todos_volumes.py` - Processar volumes
- `atualizador_base_conhecimento.py` - Atualizar base
- `blueprint_profundo_com_metas.py` - Gerar blueprints
- `executor_automatico_completo.py` - Execução automática
- `otimizador_automatico_prompts.py` - Otimizar prompts
- `teste_automatico_volume09.py` - Testar volume específico

### **Regras**
- **Verbo no infinitivo**: conectar, limpar, processar
- **Underscore**: Separação entre palavras
- **Descrição clara**: Objeto e tipo de ação
- **Extensão**: `.py` para Python

## 📊 **Dados e Evidências**

### **Blueprints (04_BLUEPRINTS/)**
```
Volume_XX.md
```

### **Evidências (05_EVIDENCIAS/)**
```
Volume_XX.json
```

### **QA (06_QA/)**
```
Volume_XX_QA.json
```

## 🚫 **Arquivos Excluídos**

### **Por .gitignore**
- `08_DADOS_BRUTOS/` - Dados brutos (13MB)
- `09_MATERIAL_ORIGINAL/` - Material original (776MB)
- `05_EVIDENCIAS/` - Evidências extraídas (7MB)
- `.DS_Store` - Arquivos de sistema macOS
- `07_BACKUP_LIMPEZA/` - Backup temporário

### **Arquivos Removidos na Limpeza**
- Arquivos redundantes (múltiplas versões)
- Scripts temporários e de debug
- Arquivos vazios ou desnecessários

## ✅ **Validação da Padronização**

### **Critérios de Qualidade**
1. **Consistência**: Mesmo padrão em todo o projeto
2. **Clareza**: Nomes autoexplicativos
3. **Organização**: Estrutura lógica e hierárquica
4. **Manutenibilidade**: Fácil de entender e modificar

### **Resultado da Limpeza**
- ✅ **79 arquivos** organizados
- ✅ **222KB** de dados estruturados
- ✅ **9 volumes** padronizados
- ✅ **Nomenclatura consistente** em todo o projeto

## 📋 **Checklist de Padronização**

### **Diretórios**
- [x] Numeração sequencial (01_, 02_, 03_)
- [x] Nomes descritivos em português
- [x] Estrutura hierárquica clara

### **Arquivos**
- [x] Nomenclatura consistente
- [x] Extensões apropriadas
- [x] Sem redundâncias
- [x] Sem arquivos temporários

### **Documentação**
- [x] README.md principal
- [x] SETUP.md para configuração
- [x] RELATORIO_FINAL.md para validação
- [x] PADRONIZACAO_NOMENCLATURA.md para referência

---

**🎯 COPYOS™ está 100% padronizado e pronto para uso!** 