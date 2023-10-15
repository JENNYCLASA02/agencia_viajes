from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    ciudad_origen = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    ciudad_destino = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    dir_origen = db.Column(db.String(50))
    dir_destino = db.Column(db.String(50))
    preferencias = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)

    def __init__(self, ciudad_origen, ciudad_destino, dir_origen,dir_destino,preferencias,fecha) :
       self.ciudad_origen = ciudad_origen
       self.ciudad_destino = ciudad_destino
       self.dir_origen = dir_origen
       self.dir_destino = dir_destino
       self.preferencias = preferencias
       self.fecha = fecha

with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','ciudad_origen','ciudad_destino','dir_origen','dir_destino','preferencias','fecha')
