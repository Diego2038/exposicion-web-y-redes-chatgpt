import openai

def modulo_image_generation(open_ai:openai,mensaje):  
    image = open_ai.Image.create(
      prompt=mensaje,
      n=1,
      size="256x256"
    )
    return image