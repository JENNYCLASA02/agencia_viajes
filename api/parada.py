from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.parada import Parada, ParadasSchema

ruta_paradas = Blueprint("ruta_parada", __name__)

parada_schema = ParadasSchema()
paradas_schema = ParadasSchema(many=True)

@ruta_paradas.route('/paradas', methods=['GET'])
def parada():
    resultall = Parada.query.all() #Select * from Paradas
    resultado_parada= paradas_schema.dump(resultall)
    return jsonify(resultado_parada)

@ruta_paradas.route('/saveparada', methods=['POST'])
def save():
    direccion_origen = request.json['direccion_origen']
    direccion_destino = request.json['direccion_destino']
    idruta = request.json['idruta']
    new_parada = Parada(direccion_origen,direccion_destino,idruta)
    db.session.add(new_parada)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_paradas.route('/updateparada', methods=['PUT'])
def Update():
    id = request.json['id']
    direccion_origen = request.json['direccion_origen']
    direccion_destino = request.json['direccion_destino']
    idruta = request.json['idruta']
    parada = Parada.query.get(id)   
    if parada :
        print(parada) 
        parada.direccion_origen = direccion_origen
        parada.direccion_destino = direccion_destino
        parada.idruta = idruta
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_paradas.route('/deleteparada/<id>', methods=['DELETE'])
def eliminar(id):
    parada = Parada.query.get(id)
    db.session.delete(parada)
    db.session.commit()
    return jsonify(parada_schema.dump(parada))