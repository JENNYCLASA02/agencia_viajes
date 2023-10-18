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
    idusuario = request.json['idusuario']
    tipodocumento = request.json['tipodocumento']
    nombre = request.json['nombre']
    apellido = request.json['apellido'] 
    edad = request.json['edad'] 
    numcelular = request.json['numcelular']
    direccion = request.json['direccion'] 
    new_viajero = Viajero(idusuario, tipodocumento,nombre,apellido,edad,numcelular,direccion)
    db.session.add(new_viajero)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_viajeros.route('/updateviajero', methods=['PUT'])
def Update():
    id = request.json['id']
    idusuario = request.json['idusuario']
    tipodocumento = request.json['tipodocumento']
    nombre = request.json['nombre']
    apellido = request.json['apellido'] 
    edad = request.json['edad'] 
    numcelular = request.json['numcelular']
    direccion = request.json['direccion'] 
    viajero = Viajero.query.get(id)   
    if viajero :
        print(viajero) 
        viajero.idusuario = idusuario
        viajero.tipodocumento = tipodocumento
        viajero.nombre = nombre
        viajero.apellido = apellido
        viajero.edad = edad 
        viajero.numcelular = numcelular
        viajero.direccion = direccion
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_viajeros.route('/deleteviajero/<id>', methods=['DELETE'])
def eliminar(id):
    viajero = Viajero.query.get(id)
    db.session.delete(viajero)
    db.session.commit()
    return jsonify(viajero_schema.dump(viajero))