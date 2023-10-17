from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viajero import Viajero, ViajerosSchema

ruta_viajeros = Blueprint("ruta_viajero", __name__)

viajero_schema = ViajerosSchema()
viajeros_schema = ViajerosSchema(many=True)

@ruta_viajeros.route('/viajeros', methods=['GET'])
def viajero():
    resultall = Viajero.query.all() #Select * from Viajeros
    resultado_viajero= viajeros_schema.dump(resultall)
    return jsonify(resultado_viajero)

@ruta_viajeros.route('/saveviajero', methods=['POST'])
def save():
    id_usuario = request.json['id_usuario']
    tipo_documento = request.json['tipo_documento']
    nombre = request.json['nombre']
    apellido = request.json['apellido'] 
    edad = request.json['edad'] 
    num_celular = request.json['num_celular']
    direccion = request.json['direccion'] 
    new_viajero = Viajero(id_usuario, tipo_documento,nombre,apellido,edad,num_celular,direccion)
    db.session.add(new_viajero)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_viajeros.route('/updateviajero', methods=['PUT'])
def Update():
    id = request.json['id']
    id_usuario = request.json['id_usuario']
    tipo_documento = request.json['tipo_documento']
    nombre = request.json['nombre']
    apellido = request.json['apellido'] 
    edad = request.json['edad'] 
    num_celular = request.json['num_celular']
    direccion = request.json['direccion'] 
    viajero = Viajero.query.get(id)   
    if viajero :
        print(viajero) 
        viajero.id_usuario = id_usuario
        viajero.tipo_documento = tipo_documento
        viajero.nombre = nombre
        viajero.apellido = apellido
        viajero.edad = edad 
        viajero.num_celular = num_celular
        viajero.direccion = direccion
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_viajeros.route('/deleteviajero/<id>', methods=['GET'])
def eliminar(id):
    viajero = Viajero.query.get(id)
    db.session.delete(viajero)
    db.session.commit()
    return jsonify(viajero_schema.dump(viajero))