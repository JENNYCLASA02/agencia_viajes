from config.db import  db, ma, app

class Viaje(db.Model):
    __tablename__ = "tblviaje"

    id = db.Column(db.Integer, primary_key =True)
    id_ruta = db.Column(db.Integer, db.ForeignKey("tblruta.id"))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey("tblvehiculo.id"))
    id_reporte = db.Column(db.Integer, db.ForeignKey("tblreporte.id"))
    fecha_inicio = db.Column(db.DateTime)
    fecha_finalizacion = db.Column(db.DateTime)
    estado = db.Column(db.Boolean)

    def __init__(self,id_ruta, id_vehiculo, id_reporte,fecha_inicio,fecha_finalizacion,estado) :
       self.id_ruta = id_ruta
       self.id_vehiculo = id_vehiculo
       self.id_reporte = id_reporte
       self.fecha_inicio = fecha_inicio
       self.fecha_finalizacion = fecha_finalizacion
       self.estado = estado
       
with app.app_context():
    db.create_all()

class ViajesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_ruta','id_vehiculo','id_reporte','fecha_inicio','fecha_finalizacion','estado',)
