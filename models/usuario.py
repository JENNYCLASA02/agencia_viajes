from config.db import  db, ma, app

class Usuario(db.Model):
    _tablename_ = "tblusuario"

    id = db.Column(db.Integer, primary_key =True)
    nombre_usuario = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    
    def _init_(self,nombre_usuario, correo, contraseña) :
       self.nombre_usuario = nombre_usuario
       self.correo = correo
       self.contraseña = contraseña
       
with app.app_context():
    db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_usuario','correo','contraseña')