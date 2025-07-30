import os
import re
import docx
import PyPDF2
from consolidar_curso import extrair_texto_srt, extrair_texto_pdf, extrair_texto_docx

def debug_modulo(caminho_modulo):
    """Debug da extração de um módulo específico"""
    print(f"🔍 DEBUG: {caminho_modulo}")
    print("="*60)
    
    if not os.path.exists(caminho_modulo):
        print(f"❌ Pasta não encontrada: {caminho_modulo}")
        return
    
    total_caracteres = 0
    
    for raiz, dirs, arquivos in os.walk(caminho_modulo):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            print(f"\n📄 Processando: {arquivo}")
            
            extensao = arquivo.lower().split('.')[-1]
            texto_arquivo = ""
            
            try:
                if extensao == 'srt':
                    texto_arquivo = extrair_texto_srt(caminho_completo)
                elif extensao == 'pdf':
                    texto_arquivo = extrair_texto_pdf(caminho_completo)
                elif extensao == 'docx':
                    texto_arquivo = extrair_texto_docx(caminho_completo)
                else:
                    print(f"  ⚠️ Extensão não suportada: {extensao}")
                    continue
                
                caracteres = len(texto_arquivo)
                total_caracteres += caracteres
                print(f"  ✅ Caracteres extraídos: {caracteres}")
                
                if caracteres < 100:
                    print(f"  ⚠️ AVISO: Poucos caracteres extraídos!")
                    print(f"  📝 Primeiros 200 caracteres: {texto_arquivo[:200]}")
                
            except Exception as e:
                print(f"  ❌ Erro: {e}")
    
    print(f"\n📊 TOTAL DE CARACTERES: {total_caracteres}")
    return total_caracteres

if __name__ == '__main__':
    # Testar módulo específico
    modulo = 'curso/01-INTRO AND OVERVIEW'
    debug_modulo(modulo) 