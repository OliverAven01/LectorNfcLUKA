import pygame
import os

# Inicializa Pygame
pygame.mixer.init()

# Define las rutas a los archivos de audio
audio_exito = os.path.join("media", "exito.mp3")
audio_error = os.path.join("media", "fallo.mp3")

def reproducir_audio(audio_file):
    """Reproduce un archivo de audio dado."""
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Esperar a que el audio termine de reproducirse
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Error al reproducir el audio: {e}")

def reproducir_exito():
    """Reproduce el audio de �xito."""
    reproducir_audio(audio_exito)

def reproducir_error():
    """Reproduce el audio de error."""
    reproducir_audio(audio_error)