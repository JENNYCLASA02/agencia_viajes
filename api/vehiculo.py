from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculosSchema

ruta_vehiculos = Blueprint("ruta_vehiculo", __name__)

vehiculo_schema = VehiculosSchema()
vehiculos_schema = VehiculosSchema(many=True)

@ruta_vehiculos.route('/vehiculos', methods=['GET'])
def vehiculo():
    resultall = Vehiculo.query.all() #Select * from Vehiculos
    resultado_vehiculo= vehiculos_schema.dump(resultall)
    return jsonify(resultado_vehiculo)

@ruta_vehiculos.route('/savevehiculo', methods=['POST'])
def save():
    placa = request.json ['placa']
    modelo = request.json ['modelo']
    capacidad = request.json ['capacidad']
    disponibilidad = request.json ['disponibilidad']
    localidad = request.json['localidad']
    new_vehiculo = Vehiculo(placa,modelo,capacidad,disponibilidad,localidad)
    db.session.add(new_vehiculo)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_vehiculos.route('/updatevehiculo', methods=['PUT'])
def Update():
    id = request.json['id']
    placa = request.json ['placa']
    modelo = request.json ['modelo']
    capacidad = request.json ['capacidad']
    disponibilidad = request.json ['disponibilidad']
    localidad = request.json['localidad']
    vehiculo = Vehiculo.query.get(id)   
    if vehiculo :
        print(vehiculo) 
        vehiculo.placa = placa 
        vehiculo.modelo = modelo
        vehiculo.capacidad = capacidad
        vehiculo.disponibilidad = disponibilidad
        vehiculo.localidad = localidad

        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_vehiculos.route('/deletevehiculo/<id>', methods=['GET'])
def eliminar(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(vehiculo_schema.dump(vehiculo))