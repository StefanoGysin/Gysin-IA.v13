# -*- coding: utf-8 -*-
"""
Módulo: Conversão de Texto para Fala

Este módulo utiliza a API do Google Cloud Text-to-Speech para converter texto em fala,
permitindo a escolha do idioma e ajustes na voz, como gênero e tom.

Autor: Stefano Gysin - StefanoGysin@hotmail.com
Data: 20/10/2024 15:12 (horário de Zurique)
"""

import os
from google.cloud import texttospeech

def text_to_speech(text, output_filename, language_code='pt-BR'):
    """
    Converte texto em fala usando a API Google Cloud Text-to-Speech.

    :param text: Texto a ser convertido em fala.
    :param output_filename: Nome do arquivo de saída para salvar o áudio.
    :param language_code: Código do idioma, padrão é 'pt-BR'.
    """

    # Define o caminho para o arquivo de credenciais do Google
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googlecloud/credencial.json"
    
    # Autentica usando as credenciais da conta de serviço
    client = texttospeech.TextToSpeechClient()

    # Configura a solicitação de síntese
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Seleção de voz Wavenet-E
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=f"{language_code}-Wavenet-E",  # Altere para outra voz se necessário
        ssml_gender=texttospeech.SsmlVoiceGender.MALE  # Altere para MALE, FEMALE ou NEUTRAL
    )

    # Configurações de áudio
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.3,  # Ajuste a velocidade conforme necessário
        pitch=-4.0  # Ajuste o pitch se necessário, por exemplo, -2.0 para um tom mais grave
    )

    # Solicita a conversão de texto para fala
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Salva a resposta de áudio em um arquivo
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print(f"Áudio salvo como {output_filename}")