#!/usr/bin/env python
import json
import datetime
from dateutil.relativedelta import *  # pip install python-dateutil
import requests

# curl -X GET --header 'Accept: application/json' 'http://127.0.0.1:8080/periodos/api'
endpoint = 'http://127.0.0.1:8080/periodos/api'
header = ''
outputFile = 'output.json'

try:
    response = requests.get(url=endpoint, headers={'Accept': 'application/json'}) 
    jsonInput = response.json()
except Exception as e: 
    print("Error al llamar al servicio (%s)" % e)


startDate = datetime.datetime.strptime(jsonInput['fechaCreacion'], '%Y-%m-%d')
endDate = datetime.datetime.strptime(jsonInput['fechaFin'], '%Y-%m-%d')
dateList = jsonInput['fechas']

tempDate = startDate
fechasFaltantes = []
while tempDate <= endDate:
    tempDate += relativedelta(months=+1)
    if tempDate.strftime("%Y-%m-%d") not in dateList:
        fechasFaltantes.append(tempDate.strftime("%Y-%m-%d"))

jsonOutput = {}
jsonOutput['id'] = jsonInput['id']
jsonOutput['fechaCreacion'] = jsonInput['fechaCreacion']
jsonOutput['fechaFin'] = jsonInput['fechaFin']
jsonOutput['fechasFaltantes'] = fechasFaltantes
json_data = json.dumps(jsonOutput, indent=3)

f = open('%s' % outputFile, "w")
f.write('%s' % json_data)
f.close()