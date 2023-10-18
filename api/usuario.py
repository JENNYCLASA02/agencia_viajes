from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.usuario import Usuario, UsuariosSchema

ruta_usuarios = Blueprint("ruta_usuario", __name__)

usuario_schema = UsuariosSchema()
usuarios_schema = UsuariosSchema(many=True)

@ruta_usuarios.route('/usuarios', methods=['GET'])
def usuario():
    resultall = Usuario.query.all() #Select * from usuario
    resultado_usuario= usuario_schema.dump(resultall)
    return jsonify(resultado_usuario)

@ruta_usuarios.route('/saveusuario', methods=['POST'])
def save():
    nombreusuario = request.json['nombreusuario']
    correo = request.json['correo']
    contrasena = request.json ['contrasena']
    new_usuario = Usuario(nombreusuario, correo, contrasena)
    db.session.add(new_usuario)
    db.session.commit()    
    return "los datos han sido guardado con exito"

@ruta_usuarios.route('/updateusuario', methods=['PUT'])
def Update():
    id = request.json['id']
    nombreusuario = request.json['nombreusuario']
    correo = request.json['correo']
    contrasena = request.json ['contrasena']
    usuario = Usuario.query.get(id)   
    if usuario :
        print(usuario) 
        usuario.nombreusuario = nombreusuario
        usuario.correo = correo
        usuario.contrasena = contrasena
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_usuarios.route('/deleteusuario/<id>', methods=['DELETE'])
def eliminar(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario))