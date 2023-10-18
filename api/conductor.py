from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.conductor import Conductor, ConductoresSchema

ruta_conductores = Blueprint("ruta_conductor", __name__)

conductor_schema = ConductoresSchema()
conductores_schema = ConductoresSchema(many=True)

@ruta_conductores.route('/conductores', methods=['GET'])
def conductor():
    resultall = Conductor.query.all() #Select * from Conductores
    resultado_conductor= conductores_schema.dump(resultall)
    return jsonify(resultado_conductor)

@ruta_conductores.route('/saveconductor', methods=['POST'])
def save():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    numero = request.json['numero']
    experiencia = request.json['experiencia']
    new_conductor = Conductor(nombre,apellido,numero,experiencia)
    db.session.add(new_conductor)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_conductores.route('/updateconductor', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    numero = request.json['numero']
    experiencia = request.json['experiencia']
    conductor = Conductor.query.get(id)   
    if conductor :
        print(conductor) 
        conductor.nombre = nombre
        conductor.apellido = apellido
        conductor.numero = numero
        conductor.experiencia = experiencia        
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_conductores.route('/deleteconductor/<id>', methods=['DELETE'])
def eliminar(id):
    conductor = Conductor.query.get(id)
    db.session.delete(conductor)
    db.session.commit()
    return jsonify(conductor_schema.dump(conductor))