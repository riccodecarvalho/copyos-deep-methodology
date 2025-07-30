import os
import re
import docx
import PyPDF2
import zipfile

# --- CONFIGURAÇÃO ---
PASTA_RAIZ = './curso'
PASTA_DESTINO = './texto_bruto'
# --------------------

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
                texto_total += f"\n\n{'='*80}\nARQUIVO: {arquivo}\n{'='*80}\n{texto_arquivo}"
    
    return texto_total

def consolidar_volume_bruto(nome_volume, modulos):
    """Consolida múltiplos módulos em um arquivo de texto bruto"""
    print(f"\n{'='*60}")
    print(f"CONSOLIDANDO BRUTO: {nome_volume}")
    print(f"Módulos: {', '.join(modulos)}")
    print(f"{'='*60}")
    
    # Extrai texto de todos os módulos
    texto_total = f"# {nome_volume.replace('_', ' ').title()}\n\n"
    texto_total += f"**Módulos incluídos:** {', '.join(modulos)}\n\n"
    texto_total += f"{'='*80}\n\n"
    
    for modulo in modulos:
        caminho_modulo = os.path.join(PASTA_RAIZ, modulo)
        print(f"\nProcessando módulo: {modulo}")
        texto_modulo = processar_pasta_recursivamente(caminho_modulo)
        texto_total += f"\n\n{'='*80}\nMÓDULO: {modulo}\n{'='*80}\n{texto_modulo}"
    
    print(f"\nTotal de caracteres extraídos: {len(texto_total)}")
    
    # Salva o resultado
    nome_arquivo = f"{nome_volume}_BRUTO.txt"
    caminho_destino = os.path.join(PASTA_DESTINO, nome_arquivo)
    
    with open(caminho_destino, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto_total)
    
    print(f"✅ Volume bruto salvo: {nome_arquivo}")
    return True

def main():
    """Função principal que executa a consolidação bruta de todos os volumes"""
    print("📄 COPYOS™ - CONSOLIDAÇÃO BRUTA")
    print("="*60)
    print("Gerando arquivos de texto bruto para análise interativa")
    print("="*60)
    
    # Cria pasta de destino
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    
    # Processa cada volume
    sucessos = 0
    total_volumes = len(VOLUMES)
    
    for nome_volume, modulos in VOLUMES.items():
        if consolidar_volume_bruto(nome_volume, modulos):
            sucessos += 1
    
    # Relatório final
    print(f"\n{'='*60}")
    print(f"🎉 CONSOLIDAÇÃO BRUTA CONCLUÍDA!")
    print(f"✅ Volumes processados: {sucessos}/{total_volumes}")
    print(f"📁 Arquivos salvos em: {PASTA_DESTINO}")
    print(f"{'='*60}")
    
    # Lista arquivos gerados
    print("\n📋 ARQUIVOS BRUTOS GERADOS:")
    for arquivo in sorted(os.listdir(PASTA_DESTINO)):
        if arquivo.endswith('_BRUTO.txt'):
            caminho = os.path.join(PASTA_DESTINO, arquivo)
            tamanho = os.path.getsize(caminho) / 1024  # KB
            print(f"  📄 {arquivo} ({tamanho:.1f} KB)")
    
    print(f"\n🚀 PRÓXIMO PASSO:")
    print(f"1. Faça upload de um arquivo _BRUTO.txt para o CopyOS™")
    print(f"2. Use o prompt de análise fornecido")
    print(f"3. Interaja para refinar e aprofundar o conteúdo")

if __name__ == '__main__':
    main() 