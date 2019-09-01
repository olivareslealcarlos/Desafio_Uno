# Nivel 3

### Requerimientos
  - Python 3.7.2

### Instalacion de librerias
  Instalar librerias con PIP
  - pip install python-dateutil
  - pip install flask
  - pip install flask_restplus

  Alternativa: py -m pip install [libreria]

### Ejecucion
  py nivel3.py
 * Serving Flask app "nivel3" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### Visualizar Documentación y consumir la API

La documentación swagger del API (una vez que se levanta el API) queda disponible en

http://127.0.0.1:5000/

Para consumir el servicio se debe invocar la siguiente URL

```bash
curl -X GET "http://127.0.0.1:5000/GDDCaller/" -H "accept: application/json"
```