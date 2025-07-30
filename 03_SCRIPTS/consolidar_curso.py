import os
import re
import time
import docx
import PyPDF2
import zipfile
import google.generativeai as genai
from pathlib import Path

# --- CONFIGURAÇÃO INICIAL ---
GOOGLE_API_KEY = 'AIzaSyCGeXVt5xZ-eXYG8eGUdraMUMq-mY-lqNQ'
PASTA_RAIZ = './curso'
PASTA_DESTINO = './base_de_conhecimento_final'
# -----------------------------

genai.configure(api_key=GOOGLE_API_KEY)

# --- DEFINIÇÃO DOS 8 VOLUMES TEMÁTICOS ---
VOLUMES = {
    'Volume_01_Fundamentos_e_Filosofia': [
        '01-INTRO AND OVERVIEW',
        '08-RMBC II MID-COURSE RECAP'
    ],
    'Volume_02_Pesquisa_e_Descoberta': [
        '02-DEEP RESEARCH',
        '13-THE 15 FACTORS THAT DETERMINE YOUR FUNNEL STRUCTURE'
    ],
    'Volume_03_Mecanismos_e_Oferta': [
        '03-UNIQUE MECHANISMS',
        '14-UPSELLS'
    ],
    'Volume_04_VSLs_Teoria_e_Estrutura': [
        '04-VSLS SECTION I-Structure Theory and Examples'
    ],
    'Volume_05_VSLs_Criacao_e_Execucao': [
        '05-BRIEF 20',
        '06-61 VSL SECTION II- Claude VSL Projects Setup',
        '07-62 VSL SECTION II- VSL Creation Examples'
    ],
    'Volume_06_Copy_Meio_de_Funil': [
        '09-ADVERTORIALS',
        '10-PDPS'
    ],
    'Volume_07_Copy_Fim_de_Funil': [
        '11-CHECKOUTS',
        '15-EMAIL MARKETING'
    ],
    'Volume_08_Anuncios_e_Trafego': [
        '12-ADS',
        '16-BONUSES'
    ]
}

