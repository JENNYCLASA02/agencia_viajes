from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reserva import Reserva, ReservasSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

@ruta_reservas.route('/reservas', methods=['GET'])
def reserva():
    resultall = Reserva.query.all() #Select * from Reservas
    resultado_reserva= reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)

@ruta_reservas.route('/savereserva', methods=['POST'])
def save():
    ciudad_origen = request.json ['ciudad_origen'] 
    ciudad_destino = request.json ['ciudad_destino'] 
    dir_origen = request.json ['dir_origen'] 
    dir_destino = request.json ['dir_destino'] 
    preferencias = request.json ['preferencias']  
    fecha = request.json ['fecha'] 
    new_reserva = Reserva(ciudad_origen,ciudad_destino,dir_origen,dir_destino,preferencias,fecha)
    db.session.add(new_reserva)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_reservas.route('/updatereserva', methods=['PUT'])
def Update():
    id = request.json['id']
    ciudad_origen = request.json ['ciudad_origen'] 
    ciudad_destino = request.json ['ciudad_destino'] 
    dir_origen = request.json ['dir_origen'] 
    dir_destino = request.json ['dir_destino'] 
    preferencias = request.json ['preferencias']  
    fecha = request.json ['fecha'] 
    reserva = Reserva.query.get(id)   
    if reserva :
        print(reserva) 
        reserva.ciudad_origen = ciudad_origen
        reserva.ciudad_destinob = ciudad_destino
        reserva.dir_origen = dir_origen
        reserva.dir_destino = dir_destino
        reserva.preferencias = preferencias
        reserva.fecha = fecha
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_reservas.route('/deletereserva/<id>', methods=['GET'])
def eliminar(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(reserva_schema.dump(reserva))