from langdetect import detect, DetectorFactory

# Configuração para resultados consistentes na detecção de idiomas
DetectorFactory.seed = 0

def detect_language(text):
    """Detecta o idioma do texto de entrada."""
    try:
        if len(text) < 3:
            print("Texto muito curto para detecção precisa.")
            return None
        return detect(text)
    except Exception as e:
        print(f"Erro na detecção do idioma: {e}")
        return None