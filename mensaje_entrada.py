import openai
from llamado_api import llamado_api

def mensaje_entrada(elegir_api, open_ai:openai): 
  print("Escribe cualquier mensaje, para salir de esta opción sólo digita \"-1\"")
  while(True):
    
    mensaje = input("Digita tu mensaje: ")
    if( mensaje == "-1"):
      print("Saliste del módulo ")
      break

    respuesta = llamado_api(modulo=elegir_api,open_ai=open_ai,mensaje=mensaje) 

    print("Mensaje: ", mensaje,"\n")
    print(respuesta)
 