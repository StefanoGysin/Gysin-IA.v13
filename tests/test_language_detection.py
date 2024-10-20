import os
import sys

# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gui.language_utils import detect_language

def test_multilingual_input():
    inputs = [
        "Olá, como você está?",
        "Hello, how are you?",
        "Hallo, wie geht es dir?",
        "Hola, ¿cómo estás?"
    ]

    for text in inputs:
        detected_lang = detect_language(text)
        print(f"Texto: {text} | Idioma detectado: {detected_lang}")

# Execute os testes de detecção
test_multilingual_input()