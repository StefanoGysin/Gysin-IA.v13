import sys
import os

# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from googlecloud.text_to_speech import text_to_speech

def test_text_to_speech_in_portuguese():
    text = "Olá Stefano, este é um teste do Google Cloud Text-to-Speech em Português Brasileiro!"
    output_file = "teste_audio_pt_br.mp3"
    text_to_speech(text, output_file, language_code='pt-BR')

def test_text_to_speech_in_english():
    text = "Hello, this is a test of Google Cloud Text-to-Speech in English!"
    output_file = "teste_audio_en.mp3"
    text_to_speech(text, output_file, language_code='en-US')

def test_text_to_speech_in_german():
    text = "Hallo, dies ist ein Test von Google Cloud Text-to-Speech auf Deutsch!"
    output_file = "teste_audio_de.mp3"
    text_to_speech(text, output_file, language_code='de-DE')

def test_text_to_speech_in_spanish():
    text = "Hola, esta es una prueba de Google Cloud Text-to-Speech en Español!"
    output_file = "teste_audio_es.mp3"
    text_to_speech(text, output_file, language_code='es-ES')

# Execute os testes
test_text_to_speech_in_portuguese()
test_text_to_speech_in_english()
test_text_to_speech_in_german()
test_text_to_speech_in_spanish()