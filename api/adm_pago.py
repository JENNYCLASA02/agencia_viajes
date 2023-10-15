from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.adm_pago import Adm_pago, Adm_pagosSchema

ruta_adm_pagos = Blueprint("ruta_adm_pago", __name__)

adm_pago_schema = Adm_pagosSchema()
adm_pagos_schema = Adm_pagosSchema(many=True)

@ruta_adm_pagos.route('/adm_pagos', methods=['GET'])
def adm_pago():
    resultall = Adm_pago.query.all() #Select * from Adm_pagos
    resultado_adm_pago= adm_pago_schema.dump(resultall)
    return jsonify(resultado_adm_pago)

@ruta_adm_pagos.route('/saveadm_pago', methods=['POST'])
def save():
    metodo_pago = request.json['metodo_pago']
    monto = request.json['monto']
    fecha = request.json['fecha']
    id_viajero = request.json['id_viajero']
    new_adm_pago = Adm_pago(metodo_pago,monto,fecha,id_viajero)
    db.session.add(new_adm_pago)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_adm_pagos.route('/updateadm_pago', methods=['PUT'])
def Update():
    id = request.json['id']
    metodo_pago = request.json['metodo_pago']
    monto = request.json['monto']
    fecha = request.json['fecha']
    id_viajero = request.json['id_viajero']
    adm_pago = Adm_pago.query.get(id)   
    if adm_pago :
        print(adm_pago) 
        adm_pago.metodo_pago = metodo_pago
        adm_pago.monto = monto
        adm_pago.fecha = fecha 
        adm_pago.id_viajero = id_viajero

        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_adm_pagos.route('/deleteadm_pago/<id>', methods=['DELETE'])
def eliminar(id):
    adm_pago = Adm_pago.query.get(id)
    db.session.delete(adm_pago)
    db.session.commit()
    return jsonify(adm_pago_schema.dump(adm_pago))