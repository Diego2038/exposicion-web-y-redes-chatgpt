# Algunas API's de Chat GPT
El siguiente código permite ejecutar algunas API's que ofrece la empresa OpenAI, la cual se puede ejecutar de diferentes maneras a través de la terminal. <br> 

## Pasos para ejecutar el código
**Nota:** Estos pasos son sólo para Windows, si tiene otro sistema operativo el procedimiento es diferente.<br>
<br>
Para crear el ambiente virtual descarga la librería "virtualenv" a través de pip:

```
pip install virtualenv 
```

<br>
Para crear el ambiente virtual con nombre "venv":

```
python -m venv venv
```

<br>
Para ejecutar el ambiente virtual (desde la carpeta raiz):

```
.\venv\Scripts\activate
```

<br>
Realizar las instalaciones de las dependencias:

```
pip install -r requirements.txt
```

<br>
Crear la carpeta *.env* y añadir la siguiente variable:

```
API_KEY="<La clave que OpenAI te proporcionó>"
``` 

<br>
Para ejecutar el código del programa:

```
python main.py
``` 

<br>
Para cerrar el ambiente virtual:

```
deactivate
``` 
