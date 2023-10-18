from config.db import  db, ma, app

class Viajero(db.Model):
    __tablename__ = "tblviajero"

    id = db.Column(db.Integer, primary_key =True)
    idusuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    tipodocumento = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    numcelular = db.Column(db.Integer)
    direccion = db.Column(db.String(50))

    def __init__(self, idusuario, tipodocumento, nombre, apellido, edad, numcelular, direccion) :
       self.idusuario = idusuario
       self.tipodocumento = tipodocumento
       self.nombre = nombre 
       self.apellido = apellido
       self.edad = edad
       self.numcelular = numcelular
       self.direccion = direccion

with app.app_context():
    db.create_all()

class ViajerosSchema(ma.Schema):
    class Meta:
        fields = ('id','idusuario','tipodocumento','nombre','apellido','edad','numcelular','direccion')
