from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje_reporte import Viaje_reporte, Viaje_reportesSchema

ruta_viaje_reportes = Blueprint("ruta_viaje_reporte", __name__)

viaje_reporte_schema = Viaje_reportesSchema()
viaje_reportes_schema = Viaje_reportesSchema(many=True)

@ruta_viaje_reportes.route('/viaje_reportes', methods=['GET'])
def viaje_reporte():
    resultall = Viaje_reporte.query.all() #Select * from Viaje_reportes
    resultado_viaje_reporte= viaje_reportes_schema.dump(resultall)
    return jsonify(resultado_viaje_reporte)

@ruta_viaje_reportes.route('/saveviaje_reporte', methods=['POST'])
def save():
    id_viaje = request.json['id_viaje']
    id_reporte = request.json['id_reporte']
    new_viaje_reporte = Viaje_reporte(id_viaje,id_reporte)
    db.session.add(new_viaje_reporte)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_viaje_reportes.route('/updateviaje_reporte', methods=['PUT'])
def Update():
    id = request.json['id']
    id_viaje = request.json['id_viaje']
    id_reporte = request.json['id_reporte']
    viaje_reporte = Viaje_reporte.query.get(id)   
    if viaje_reporte :
        print(viaje_reporte) 
        viaje_reporte.id_viaje = id_viaje
        viaje_reporte.id_reporte = id_reporte
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_viaje_reportes.route('/deleteviaje_reporte/<id>', methods=['DELETE'])
def eliminar(id):
    viaje_reporte = Viaje_reporte.query.get(id)
    db.session.delete(viaje_reporte)
    db.session.commit()
    return jsonify(viaje_reporte_schema.dump(viaje_reporte))