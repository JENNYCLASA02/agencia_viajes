from config.db import  db, ma, app

class Vehiculo_conductor(db.Model):
    __tablename__ = "tblvehiculo_conductor"

    id = db.Column(db.Integer, primary_key =True)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('tblvehiculo.id'))
    id_conductor = db.Column(db.Integer, db.ForeignKey('tblconductor.id'))

    def __init__(self, id_vehiculo, id_conductor) :
       self.id_vehiculo = id_vehiculo
       self.id_conductor = id_conductor

with app.app_context():
    db.create_all()

class Vehiculo_conductoresSchema(ma.Schema):
    class Meta:
        fields = ('id','id_vehiculo', 'id_conductor')
