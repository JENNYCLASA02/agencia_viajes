from config.db import  db, ma, app

class Adm_pago(db.Model):
    _tablename_ = "tbladm_pago"

    id = db.Column(db.Integer, primary_key =True)
    metodo_pago = db.Column(db.String(50))
    monto = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    id_viajero = db.Column(db.Integer, db.ForeignKey('tblviajero.id'))
    
    def _init_(self,metodo_pago,monto,fecha,id_viajero) :
       self.metodo_pago = metodo_pago
       self.monto = monto
       self.fecha = fecha
       self.id_viajero = id_viajero
       
with app.app_context():
    db.create_all()

class Adm_pagosSchema(ma.Schema):
    class Meta:
        fields = ('id','metodo_pago','monto','fecha','id_viajero')