import openai  
from dotenv import load_dotenv
import os
from llamado_api import llamado_api

def mensaje_entrada(elegir_api): 
  print("Escribe cualquier mensaje, para salir de esta opción sólo digita \"-1\"")
  while(True):
    load_dotenv()
    OPENAI_API_KEY = os.getenv("API_KEY")
    
    openai.api_key = OPENAI_API_KEY
    open_ai = openai 

    mensaje = input("Digita tu mensaje: ")
    if( mensaje == "-1"):
      print("Saliste del módulo ")
      break

    respuesta = llamado_api(modulo=elegir_api,open_ai=open_ai,mensaje=mensaje) 

    print("Mensaje: ", mensaje,"\n")
    print(respuesta)
 