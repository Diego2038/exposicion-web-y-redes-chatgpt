
#Pasos para ejecutar el código

Para crear el ambiente virtual descarga la librería "virtualenv" a través de pip
```
pip install virtualenv 
```

Para crear el ambiente virtual con nombre "venv":
```
python -m venv venv
```

Para ejecutar el ambiente virtual (desde la carpeta raiz y desde Windows):
```
.\venv\Scripts\activate
```

Realizar las instalaciones de las dependencias
```
pip install -r requirements.txt
```

Crear la carpeta *.env* y añadir la siguiente variable
```
API_KEY="<La clave que OpenAI te proporcionó>"
``` 