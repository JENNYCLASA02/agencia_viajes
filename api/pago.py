from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagosSchema

ruta_pagos = Blueprint("ruta_pago", __name__)

pago_schema = PagosSchema()
pagos_schema = PagosSchema(many=True)

@ruta_pagos.route('/pagos', methods=['GET'])
def pago():
    resultall = Pago.query.all() #Select * from Pagos
    resultado_pago= pago_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_pagos.route('/savepago', methods=['POST'])
def save():
    metodo_pago = request.json['metodo_pago']
    monto = request.json['monto']
    fecha = request.json['fecha']
    estado = request.json['estado']
    id_viajero = request.json['id_viajero']
    new_pago = Pago(metodo_pago,monto,fecha,estado,id_viajero)
    db.session.add(new_pago)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_pagos.route('/updatepago', methods=['PUT'])
def Update():
    id = request.json['id']
    metodo_pago = request.json['metodo_pago']
    monto = request.json['monto']
    fecha = request.json['fecha']
    estado = request.json['estado']
    id_viajero = request.json['id_viajero']
    pago = Pago.query.get(id)   
    if pago :
        print(pago) 
        pago.metodo_pago = metodo_pago
        pago.monto = monto
        pago.fecha = fecha 
        pago.estado = estado
        pago.id_viajero = id_viajero

        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_pagos.route('/deletepago/<id>', methods=['DELETE'])
def eliminar(id):
    pago = Pago.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(pago_schema.dump(pago))