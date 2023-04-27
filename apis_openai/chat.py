import openai

def modulo_chat(open_ai:openai,mensaje):

      
      response= open_ai.ChatCompletion.create(

          model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": mensaje}],
          temperature=0.5, #valores más altos como 0.8 harán que la salida sea más aleatoria, mientras que los valores más bajos como 0.2 la harán más enfocada y determinista.
          max_tokens=60,
          top_p=1.0,
          frequency_penalty=0.5, # probabilidad de que el modelo repita la misma línea textualmente.
          presence_penalty = 0.0, #aumenta la probabilidad de que el modelo hable sobre nuevos temas.

      )

      return response.choices[0].message.copy().get("content")
