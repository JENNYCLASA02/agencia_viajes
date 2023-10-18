from config.db import  db, ma, app

class Reporte(db.Model):
    __tablename__ = "tblreporte"

    id = db.Column(db.Integer, primary_key =True)
    fecha_creacion = db.Column(db.DateTime)

    def _init_(self,fecha_creacion) :
       self.fecha_creacion = fecha_creacion 
       
with app.app_context():
    db.create_all()

class ReportesSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha_creacion')