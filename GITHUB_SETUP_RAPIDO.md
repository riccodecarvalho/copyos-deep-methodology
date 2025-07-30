# 🚀 CONEXÃO RÁPIDA COM GITHUB - COPYOS™

## ⚡ MÉTODO MAIS FÁCIL (5 minutos)

### 1. **Criar Repositório no GitHub**
- Acesse: https://github.com/new
- **Nome**: `copyos-deep-methodology`
- **Descrição**: `COPYOS™ - Sistema de Copywriting com Metodologia Profunda`
- **Público** ✅
- **NÃO** inicialize com README ❌
- Clique em **"Create repository"**

### 2. **Conectar Localmente**
Execute estes comandos no terminal:

```bash
# Navegar para a pasta do projeto
cd "COPYOS_FINAL"

# Inicializar Git (se não estiver inicializado)
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: COPYOS™ with deep methodology"

# Conectar ao repositório remoto
git remote add origin https://github.com/SEU_USUARIO/copyos-deep-methodology.git

# Renomear branch para main
git branch -M main

# Fazer push
git push -u origin main
```

### 3. **Usar no Cursor Online**
- Acesse: https://cursor.sh
- Clique em **"Open Repository"**
- Selecione o repositório `copyos-deep-methodology`
- Pronto! O `.cursorrules` será carregado automaticamente

---

## 🔧 MÉTODO AUTOMÁTICO (se tiver GitHub CLI)

Se você já tem o GitHub CLI instalado:

```bash
# Navegar para a pasta
cd "COPYOS_FINAL"

# Executar script automático
python3 03_SCRIPTS/conectar_github.py
```

---

## 📋 VERIFICAÇÃO RÁPIDA

Após a conexão, verifique se:

✅ **Arquivos principais estão no GitHub:**
- `README.md`
- `01_BASE_DE_CONHECIMENTO/` (9 volumes)
- `02_PROMPTS/` (prompts para ChatGPT/Gemini)
- `03_SCRIPTS/` (scripts de automação)
- `.cursorrules` (configuração do Cursor Agent)

✅ **Arquivos grandes estão ignorados:**
- `04_DADOS_BRUTOS/` ❌
- `05_MATERIAL_ORIGINAL/` ❌
- `evidencias/` ❌

---

## 🎯 PRÓXIMOS PASSOS

1. **Acesse o repositório**: https://github.com/SEU_USUARIO/copyos-deep-methodology
2. **Configure o Cursor Agent online**
3. **Teste os prompts** com o CopyOS™
4. **Compartilhe** o repositório se necessário

---

## ❓ PROBLEMAS COMUNS

**Erro: "Repository already exists"**
- Use um nome diferente: `copyos-deep-methodology-v2`

**Erro: "Authentication failed"**
- Configure suas credenciais do GitHub:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

**Erro: "Large files"**
- O `.gitignore` já está configurado para ignorar arquivos grandes
- Se ainda houver problemas, use: `git add . && git commit -m "Initial commit"` 