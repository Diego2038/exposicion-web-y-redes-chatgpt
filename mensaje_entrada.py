import openai
from llamado_api import llamado_api

def mensaje_entrada(elegir_api, open_ai:openai):  
  while(True):
    
    mensaje = input("Digita tu mensaje (-1 para salir del módulo): ").strip()
    if( mensaje == "-1"):
      print("Saliste del módulo ")
      break

    respuesta = llamado_api(modulo=elegir_api,open_ai=open_ai,mensaje=mensaje) 

    print("Mensaje:\n", mensaje,"\n")
    print("Salida:\n",respuesta,"\n")
 