import openai   

def modulo_audio_transcription(open_ai:openai,mensaje):  
    transcription = open_ai.Audio.transcribe(
        file = open(mensaje, "rb"),
        model="whisper-1",
    )
    return transcription