from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ruta import Ruta, RutasSchema

ruta_rutas = Blueprint("ruta_route", __name__)

ruta_schema = RutasSchema()
rutas_schema = RutasSchema(many=True)

@ruta_rutas.route('/rutas', methods=['GET'])
def ruta():
    resultall = Ruta.query.all() #Select * from Routes
    resultado_ruta= rutas_schema.dump(resultall)
    return jsonify(resultado_ruta)

@ruta_rutas.route('/saveruta', methods=['POST'])
def save():
    origen = request.json['origen']
    destino = request.json['destino']
    distancia = request.json['distancia']
    duracion = request.json ['duracion']
    new_ruta = Ruta(origen,destino,distancia,duracion)
    db.session.add(new_ruta)
    db.session.commit()    
    return "los datos han sido guardado con exito"

@ruta_rutas.route('/updateruta', methods=['PUT'])
def Update():
    id = request.json['id']
    origen = request.json['origen']
    destino = request.json['destino']
    distancia = request.json['distancia']
    duracion = request.json ['duracion']
    ruta = Ruta.query.get(id)   
    if ruta :
        print(ruta)
        ruta.origen = origen
        ruta.destino = destino
        ruta.distancia = distancia
        ruta.duracion = duracion
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_rutas.route('/deleteruta/<id>', methods=['DELETE'])
def eliminar(id):
    ruta = Ruta.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(ruta))