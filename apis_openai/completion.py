import openai   

def modulo_completion(open_ai:openai,mensaje):  
    
    completion = open_ai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": mensaje}
    ])

    return completion.choices[0].message 