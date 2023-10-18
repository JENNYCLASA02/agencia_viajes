from config.db import  db, ma, app

class Conductor(db.Model):
    __tablename__ = "tblconductor"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    numero = db.Column(db.String(50))
    experiencia = db.Column(db.String(50))

    def __init__(self, nombre, apellido, numero, experiencia) :
       self.nombre = nombre
       self.apellido = apellido
       self.numero = numero
       self.experiencia = experiencia

with app.app_context():
    db.create_all()

class ConductoresSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido','numero','experiencia')
