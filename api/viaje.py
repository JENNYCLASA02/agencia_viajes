from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import Viaje, ViajesSchema

ruta_viajes = Blueprint("ruta_viaje", __name__)

viaje_schema = ViajesSchema()
viajes_schema = ViajesSchema(many=True)

@ruta_viajes.route('/viajes', methods=['GET'])
def viaje():
    resultall = Viaje.query.all() #Select * from Viajes
    resultado_viaje= viajes_schema.dump(resultall)
    return jsonify(resultado_viaje)

@ruta_viajes.route('/saveviaje', methods=['POST'])
def save():
    id_ruta = request.json ['id_ruta']
    id_vehiculo= request.json ['id_vehiculo']
    fecha_inicio = request.json['fecha_inicio']
    fecha_finalizacion = request.json ['fecha_finalizacion']
    estado = request.json ['estado']
    new_viaje = Viaje(id_ruta,id_vehiculo,fecha_inicio,fecha_finalizacion,estado)
    db.session.add(new_viaje)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_viajes.route('/updateviaje', methods=['PUT'])
def Update():
    id = request.json['id']
    id_ruta = request.json ['id_ruta']
    id_vehiculo= request.json ['id_vehiculo']
    fecha_inicio = request.json['fecha_inicio']
    fecha_finalizacion = request.json ['fecha_finalizacion']
    estado = request.json ['estado']
    viaje = Viaje.query.get(id)   
    if viaje :
        print(viaje)
        viaje.id_ruta = id_ruta
        viaje.id_vehiculo = id_vehiculo
        viaje.fecha_inicio = fecha_inicio
        viaje.fecha_finalizacion = fecha_finalizacion
        viaje.estado = estado
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_viajes.route('/deleteviaje/<id>', methods=['DELETE'])
def eliminar(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(viaje_schema.dump(viaje))