#!/usr/bin/env python
import argparse
import json
import datetime
from dateutil.relativedelta import *  # pip install python-dateutil

def fechasFaltantes(inputFile, outputFile):
    data = ''
    with open('%s' % (inputFile), 'r') as file:
        data = file.read()

    jsonInput = json.loads(data)
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
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Nombre de archivo de entrada')
    parser.add_argument('output', help='Nombre de archivo de salida')
    args = parser.parse_args()
    fechasFaltantes(args.input, args.output)