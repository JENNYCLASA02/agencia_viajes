from config.db import  db, ma, app

class Parada(db.Model):
    __tablename__ = "tblparada"

    id = db.Column(db.Integer, primary_key =True)
    direccion_origen = db.Column(db.String(50))
    direccion_destino = db.Column(db.String(50))
    idruta = db.Column(db.Integer, db.ForeignKey('tblruta.id'))

    def __init__(self, direccion_origen,direccion_destino,idruta ) :
       self.direccion_origen = direccion_origen
       self.direccion_destino = direccion_destino
       self.idruta = idruta

with app.app_context():
    db.create_all()

class ParadasSchema(ma.Schema):
    class Meta:
        fields = ('id','direccion_origen','direccion_destino','idruta')
