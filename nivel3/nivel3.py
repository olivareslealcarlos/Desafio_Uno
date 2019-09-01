#!/usr/bin/env python
from flask import Flask
from flask_restplus import Api, Resource
import requests, json, datetime
from dateutil.relativedelta import *  # pip install python-dateutil

flaskApp = Flask(__name__)
app = Api(app = flaskApp)
application = app.namespace('GDDCaller', description='Desafio Nivel 3')

# curl -X GET --header 'Accept: application/json' 'http://127.0.0.1:8080/periodos/api'
endpoint = 'http://127.0.0.1:8080/periodos/api'

@application.route("/")
class GDDCaller(Resource):
	def get(self):
            try:
                jsonInput = requests.get(url=endpoint, headers={'Accept': 'application/json'}).json()
                statusMsg = "Datos obtenidos exitosamente"

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
                jsonOutput['fechas'] = jsonInput['fechas']
                jsonOutput['fechasFaltantes'] = fechasFaltantes

            except Exception as e: 
                statusMsg = "Error con el servicio GDD"
                print("Error al llamar al servicio (%s)" % e)

            return {
                "status": statusMsg,
                "data": jsonOutput
            }

if __name__ == "__main__":
    flaskApp.run()
