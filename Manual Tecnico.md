# MANUAL TÉCNICO

## Modelo Conceptual
<img src="./modelos/Modelo Conceptual.png" alt="Modelo Conceptual" width="600px">

## Modelo Lógico
<img src="./modelos/Modelo Logico.png" alt="Modelo Lógico" width="800px">


## Modelo Físico
<img src="./modelos/Modelo Relacional.png" alt="Modelo Físico" width="1000px">
A continuacion se detallan las tablas que conforman el modelo físico de la base de datos, así como sus atributos y descripción. También se detallan las relaciones entre las tablas.

### Partido
Esta tabla almacena la información de los partidos políticos que participan en las elecciones. <br><br>
Atributos:
- **id:** Identificador del partido. Es la llave primaria de la tabla, es de tipo INTEGER y no puede ser nulo.
- **nombre:** Nombre del partido. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el nombre) y no puede ser nulo.
- **siglas:** Siglas del partido. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 15 (adecuado para  las siglas las cuales no son muy extensas) y no puede ser nulo.
- **fundacion:** Fecha de fundación del partido. Es de tipo DATE (porque solo contiene una fecha sin hora) y no puede ser nulo.

### Candidato
Esta tabla almacena la información de los candidatos que participan en las elecciones. <br><br>
Atributos:
- **id:** Identificador del candidato. Es la llave primaria de la tabla, es de tipo INTEGER y no puede ser nulo.
- **nombre:** Nombre del candidato. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el nombre) y no puede ser nulo.
- **fecha_nacimiento:** Fecha de nacimiento del candidato. Es de tipo DATE (porque solo contiene una fecha sin hora) y no puede ser nulo.
- **partido_id:** Identificador del partido al que pertenece el candidato. Es una llave foránea que hace referencia al identificador de la tabla Partido, es de tipo INTEGER y no puede ser nulo.
- **cargo_id:** Identificador del cargo al que aspira el candidato. Es una llave foránea que hace referencia al identificador de la tabla Cargo, es de tipo INTEGER y no puede ser nulo.

### Cargo
Esta tabla almacena la información de los cargos a los que aspiran los candidatos. <br><br>
Atributos:
- **id:** Identificador del cargo. Es la llave primaria de la tabla, es de tipo INTEGER y no puede ser nulo.
- **cargo:** Nombre del cargo. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el nombre) y no puede ser nulo.

### Papeleta
Esta tabla almacena la información de las papeletas (una papeleta diferente por cargo) que se utilizan en las elecciones. <br><br>
Atributos:
- **id:** Identificador de la papeleta. Es la llave primaria de la tabla, es de tipo INTEGER autoincrementable y no puede ser nulo.
- **voto_id:** Identificador del voto al que pertenece la papeleta. Es una llave foránea que hace referencia al identificador de la tabla Voto, es de tipo INTEGER y no puede ser nulo.
- **candidato_id:** Identificador del candidato por el cual se vota en la papeleta. Es una llave foránea que hace referencia al identificador de la tabla Candidato, es de tipo INTEGER y no puede ser nulo.

### Ciudadano
Esta tabla almacena la información de los ciudadanos que participan en las elecciones. <br><br>
Atributos:
- **dpi:** Número de identificación personal del ciudadano. Es la llave primaria de la tabla, es de tipo BIGINT (para poder almacenar correctamente el número debido a que este es muy grande al ser de 13 digitos, no se usó VARCHAR porque los tipos numéricos son más eficientes en términos de almacenamiento y procesamiento además son más fáciles de indexar y buscar, tambien se verificó que ningún dato tuviera ceros a la izquierda porque al guardar como entero eliminaría esos ceros y cambiaría con respecto al dato original) y no puede ser nulo.
- **nombre:** Nombre del ciudadano. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el nombre) y no puede ser nulo.
- **apellido:** Apellido del ciudadano. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el apellido) y no puede ser nulo.
- **direccion:** Dirección del ciudadano. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 100 (para que tenga sufciente espacio para almacenar toda la dirección) y no puede ser nulo.
- **telefono:** Número de teléfono del ciudadano. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 10 (porque en los archivos de entrada siempre tiene esa misma longitud) y no puede ser nulo.
- **edad:** Edad del ciudadano. Es de tipo INTEGER (porque es un dato numérico) y no puede ser nulo.
- **genero:** Género del ciudadano. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 1 (ya que solo contiene una letra) y no puede ser nulo.

