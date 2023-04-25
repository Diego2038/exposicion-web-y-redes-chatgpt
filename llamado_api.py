import openai 
from apis_openai.moderation import modulo_moderation  
from apis_openai.completion import modulo_completion
from apis_openai.edit import modulo_edit
from apis_openai.image_generation import modulo_image_generation

def no_encontrado(open_ai, mensaje):
    return "Falta ser implementado por ustedes, equis dé"

def llamado_modulo(modulo):
    switcher = {
        '1': modulo_moderation, 
        '2': modulo_completion,
        '3': modulo_edit,
        '4': modulo_image_generation,
    }
    return switcher.get(modulo, no_encontrado) 

def llamado_api(modulo,open_ai:openai,mensaje):  
    return llamado_modulo(modulo)(open_ai=open_ai, mensaje=mensaje) 