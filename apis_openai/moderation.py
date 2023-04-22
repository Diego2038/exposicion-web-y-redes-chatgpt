import openai   

def modulo_moderation(open_ai:openai,mensaje):  
    moderation = open_ai.Moderation.create(
      input=mensaje,
    )
    return moderation