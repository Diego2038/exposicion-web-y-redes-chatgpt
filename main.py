import openai  
from dotenv import load_dotenv
import os
from mensaje_entrada import mensaje_entrada

def main():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("API_KEY")

    openai.api_key = OPENAI_API_KEY
    open_ai = openai  
    print("A continuación se mostrarán las opciones de API's que tiene para escoger:")
    while(True):
        print("\n   1) Moderation\n   2) Completion\n   3) Edit\n   4) <NO IMPLEMENTADO>\n   5) <NO IMPLEMENTADO>\n")
        modulo = input("Digite el módulo que quiere entrar(-1 para terminar el programa): ").strip()
        if (modulo == "-1"):
            break

        if modulo in ['1','2','3','4','5']:
            mensaje_entrada(elegir_api=modulo,open_ai=open_ai)
        else:
            print('Número NO reconocido, por favor vuelva a intentarlo\n------------------------\n\n')

main()
     