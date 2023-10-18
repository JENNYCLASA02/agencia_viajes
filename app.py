from flask import Flask, jsonify,json
from config.db import  db, ma, app

from api.usuario import Usuario, ruta_usuarios
from api.ciudad import Ciudad, ruta_ciudades
from api.viajero import Viajero, ruta_viajeros
from api.reporte import Reporte, ruta_reportes
from api.conductor import Conductor, ruta_conductores
from api.vehiculo import Vehiculo, ruta_vehiculos
from api.ruta import Ruta, ruta_rutas
from api.parada import Parada, ruta_paradas
from api.viaje import Viaje, ruta_viajes
from api.viaje_reporte import Viaje_reporte, ruta_viaje_reportes
from api.pago import Pago, ruta_pagos
from api.vehiculo_conductor import Vehiculo_conductor, ruta_vehiculo_conductores
from api.reserva import Reserva, ruta_reservas

app.register_blueprint(ruta_usuarios,url_prefix = '/api')
app.register_blueprint(ruta_ciudades,url_prefix = '/api')
app.register_blueprint(ruta_viajeros,url_prefix = '/api')
app.register_blueprint(ruta_reportes,url_prefix = '/api')
app.register_blueprint(ruta_conductores,url_prefix = '/api')
app.register_blueprint(ruta_vehiculos,url_prefix = '/api')
app.register_blueprint(ruta_rutas,url_prefix = '/api')
app.register_blueprint(ruta_paradas,url_prefix = '/api')
app.register_blueprint(ruta_viajes,url_prefix = '/api')
app.register_blueprint(ruta_viaje_reportes,url_prefix = '/api')
app.register_blueprint(ruta_pagos,url_prefix = '/api')
app.register_blueprint(ruta_vehiculo_conductores,url_prefix = '/api')
app.register_blueprint(ruta_reservas,url_prefix = '/api')



@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')