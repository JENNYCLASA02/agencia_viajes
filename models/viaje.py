from config.db import  db, ma, app

class Viaje(db.Model):
    __tablename__ = "tblviaje"

    id = db.Column(db.Integer, primary_key =True)
    hora_inicio = db.Column(db.DateTime)
    hora_finalizacion = db.Column(db.DateTime)
    fecha = db.Column(db.DateTime)
    duracion = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey("tblvehiculo.id") )
    
    def __init__(self, hora_inicio, hora_finalizacion, fecha, duracion, estado,id_vehiculo) :
       self.hora_inicio = hora_inicio
       self.hora_finalizacion = hora_finalizacion
       self.fecha = fecha
       self.duracion = duracion
       self.estado = estado
       self.id_vehiculo = id_vehiculo

with app.app_context():
    db.create_all()

class ViajesSchema(ma.Schema):
    class Meta:
        fields = ('id','hora_inicio','hora_finalizacion','fecha','duracion','estado','id_vehiculo')
