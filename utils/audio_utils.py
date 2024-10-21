# Conteúdo do arquivo: C:\Servidor\Gysin-IA.v13\utils\audio_utils.py

import pyaudio
import wave

def record_audio(output_filename, duration=5):
    """Grava áudio do microfone e salva em um arquivo WAV."""
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    print("Gravando...")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Gravação finalizada.")

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()