import openai 
from apis_openai.moderation import modulo_moderation  
from apis_openai.completion import modulo_completion

def no_encontrado(open_ai, mensaje):
    return "Falta ser implementado por ustedes, equis dé"

def llamado_modulo(modulo):
    switcher = {
        '1': modulo_moderation, 
        '2': modulo_completion,
    }
    return switcher.get(modulo, no_encontrado) 

def llamado_api(modulo,open_ai:openai,mensaje):  
    return llamado_modulo(modulo)(open_ai=open_ai, mensaje=mensaje) 