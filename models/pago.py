from config.db import  db, ma, app

class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key =True)
    metodo_pago = db.Column(db.String(50))
    monto = db.Column(db.Double)
    fecha = db.Column(db.DateTime)
    estado = db.Column(db.Boolean)
    id_viajero = db.Column(db.Integer, db.ForeignKey('tblviajero.id'))
    
    def _init_(self,metodo_pago,monto,fecha,estado,id_viajero) :
       self.metodo_pago = metodo_pago
       self.monto = monto
       self.fecha = fecha
       self.estado = estado
       self.id_viajero = id_viajero
       
with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('id','metodo_pago','monto','fecha','estado','id_viajero')