import os
from google.cloud import speech
import io

def transcribe_audio(audio_filename):
    """Transcreve o áudio usando Google Cloud Speech-to-Text."""
    # Defina o caminho para o arquivo de credenciais do Google
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googlecloud/credencial.json"
    
    client = speech.SpeechClient()

    with io.open(audio_filename, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="pt-BR",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcrição: {}".format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript

    return ""