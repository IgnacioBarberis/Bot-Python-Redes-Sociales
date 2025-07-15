import tweepy
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde .env
load_dotenv()

# Tus claves de API (las pondrás en un archivo separado)
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Autenticación con la API de Twitter (X)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Función para publicar un tweet
def publicar_tweet(mensaje):
    try:
        api.update_status(mensaje)
        print("¡Tweet publicado con éxito!")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso: Cambia el mensaje por lo que quieras
publicar_tweet("¡Hola desde mi bot Python! Esto es una prueba automática. #PythonBot")