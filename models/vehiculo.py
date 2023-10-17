from config.db import  db, ma, app

class Vehiculo(db.Model):
    __tablename__ = "tblvehiculo"

    id = db.Column(db.Integer, primary_key =True)
    placa = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    capacidad = db.Column(db.Integer)
    disponibilidad =  db.Column(db.Boolean)
    localidad = db.Column(db.String(50))

    def __init__(self, placa, modelo, capacidad, disponibilidad,localidad) :
       self.placa = placa 
       self.modelo = modelo
       self.capacidad = capacidad
       self.disponibilidad = disponibilidad
       self.localidad = localidad

with app.app_context():
    db.create_all()

class VehiculosSchema(ma.Schema):
    class Meta:
        fields = ('id','placa', 'modelo', 'capacidad','disponibilidad','localidad')