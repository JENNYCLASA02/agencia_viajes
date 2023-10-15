from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.viajero import Viajero, ruta_viajeros
from api.ciudad import Ciudad, ruta_ciudades
from api.vehiculo import Vehiculo, ruta_vehiculos
from api.viaje import Viaje, ruta_viajes
from api.adm_pago import Adm_pago, ruta_adm_pagos
from api.reserva import Reserva, ruta_reservas

app.register_blueprint(ruta_viajeros,url_prefix = '/api')
app.register_blueprint(ruta_ciudades,url_prefix = '/api')
app.register_blueprint(ruta_vehiculos,url_prefix = '/api')
app.register_blueprint(ruta_viajes,url_prefix = '/api')
app.register_blueprint(ruta_adm_pagos,url_prefix = '/api')
app.register_blueprint(ruta_reservas,url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')