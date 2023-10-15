from config.db import  db, ma, app

class Vehiculo(db.Model):
    __tablename__ = "tblvehiculo"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    placa = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    capacidad_pasajero = db.Column(db.Integer)
    disponibilidad =  db.Column(db.String(50))

    def __init__(self, nombre, placa, modelo, capacidad, disponibilidad) :
       self.nombre = nombre
       self.placa = placa 
       self.modelo = modelo
       self.capacidad = capacidad
       self.disponibilidad = disponibilidad

with app.app_context():
    db.create_all()

class VehiculosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'placa', 'modelo', 'capacidad','disponibilidad')