from flask import Flask, jsonify, request
from flask_cors import CORS
from db import DB


app = Flask(__name__)
CORS(app)

db = DB()
#db.close()

@app.route('/crearmodelo', methods=['GET'])
def crearmodelo():
    return jsonify(db.crearModelo())


@app.route('/cargartabtemp', methods=['GET'])
def cargartabtemp():
    return jsonify(db.cargarTablaTemporal())

@app.route('/eliminarmodelo', methods=['GET'])
def eliminarmodelo():
    return jsonify(db.eliminarModelo())