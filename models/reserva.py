from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('tblviaje.id'))
    id_viajero = db.Column(db.Integer, db.ForeignKey('tblviajero.id'))
    ciudad_origen = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    ciudad_destino = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    dir_origen = db.Column(db.String(50))
    dir_destino = db.Column(db.String(50))
    preferencias = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    estado = db.Column(db.Boolean)
    fecha_recogida = db.Column(db.DateTime)

    def __init__(self, id_viaje, id_viajero, ciudad_origen, ciudad_destino, dir_origen,dir_destino,preferencias,fecha,estado,fecha_recogida) :
       self.id_viaje = id_viaje
       self.id_viajero = id_viajero
       self.ciudad_origen = ciudad_origen
       self.ciudad_destino = ciudad_destino
       self.dir_origen = dir_origen
       self.dir_destino = dir_destino
       self.preferencias = preferencias
       self.fecha = fecha
       self.estado = estado
       self.fecha_recogida = fecha_recogida


with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_viaje','id_viajero','ciudad_origen','ciudad_destino','dir_origen','dir_destino','preferencias','fecha','estado','fecha_recogida')
