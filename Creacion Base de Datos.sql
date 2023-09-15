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