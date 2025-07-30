import sys
import os
from consolidar_curso import consolidar_volume, VOLUMES

def testar_volume_especifico(nome_volume):
    """Testa a consolidação de um volume específico"""
    if nome_volume not in VOLUMES:
        print(f"❌ Volume '{nome_volume}' não encontrado!")
        print("\n📋 Volumes disponíveis:")
        for vol in VOLUMES.keys():
            print(f"  - {vol}")
        return False
    
    print(f"🧪 TESTANDO VOLUME: {nome_volume}")
    print(f"Módulos: {', '.join(VOLUMES[nome_volume])}")
    
    # Executa a consolidação
    sucesso = consolidar_volume(nome_volume, VOLUMES[nome_volume])
    
    if sucesso:
        print(f"\n✅ Teste concluído com sucesso!")
        print(f"📄 Arquivo gerado: base_de_conhecimento_final/{nome_volume}.md")
    else:
        print(f"\n❌ Teste falhou!")
    
    return sucesso

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 testar_volume.py <nome_do_volume>")
        print("\nExemplo: python3 testar_volume.py Volume_01_Fundamentos_e_Filosofia")
        print("\n📋 Volumes disponíveis:")
        for vol in VOLUMES.keys():
            print(f"  - {vol}")
        sys.exit(1)
    
    nome_volume = sys.argv[1]
    testar_volume_especifico(nome_volume) 