### Voto
Esta tabla almacena la información de los votos que se realizan en las elecciones. <br><br>
Atributos:
- **id:** Identificador del voto. Es la llave primaria de la tabla, es de tipo INTEGER autoincrementable y no puede ser nulo.
- **fecha_hora:** Fecha y hora en la que se realizó el voto. Es de tipo DATETIME (porque contiene una fecha con hora) y no puede ser nulo.
- **mesa_id:** Identificador de la mesa en la que se realizó el voto. Es una llave foránea que hace referencia al identificador de la tabla Mesa, es de tipo INTEGER y no puede ser nulo.
- **ciudadano_id:** Identificador del ciudadano que realizó el voto. Es una llave foránea que hace referencia al identificador de la tabla Ciudadano, es de tipo BIGINT y no puede ser nulo.

### Mesa
Esta tabla almacena la información de las mesas en las que se realizan los votos. <br><br>
Atributos:
- **id:** Identificador de la mesa. Es la llave primaria de la tabla, es de tipo INTEGER autoincrementable y no puede ser nulo.
- **departamento_id:** Identificador del departamento en el que se realizó el voto. Es una llave foránea que hace referencia al identificador de la tabla Departamento, es de tipo INTEGER y no puede ser nulo.

### Departamento
Esta tabla almacena la información de los 22 departamentos de Guatemala en los que se realizan los votos. <br><br>
Atributos:
- **id:** Identificador del departamento. Es la llave primaria de la tabla, es de tipo INTEGER autoincrementable y no puede ser nulo.
- **nombre:** Nombre del departamento. Es de tipo VARCHAR (porque es una cadena de texto) con un tamaño de 50 (para que tenga sufciente espacio para almacenar todo el nombre) y no puede ser nulo.

### Relaciones
- **Partido-Candidato:** Un partido tiene uno a muchos candidatos, un candidato pertenece a un partido.
- **Cargo-Candidato:** Un cargo tiene uno o muchos candidatos, un candidato aspira a un cargo.
- **Candidato-Papeleta:** Un candidato está en una o muchas papeletas, una papeleta contiene a un candidato.
- **Voto-Papeleta:** Un voto tiene una o muchas papeletas, una papeleta pertenece a un voto.
- **Ciudadano-Voto:** Un ciudadano puede ejercer uno o muchos votos, un voto pertenece a un ciudadano.
- **Mesa-Voto:** Una mesa puede tener uno o muchos votos, un voto pertenece a una mesa.
- **Departamento-Mesa:** Un departamento tiene una o muchas mesas, una mesa pertenece a un departamento.

## Creación de la Base de Datos
Para crear el la base de datos con el nombre 'bd1_proyecto1' con las tablas descritas en el modelo físico se utilizó el siguiente script:
```sql
-- CREAR BASE DE DATOS
CREATE SCHEMA IF NOT EXISTS bd1_proyecto1;

--  TABLA PARTIDO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.partido (
	id INTEGER NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	siglas VARCHAR(15) NOT NULL,
	fundacion DATE NOT NULL,
	PRIMARY KEY (id));

-- TABLA CARGO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.cargo (
	id INTEGER NOT NULL,
	cargo VARCHAR(50) NOT NULL,
	PRIMARY KEY (id));

-- TABLA CANDIDATO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.candidato (
	id INTEGER NOT NULL,
	nombres VARCHAR(50) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
    partido_id INTEGER NOT NULL,
    cargo_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (cargo_id) REFERENCES bd1_proyecto1.cargo(id),
	FOREIGN KEY (partido_id) REFERENCES bd1_proyecto1.partido(id)
  );
  
-- TABLA CIUDADANO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.ciudadano (
	dpi BIGINT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    edad INTEGER NOT NULL,
    genero VARCHAR(1) NOT NULL,
	PRIMARY KEY (dpi)
);

-- TABLA DEPARTAMENTO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.departamento (
	id INTEGER NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);

-- TABLA MESA
CREATE TABLE IF NOT EXISTS bd1_proyecto1.mesa (
	id INTEGER NOT NULL AUTO_INCREMENT,
	departamento_id INTEGER NOT NULL,
	PRIMARY KEY (id),
    FOREIGN KEY (departamento_id) REFERENCES bd1_proyecto1.departamento(id)
);

-- TABLA VOTO
CREATE TABLE IF NOT EXISTS bd1_proyecto1.voto (
	id INTEGER NOT NULL AUTO_INCREMENT,
    fecha_hora DATETIME NOT NULL,
    ciudadano_dpi BIGINT NOT NULL,
	mesa_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (ciudadano_dpi) REFERENCES bd1_proyecto1.ciudadano(dpi),
    FOREIGN KEY (mesa_id) REFERENCES bd1_proyecto1.mesa(id)
);

-- TABLA PAPELETA
CREATE TABLE IF NOT EXISTS bd1_proyecto1.papeleta (
	id INTEGER NOT NULL AUTO_INCREMENT,
    voto_id INTEGER NOT NULL,
    candidato_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (voto_id) REFERENCES bd1_proyecto1.voto(id),
    FOREIGN KEY (candidato_id) REFERENCES bd1_proyecto1.candidato(id)
);
```

