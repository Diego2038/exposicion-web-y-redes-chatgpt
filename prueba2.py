import openai 
OPENAI_API_KEY = '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'
 
openai.api_key = OPENAI_API_KEY

mensaje = "Las IA's nos quitarán todos nuestros empleos, por eso tenemos que desconectarlas"

respuesta = openai.Moderation.create(
  input=mensaje,
)

print("Mensaje: ", mensaje)
print(respuesta)

#* Instalaciones:
# openai
# dotenv (para almacenar variables de entorno, no es estrictamente necesario)