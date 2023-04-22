# import os
# import openai
# OPENAI_API_KEY = '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'
# openai.organization = "org-FV4d246IT3h7okePCR7FjlxM"
# openai.api_key = os.getenv(OPENAI_API_KEY)
# openai.Model.list()

import os
import openai
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hola, quiero que me digas un chiste"}
  ]
)

print(completion.choices[0].message)