## Carga de Datos
Para cargar los datos se utilizo una api en python, la función 'cargarTablatemporal()' es la encargada de esto. Primero abre el archivo .sql que contiene un script para crear unas tablas temporales en la base de datos que tienen la misma estructura de los archivos de entrada, luego abre y lee el contenido de cada uno de los archivos .csv que contienen los datos de cada tabla y los inserta en la tabla temporal correspondiente en la base de datos. Por último carga los datos de las tablas temporales a las tablas del modelo.

El script utilizado para la creación de las tablas temporales es el siguiente:	<br>

```sql
-- CREACION DE TABLA TEMPORAL DE VOTACIONES
CREATE TEMPORARY TABLE bd1_proyecto1.temp_votaciones (
	id_voto INTEGER NOT NULL,
	id_candidato INTEGER NOT NULL,
    dpi BIGINT NOT NULL,
    mesa_id INTEGER NOT NULL,
    fecha_hora DATETIME NOT NULL
);

-- CREACION DE TABLA TEMPORAL PARTIDO
CREATE TEMPORARY TABLE bd1_proyecto1.temp_partido (
	id INTEGER NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	siglas VARCHAR(15) NOT NULL,
	fundacion DATE NOT NULL
);

-- CREACION DE TABLA TEMPORAL MESA
CREATE TEMPORARY TABLE bd1_proyecto1.temp_mesa (
	id INTEGER NOT NULL,
	departamento_id INTEGER NOT NULL
);

-- CREACION DE TABLA TEMPORAL DEPARTAMENTO
CREATE TEMPORARY TABLE bd1_proyecto1.temp_departamento (
	id INTEGER NOT NULL,
	nombre VARCHAR(50) NOT NULL
);

-- CREACION DE TABLA TEMPORAL CIUDADANO
CREATE TEMPORARY TABLE bd1_proyecto1.temp_ciudadano (
	dpi BIGINT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
	edad INTEGER NOT NULL,
    genero VARCHAR(1) NOT NULL
);

-- CREACION DE TABLA TEMPORAL CARGO
CREATE TEMPORARY TABLE bd1_proyecto1.temp_cargo (
	id INTEGER NOT NULL,
	cargo VARCHAR(50) NOT NULL
);

-- CREACION DE TABLA TEMPORAL CANDIDATO
CREATE TEMPORARY TABLE bd1_proyecto1.temp_candidato (
	id INTEGER NOT NULL,
	nombres VARCHAR(50) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
    partido_id INTEGER NOT NULL,
    cargo_id INTEGER NOT NULL
);
```

<br>El código utilizado para la carga de datos a las tablas temporales es el siguiente: <br>