# --- FUNÇÕES DE EXTRAÇÃO DE TEXTO ---
def extrair_texto_srt(caminho):
    """Extrai texto de arquivos .srt"""
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        # Remove timestamps e números de legenda
        linhas = conteudo.split('\n')
        texto_limpo = []
        
        for linha in linhas:
            linha = linha.strip()
            # Pula linhas vazias, números e timestamps
            if (linha and 
                not linha.isdigit() and 
                not re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', linha)):
                texto_limpo.append(linha)
        
        return ' '.join(texto_limpo)
    except Exception as e:
        print(f"  Erro ao ler {caminho}: {e}")
        return ""

def extrair_texto_pdf(caminho):
    """Extrai texto de arquivos .pdf"""
    try:
        with open(caminho, 'rb') as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            texto = ""
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
        return texto
    except Exception as e:
        print(f"  Erro ao ler {caminho}: {e}")
        return ""

def extrair_texto_docx(caminho):
    """Extrai texto de arquivos .docx"""
    try:
        doc = docx.Document(caminho)
        texto = ""
        for paragrafo in doc.paragraphs:
            texto += paragrafo.text + "\n"
        return texto
    except Exception as e:
        print(f"  Erro ao ler {caminho}: {e}")
        return ""

def extrair_texto_zip(caminho):
    """Extrai texto de arquivos dentro de ZIPs"""
    try:
        texto_total = ""
        with zipfile.ZipFile(caminho, 'r') as zip_ref:
            for nome_arquivo in zip_ref.namelist():
                if nome_arquivo.endswith(('.docx', '.pdf')):
                    # Extrai temporariamente o arquivo
                    with zip_ref.open(nome_arquivo) as arquivo_zip:
                        # Cria arquivo temporário
                        temp_path = f"temp_{nome_arquivo.replace('/', '_')}"
                        with open(temp_path, 'wb') as temp_file:
                            temp_file.write(arquivo_zip.read())
                        
                        # Processa o arquivo temporário
                        if nome_arquivo.endswith('.docx'):
                            texto_total += extrair_texto_docx(temp_path) + "\n"
                        elif nome_arquivo.endswith('.pdf'):
                            texto_total += extrair_texto_pdf(temp_path) + "\n"
                        
                        # Remove arquivo temporário
                        os.remove(temp_path)
        return texto_total
    except Exception as e:
        print(f"  Erro ao ler {caminho}: {e}")
        return ""

def processar_arquivo(caminho):
    """Processa um arquivo individual baseado na extensão"""
    # Verifica se o nome do arquivo (não o caminho completo) começa com '.'
    nome_arquivo = os.path.basename(caminho)
    if nome_arquivo.startswith('.'):  # Ignora arquivos ocultos
        return ""
    
    extensao = caminho.lower().split('.')[-1]
    
    if extensao == 'srt':
        return extrair_texto_srt(caminho)
    elif extensao == 'pdf':
        return extrair_texto_pdf(caminho)
    elif extensao == 'docx':
        return extrair_texto_docx(caminho)
    elif extensao == 'zip':
        return extrair_texto_zip(caminho)
    else:
        return ""

def processar_pasta_recursivamente(caminho_pasta):
    """Processa todos os arquivos em uma pasta e subpastas"""
    texto_total = ""
    
    if not os.path.exists(caminho_pasta):
        print(f"  Pasta não encontrada: {caminho_pasta}")
        return texto_total
    
    for raiz, dirs, arquivos in os.walk(caminho_pasta):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            print(f"  Lendo arquivo: {arquivo}...")
            texto_arquivo = processar_arquivo(caminho_completo)
            if texto_arquivo:
                texto_total += f"\n\n--- {arquivo} ---\n{texto_arquivo}"
    
    return texto_total

# --- PROMPT HÍBRIDO FINAL OTIMIZADO ---
def gerar_prompt_volume(nome_volume, modulos, texto_completo):
    return f"""
Como Arquiteto de Conversão e Copywriter Sênior, sua missão é criar um "cérebro" de conhecimento especializado para o CopyOS™ - um agente de IA autônomo que deve ser capaz de gerar copy de alta conversão sem intervenção manual.

**CONTEXTO ESPECÍFICO:**
Você está processando o {nome_volume} que contém os seguintes módulos do curso RMBC II:
{', '.join(modulos)}

**OBJETIVO:**
Transformar este conhecimento em uma base de dados executiva que permita ao CopyOS™:
1. Analisar pedidos de copywriting (ex: "preciso de uma VSL")
2. Raciocinar com base nos frameworks RMBC II
3. Executar tarefas criativas aplicando metodologias corretas automaticamente

**INSTRUÇÕES CRÍTICAS:**
Combine estratégia profunda com implementação específica. Foque em INFORMAÇÕES EXECUTÁVEIS, TEMPLATES PRÁTICOS e CHECKLISTS DE IMPLEMENTAÇÃO. NÃO RESUMIR. Em vez disso, EXTRAIR, ORGANIZAR e PRESERVAR o máximo de informações práticas possíveis.

**ESTRUTURA OBRIGATÓRIA DO OUTPUT:**

# **{nome_volume.replace('_', ' ').title()}**

## 🎯 **CONTEXTO E OBJETIVOS EXECUTIVOS**
[Defina claramente o propósito estratégico deste volume e como ele se conecta ao copywriting de alta conversão]

## 🧠 **PRINCIPAIS MODELOS MENTAIS E FILOSOFIA**
[Extraia os princípios fundamentais, crenças e abordagens mentais que guiam as decisões de copywriting nesta área]

## 🎭 **VOZ E FILOSOFIA DO AUTOR**
[Capture o tom, estilo e perspectiva única do Stefan Georgi. Como ele pensa, como ele ensina, qual sua filosofia sobre copywriting]

## 🛠️ **METODOLOGIAS E PROCESSOS DETALHADOS**
[Processos passo-a-passo, frameworks específicos, metodologias testadas]

## 📝 **PROMPTS E TEMPLATES PRÁTICOS**
[Templates literais, prompts específicos, estruturas reutilizáveis]

## 💼 **EXEMPLOS E CASOS DE ESTUDO COMPLETOS**
[Exemplos literais de copy, casos reais, demonstrações práticas]

## 🎯 **FRAMEWORKS E MODELOS APLICÁVEIS**
[Modelos específicos, frameworks testados, estruturas comprovadas]

## ⚠️ **ARMADILHAS E SOLUÇÕES**
[Problemas comuns, erros frequentes, soluções rápidas]

## 🔧 **FERRAMENTAS E RECURSOS**
[Ferramentas específicas, recursos online, KPIs relevantes]

## 📚 **GLOSSÁRIO TÉCNICO**
[Termos específicos, definições, nomenclatura do curso]

## ❓ **PERGUNTAS PRÁTICAS E RESPOSTAS**
[Perguntas frequentes com respostas executáveis]

## 🎯 **MODOS DE OPERAÇÃO SUGERIDOS**
[Como o CopyOS™ deve usar este conhecimento: Diagnóstico, Criação, Revisão, Otimização, Estratégia]

## 📝 **PLACEHOLDERS E VARIÁVEIS DINÂMICAS**
[Variáveis que podem ser substituídas dinamicamente: [Nome do Produto], [Preço], etc.]

## 🏗️ **CHECKLIST DE IMPLEMENTAÇÃO (BLUEPRINT)**
[Checklist executável para designers/desenvolvedores implementarem o conhecimento]

## 🔗 **REFERÊNCIAS CRUZADAS**
[Conceitos relacionados em outros volumes, conexões importantes]

---

**TEXTO COMPLETO DOS MÓDULOS:**
{texto_completo}

**IMPORTANTE:** Mantenha a densidade de informação máxima. Cada seção deve conter informações específicas, exemplos literais e instruções executáveis. O objetivo é que o CopyOS™ possa usar este conhecimento para gerar copy de alta qualidade sem intervenção manual.
"""

# --- FUNÇÃO PRINCIPAL DE CONSOLIDAÇÃO ---
def consolidar_volume(nome_volume, modulos):
    """Consolida múltiplos módulos em um volume temático"""
    print(f"\n{'='*60}")
    print(f"CONSOLIDANDO: {nome_volume}")
    print(f"Módulos: {', '.join(modulos)}")
    print(f"{'='*60}")
    
    # Extrai texto de todos os módulos
    texto_total = ""
    for modulo in modulos:
        caminho_modulo = os.path.join(PASTA_RAIZ, modulo)
        print(f"\nProcessando módulo: {modulo}")
        texto_modulo = processar_pasta_recursivamente(caminho_modulo)
        texto_total += f"\n\n{'='*50}\nMÓDULO: {modulo}\n{'='*50}\n{texto_modulo}"
    
    print(f"\nTotal de caracteres extraídos: {len(texto_total)}")
    
    # Gera prompt específico para o volume
    prompt = gerar_prompt_volume(nome_volume, modulos, texto_total)
    
    # Chama Gemini 2.5 Pro
    try:
        modelo = genai.GenerativeModel('gemini-2.0-flash-exp')
        resposta = modelo.generate_content(prompt)
        
        # Salva o resultado
        nome_arquivo = f"{nome_volume}.md"
        caminho_destino = os.path.join(PASTA_DESTINO, nome_arquivo)
        
        with open(caminho_destino, 'w', encoding='utf-8') as arquivo:
            arquivo.write(resposta.text)
        
        print(f"✅ Volume salvo: {nome_arquivo}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao processar {nome_volume}: {e}")
        return False

# --- FUNÇÃO PRINCIPAL ---
def main():
    """Função principal que executa a consolidação de todos os volumes"""
    print("🧠 COPYOS™ - CONSOLIDAÇÃO TEMÁTICA INTELLIGENTE")
    print("="*60)
    
    # Cria pasta de destino
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    
    # Processa cada volume
    sucessos = 0
    total_volumes = len(VOLUMES)
    
    for nome_volume, modulos in VOLUMES.items():
        if consolidar_volume(nome_volume, modulos):
            sucessos += 1
        
        # Pausa entre volumes para evitar rate limiting
        if sucessos < total_volumes:
            print("\n⏳ Aguardando 5 segundos antes do próximo volume...")
            time.sleep(5)
    
    # Relatório final
    print(f"\n{'='*60}")
    print(f"🎉 CONSOLIDAÇÃO CONCLUÍDA!")
    print(f"✅ Volumes processados com sucesso: {sucessos}/{total_volumes}")
    print(f"📁 Arquivos salvos em: {PASTA_DESTINO}")
    print(f"{'='*60}")
    
    # Lista arquivos gerados
    print("\n📋 ARQUIVOS GERADOS:")
    for arquivo in sorted(os.listdir(PASTA_DESTINO)):
        if arquivo.endswith('.md'):
            caminho = os.path.join(PASTA_DESTINO, arquivo)
            tamanho = os.path.getsize(caminho) / 1024  # KB
            print(f"  📄 {arquivo} ({tamanho:.1f} KB)")

if __name__ == '__main__':
    main() 