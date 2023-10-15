from config.db import  db, ma, app

class Viajero(db.Model):
    __tablename__ = "tblviajero"

    id = db.Column(db.Integer, primary_key =True)
    tipo_documento = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    num_celular = db.Column(db.Integer)
    direccion = db.Column(db.String(50))

    def __init__(self, tipo_documento, nombre, apellido, edad, correo, num_celular, direccion) :
       self.tipo_documento = tipo_documento
       self.nombre = nombre 
       self.apellido = apellido
       self.edad = edad
       self.correo = correo
       self.num_celular = num_celular
       self.direccion = direccion

with app.app_context():
    db.create_all()

class ViajerosSchema(ma.Schema):
    class Meta:
        fields = ('id','tipo_documento','nombre', 'apellido', 'edad', 'correo', 'num_celular', 'direccion')
