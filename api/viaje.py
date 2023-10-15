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
    hora_inicio = request.json['hora_inicio']
    hora_finalizacion = request.json ['hora_finalizacion']
    fecha = request.json ['fecha']
    duracion = request.json ['duracion']
    estado = request.json ['estado']
    id_vehiculo = request.json ['id_vehiculo']
    new_viaje = Viaje(hora_inicio, hora_finalizacion, fecha, duracion, estado, id_vehiculo)
    db.session.add(new_viaje)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_viajes.route('/updateviaje', methods=['PUT'])
def Update():
    id = request.json['id']
    hora_inicio = request.json['hora_inicio']
    hora_finalizacion = request.json ['hora_finalizacion']
    fecha = request.json ['fecha']
    duracion = request.json ['duracion']
    estado = request.json ['estado']
    id_vehiculo = request.json ['id_vehiculo']
    viaje = Viaje.query.get(id)   
    if viaje :
        print(viaje) 
        viaje.hora_inicio = hora_inicio
        viaje.hora_finalizacion = hora_finalizacion
        viaje.fecha = fecha
        viaje.duracion = duracion
        viaje.estado = estado
        viaje.id_vehiculo = id_vehiculo
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_viajes.route('/deleteviaje/<id>', methods=['GET'])
def eliminar(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(viaje_schema.dump(viaje))