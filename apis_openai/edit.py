
import openai   

def modulo_edit(open_ai:openai,mensaje):
    edit = open_ai.Edit.create(
    	model="text-davinci-edit-001",
    	input=mensaje,
    	instruction="Fix the spelling mistakes"
  	)
    return edit.choices[0].text