```python
def cargarTablaTemporal(self):
    # Crea las tablas temporales en la base de datos
    with open('./querys/Creacion Tablas Temporales.sql', 'r', encoding='utf-8') as archivo:
        SCRIPT = archivo.read()
    commands = SCRIPT.split(";")
    try:
        for command in commands:
            if command == "":
                continue
            self.cursor.execute(command)
            self.connection.commit()
    except Exception as e:
        return ({"Mensaje": "Error al crear la tabla temporal -> " + str(e.args)})
        

    # Carga el archivo de votaciones a su tabla temporal
    with open('./carga/votaciones.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            id_candidato = int(registro[1])
            dpi = int(registro[2])
            mesa_id = int(registro[3])
            fecha = registro[4]
            # Formatea la fecha en el formato YYYY/MM/DD HH:MM:SS
            fecha = datetime.strptime(fecha, "%d/%m/%Y %H:%M").strftime("%Y/%m/%d %H:%M:%S")
            query = f'INSERT INTO bd1_proyecto1.temp_votaciones VALUES ({id},{id_candidato},{dpi},{mesa_id},"{fecha}");'
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
    
    # Carga el archivo de partidos a su tabla temporal
    with open('./carga/partidos.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            nombre = registro[1]
            siglas = registro[2]
            fundacion = registro[3]
            # Formatea la fecha en el formato YYYY/MM/DD
            fundacion = datetime.strptime(fundacion, "%d/%m/%Y").strftime("%Y/%m/%d")
            query = f'INSERT INTO bd1_proyecto1.temp_partido VALUES ({id},"{nombre}","{siglas}","{fundacion}");'
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})


    # Carga el archivo de mesas a su tabla temporal
    with open('./carga/mesas.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            departemento_id = int(registro[1])
            query = f"INSERT INTO bd1_proyecto1.temp_mesa VALUES ({id},{departemento_id});"
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})

    
    # Carga el archivo de departamentos a su tabla temporal
    with open('./carga/departamentos.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            nombre = registro[1]
            query = f'INSERT INTO bd1_proyecto1.temp_departamento VALUES ({id},"{nombre}");'
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                
        
    # Carga el archivo de ciudadanos a su tabla temporal
    with open('./carga/ciudadanos.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            dpi = int(registro[0])
            nombre = registro[1]
            apellido = registro[2]
            direccion = registro[3]
            telefono = registro[4]
            edad = int(registro[5])
            genero = registro[6]
            query = f"""INSERT INTO bd1_proyecto1.temp_ciudadano 
                        VALUES ({dpi},"{nombre}","{apellido}","{direccion}","{telefono}",{edad},"{genero}");"""
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                
    
    # Carga el archivo de cargos a su tabla temporal
    with open('./carga/cargos.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            cargo = registro[1]
            query = f'INSERT INTO bd1_proyecto1.temp_cargo VALUES ({id},"{cargo}");'
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                

    # Carga el archivo de candidatos a su tabla temporal
    with open('./carga/candidatos.csv', 'r', encoding='utf-8') as archivo_csv:
        leido = csv.reader(archivo_csv)
        next(leido) # Omite los encabezados al saltar la primera linea
        for registro in leido:
            id = int(registro[0])
            nombre = registro[1]
            fecha = registro[2]
            # Formatea la fecha en el formato YYYY/MM/DD
            fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y/%m/%d")
            partido_id = int(registro[3])
            cargo_id = int(registro[4])
            query = f"""INSERT INTO bd1_proyecto1.temp_candidato
                    VALUES ({id},"{nombre}","{fecha}",{partido_id},{cargo_id});"""
            try:
                self.cursor.execute(query) 
                self.connection.commit()
            except Exception as e:
                self.close()
                return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                


    # Carga los datos de las tablas temporales a las tablas del modelo
    with open('./querys/Carga de Modelo.sql', 'r', encoding='utf-8') as archivo:
        SCRIPT = archivo.read()
    commands = SCRIPT.split(";")
    try:
        for command in commands:
            if command == "":
                continue
            self.cursor.execute(command)
            self.connection.commit()
    except Exception as e:
        return ({"Mensaje": "Error al cargar los datos al modelo -> " + str(e.args)})
        
    
    self.close()
    self.restartConnection()
    return ({"Mensaje": "Se Cargaron los Datos de las Tablas Temporales hacia el Modelo"})
```