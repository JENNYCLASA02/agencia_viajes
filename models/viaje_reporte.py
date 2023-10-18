from config.db import  db, ma, app

class Viaje_reporte(db.Model):
    __tablename__ = "tblviaje_reporte"

    id = db.Column(db.Integer, primary_key =True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('tblviaje.id'))
    id_reporte = db.Column(db.Integer, db.ForeignKey('tblreporte.id'))
    
    def __init__(self, id_viaje, id_reporte):
       self.id_viaje = id_viaje
       self.id_reporte = id_reporte
       
with app.app_context():
    db.create_all()

class Viaje_reportesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_viaje','id_reporte')