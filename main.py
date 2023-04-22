import openai  
from dotenv import load_dotenv
import os
from mensaje_entrada import mensaje_entrada

def main():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("API_KEY")

    openai.api_key = OPENAI_API_KEY
    open_ai = openai 

    print("Seleccione un número para escoger el módulo, digite -1 para salir del módulo en cuestión")
    while(True):
        modulo = input("Digite el módulo que quiere entrar: ")
        if (modulo == "-1"):
            break

        if modulo in ['1','2','3','4','5']:
            mensaje_entrada(elegir_api=modulo,open_ai=open_ai)
        else:
            print('Número NO reconocido, por favor vuelva a intentarlo')

main()
     