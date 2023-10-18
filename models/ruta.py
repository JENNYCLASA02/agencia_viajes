from config.db import  db, ma, app

class Ruta(db.Model):
    __tablename__ = "tblruta"

    id = db.Column(db.Integer, primary_key =True)
    origen = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    destino = db.Column(db.Integer, db.ForeignKey('tblciudad.id'))
    distancia = db.Column(db.String(50))
    duracion = db.Column(db.String(50))
    
    def _init_(self,origen, destino,distancia,duracion) :
       self.origen = origen
       self.destino = destino
       self.distancia = distancia
       self.duracion = duracion
       
with app.app_context():
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('id','origen','destino','distancia','duracion')