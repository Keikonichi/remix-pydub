from pydub import AudioSegment
from datetime import datetime

def tempo_para_ms(minuto, segundo):
    return (minuto * 60 + segundo) * 1000

# Nome com data e hora (ex: remix_20250428_1432_fade.mp3)
def salvar_versao(nome_sufixo, audio):
    agora = datetime.now().strftime("%Y%m%d_%H%M")
    arquivo = f"Nome-final-remix_{agora}_{nome_sufixo}.mp3"
    audio.export(arquivo, format="mp3")
    print(f"✔️ Exportado: {arquivo}")

# Carregar os arquivos de áudio original
musica_loop1 = AudioSegment.from_file("arquivoOriginal.mp3")
musica_principal1 = AudioSegment.from_file("arquivoOriginal.mp3")
musica_principal2 = AudioSegment.from_file("arquivoOriginal.mp3")

# Cortes
intro =  musica_loop1[tempo_para_ms(0, 0):tempo_para_ms(0, 26)]

# trecho principal
trecho_principal1 = musica_principal1[tempo_para_ms(0, 17):tempo_para_ms(1, 54)]

trecho_principal2 = musica_principal2[tempo_para_ms(0, 0):tempo_para_ms(1, 41)]

loop2 = musica_principal2[tempo_para_ms(1, 37):tempo_para_ms(1, 41)]

trecho_principalLimpo = trecho_principal2.strip_silence(silence_len=500, silence_thresh=-40)

# Repete esse trecho 3 vezes
# loop = intro * 2

# Export para teste de transição simples
test_mix = intro + trecho_principal1 + trecho_principal2 + loop2
test_mix.export("test_transicao.mp3", format="mp3")


# Versão com fade e efeitos
whoosh = AudioSegment.from_file("efeito-a-ser-usado.mp3")
remix_final = intro + trecho_principal1.fade_out(1000) + trecho_principalLimpo.fade_out(1500) + loop2 + whoosh
salvar_versao("fade", remix_final)
print("Remix base exportado: Nome-arquivo-final.mp3", remix_final)

# Versão com crossfade suave entre partes
parte_crossfade = trecho_principal1.append(trecho_principal2, crossfade=500)
remix_crossfade = intro + parte_crossfade + loop2 + whoosh
salvar_versao("crossfade", remix_crossfade)

# Versão com overlay + whoosh
whoosh_overlay = AudioSegment.from_file("efeito-a-ser-usado.mp3") - 5
parte_overlay = trecho_principal1 + whoosh_overlay.overlay(trecho_principal2, position=500)
remix_overlay = intro + parte_overlay + loop2 + whoosh
salvar_versao("overlay", remix_overlay)

# Exporta interativos
#Pergunta ao usuário sobre os efeitos

if input("Aplicar efeito 'whoosh' de transição? (s/n): ").strip().lower() == "s":

    # Aplica efeito 'whoosh' de transição
    whoosh = AudioSegment.from_file("Efeitos/happy-child-laughing.mp3")
    remix_whoosh2 = intro + trecho_principal1.fade_out(3000) + whoosh + trecho_principal2.fade_out(1000) + loop2
   
    salvar_versao("happy", remix_whoosh2)
   
    print("Efeito 'happy-child-laughing' aplicado.")

if input("Aplicar efeito 'whoosh' de transição? (s/n): ").strip().lower() == "s":
    # Aplica efeito 'whoosh' de transição
    whoosh = AudioSegment.from_file("Efeitos/futuristic-space.mp3")
    remix_whoosh3 = intro + trecho_principal1 + whoosh + trecho_principalLimpo + loop2 + whoosh

    salvar_versao("futuristic", remix_whoosh3)

    print("Efeito 'futuristic-space' aplicado.")


print("\Todos os efeitos aplicados conforme sua escolha!")