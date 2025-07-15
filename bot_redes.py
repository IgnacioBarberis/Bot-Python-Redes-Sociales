import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

CONSUMER_KEY = os.getenv('API_KEY')
CONSUMER_SECRET = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Mensajes predefinidos bilingües
mensajes = {
    "español": "¡Hola desde mi bot Python! Prueba en español. #BotBilingue",
    "inglés": "Hello from my Python bot! Test in English. #BilingualBot"
}

def publicar_tweet(idioma):
    mensaje = mensajes.get(idioma.lower(), "Idioma no soportado")
    try:
        response = client.create_tweet(text=mensaje)
        print(f"¡Tweet publicado en {idioma}! ID:", response.data['id'])
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo: Cambia 'español' o 'inglés'
publicar_tweet("español")  # O "inglés"