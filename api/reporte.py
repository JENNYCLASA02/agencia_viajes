from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReportesSchema

ruta_reportes = Blueprint("ruta_reporte", __name__)

reporte_schema = ReportesSchema()
reportes_schema = ReportesSchema(many=True)

@ruta_reportes.route('/reportes', methods=['GET'])
def scale():
    resultall = Reporte.query.all() #Select * from Reportes
    resultado_reporte= reportes_schema.dump(resultall)
    return jsonify(resultado_reporte)

@ruta_reportes.route('/savereporte', methods=['POST'])
def save():
    fecha_creacion = request.json['fecha_creacion']
    new_reporte = Reporte(fecha_creacion)
    db.session.add(new_reporte)
    db.session.commit()    
    return "los datos han sido guardado con exito"

@ruta_reportes.route('/updatereporte', methods=['PUT'])
def Update():
    id = request.json['id']
    fecha_creacion = request.json['fecha_creacion']
    reporte = Reporte.query.get(id)   
    if reporte :
        print(reporte) 
        reporte.fecha_creacion = fecha_creacion
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_reportes.route('/deletereporte/<id>', methods=['DELETE'])
def eliminar(id):
    reporte = Reporte.query.get(id)
    db.session.delete(reporte)
    db.session.commit()
    return jsonify(reporte_schema.dump(reporte))