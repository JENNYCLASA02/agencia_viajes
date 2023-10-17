from config.db import  db, ma, app

class Reporte(db.Model):
    _tablename_ = "tblreporte"

    id = db.Column(db.Integer, primary_key =True)
    fecha_creacion = db.Column(db.DateTime)
    descripcion = db.Column(db.String(50))
    itinerario_det = db.Column(db.String(50))
    ingresos = db.Column(db.Double)

    def _init_(self,fecha_creacion, descripcion, itinerario_det,ingresos) :
       self.fecha_creacion = fecha_creacion 
       self.descripcion = descripcion
       self.itinerario_det = itinerario_det
       self.ingresos = ingresos
       
with app.app_context():
    db.create_all()

class ReportesSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha_creacion','descripcion','itinerario_det','ingresos')