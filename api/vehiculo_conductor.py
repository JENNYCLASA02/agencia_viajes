from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo_conductor import Vehiculo_conductor, Vehiculo_conductoresSchema

ruta_vehiculo_conductores = Blueprint("ruta_vehiculo_conductor", __name__)

vehiculo_conductor_schema = Vehiculo_conductoresSchema()
vehiculo_conductores_schema = Vehiculo_conductoresSchema(many=True)

@ruta_vehiculo_conductores.route('/vehiculo_conductores', methods=['GET'])
def vehiculo_conductor():
    resultall = Vehiculo_conductor.query.all() #Select * from Vehiculo_conductores
    resultado_vehiculo_conductor= vehiculo_conductores_schema.dump(resultall)
    return jsonify(resultado_vehiculo_conductor)

@ruta_vehiculo_conductores.route('/savevehiculo_conductor', methods=['POST'])
def save():
    id_vehiculo = request.json['id_vehiculo']
    id_conductor = request.json['id_conductor']
    new_vehiculo_conductor = Vehiculo_conductor(id_vehiculo,id_conductor)
    db.session.add(new_vehiculo_conductor)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_vehiculo_conductores.route('/updatevehiculo_conductor', methods=['PUT'])
def Update():
    id = request.json['id']
    id_vehiculo = request.json['id_vehiculo']
    id_conductor = request.json['id_conductor']
    vehiculo_conductor = Vehiculo_conductor.query.get(id)   
    if vehiculo_conductor :
        print(vehiculo_conductor) 
        vehiculo_conductor.id_vehiculo = id_vehiculo
        vehiculo_conductor.id_conductor = id_conductor
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_vehiculo_conductores.route('/deletevehiculo_conductor/<id>', methods=['GET'])
def eliminar(id):
    vehiculo_conductor = Vehiculo_conductor.query.get(id)
    db.session.delete(vehiculo_conductor)
    db.session.commit()
    return jsonify(vehiculo_conductor_schema.dump(vehiculo_conductor))