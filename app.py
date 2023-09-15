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

# Nombre de los candidatos a presidentes y vicepresidentes por partido 
@app.route('/consulta1', methods=['GET'])
def consulta1():
    datos = db.consulta1()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 1</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
      <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 1 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">No.</th>
                <th scope="col">Presidente</th>
                <th scope="col">Vicepresidente</th>
                <th scope="col">Partido</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {str(dato['Presidente'])}</td>
                <td scope="col"> {str(dato['Vicepresidente'])}</td>
                <td scope="col"> {str(dato['Partido'])}</td>
            </tr>"""
    contenido_html += """
        </table>
      </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Número de candidatos a diputados por cada partido
@app.route('/consulta2', methods=['GET'])
def consulta2():
    datos = db.consulta2()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 2</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 2 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">No.</th>
                <th scope="col">Cantidad</th>
                <th scope="col">Partido</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Cantidad']}</td>
                <td scope="col"> {str(dato['Partido'])}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Nombre de los candidatos a alcalde por partido
@app.route('/consulta3', methods=['GET'])
def consulta3():
    datos = db.consulta3()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 3</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 3 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">No.</th>
                <th scope="col">Nombre</th>
                <th scope="col">Partido</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {str(dato['Nombre'])}</td>
                <td scope="col"> {str(dato['Partido'])}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos


# Cantidad de candidatos por partido (presidentes, vicepresidentes, diputados, alcaldes).
@app.route('/consulta4', methods=['GET'])
def consulta4():
    datos = db.consulta4()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 4</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 4 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">No.</th>
                <th scope="col">Cantidad</th>
                <th scope="col">Partido</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Cantidad']}</td>
                <td scope="col"> {str(dato['Partido'])}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Cantidad de votaciones por departamentos.
@app.route('/consulta5', methods=['GET'])   
def consulta5():
    datos = db.consulta5()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 5</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 5 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">No.</th>
                <th scope="col">Departamento</th>
                <th scope="col">Cantidad de Votaciones</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Departamento']}</td>
                <td scope="col"> {dato['Cantidad de Votaciones']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Cantidad de votos nulos.
@app.route('/consulta6', methods=['GET'])
def consulta6():
    dato = db.consulta6()
    contenido_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 6</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
        <h1 style="margin-top: 20px;"> <center> Votos Nulos: {dato} </center></h1>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify({"Votos Nulos":dato}) # Retorna un json con los datos

# Top 10 de edad de ciudadanos que realizaron su voto
@app.route('/consulta7', methods=['GET'])
def consulta7():
    datos = db.consulta7()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 7</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 7 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Top</th>
                <th scope="col">Cantidad</th>
                <th scope="col">Edad</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Cantidad']}</td>
                <td scope="col"> {dato['Edad']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Top 10 de candidatos más votados para presidente y vicepresidente (el voto por presidente incluye el vicepresidente)
@app.route('/consulta8', methods=['GET'])
def consulta8():
    datos = db.consulta8()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 8</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 8 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Top</th>
                <th scope="col">Presidente</th>
                <th scope="col">Vicepresidente</th>
                <th scope="col">Votos Totales</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Presidente']}</td>
                <td scope="col"> {dato['Vicepresidente']}</td>
                <td scope="col"> {dato['Votos Totales']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Top 5 de mesas más frecuentadas (mostrar no. Mesa y departamento al que pertenece)
@app.route('/consulta9', methods=['GET'])
def consulta9():
    datos = db.consulta9()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 9</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 9 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Top</th>
                <th scope="col">No. Mesa</th>
                <th scope="col">Departamento</th>
                <th scope="col">Cantidad de Votos</th>
            </tr>
            """
    num = 0
    for dato in datos:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Mesa']}</td>
                <td scope="col"> {dato['Departamento']}</td>
                <td scope="col"> {dato['Votos']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos

# Top 5 la hora más concurrida en que los ciudadanos fueron a votar.
@app.route('/consulta10', methods=['GET'])
def consulta10():
    datos = db.consulta10()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 10</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 10 </center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Top</th>
                <th scope="col">Hora y Minuto</th>
                <th scope="col">Cantidad de Votos</th>
            </tr>
            """
    num = 0
    datos1 = datos['HM']
    for dato in datos1:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Hora y Minuto']}</td>
                <td scope="col"> {dato['Votos']}</td>
            </tr>"""
    contenido_html += """
        </table>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Top</th>
                <th scope="col">Hora</th>
                <th scope="col">Cantidad de Votos</th>
            </tr>"""
    num = 0
    datos2 = datos['H']
    for dato in datos2:
        num+=1
        contenido_html += f"""
            <tr>
                <td scope="col"> {num}</td>
                <td scope="col"> {dato['Hora']}</td>
                <td scope="col"> {dato['Votos']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos


# Cantidad de votos por genero (Masculino, Femenino)
@app.route('/consulta11', methods=['GET'])
def consulta11():
    datos = db.consulta11()
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consulta 11</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    </head>
    <body>
    <div style="position: absolute; width: 90%; left: 5%; top: 20px;">
        <h1 style="margin-bottom: 20px;"> <center> CONSULTA 11</center></h1>
        <table class="table table-ligth table-striped table-hover table-bordered border-dark">
            <tr class="table table-dark">
                <th scope="col">Género</th>
                <th scope="col">Cantidad de Votos</th>
            </tr>
            """
    for dato in datos:
        contenido_html += f"""
            <tr>
                <td scope="col"> {dato['Genero']}</td>
                <td scope="col"> {dato['Votos']}</td>
            </tr>"""
    contenido_html += """
        </table>
    </div>
    </body>
    </html>
    """
    return contenido_html # Retorna una página web con la tabla de datos
    #return jsonify(datos) # Retorna un json con los datos
