-- TABLA PARTIDO
INSERT INTO bd1_proyecto1.partido SELECT * FROM bd1_proyecto1.temp_partido;

-- TABLA CARGO
INSERT INTO bd1_proyecto1.cargo SELECT * FROM bd1_proyecto1.temp_cargo;

-- TABLA CANDIDATO
INSERT INTO bd1_proyecto1.candidato SELECT * FROM bd1_proyecto1.temp_candidato;

-- TABLA CIUDADANO
INSERT INTO bd1_proyecto1.ciudadano SELECT * FROM bd1_proyecto1.temp_ciudadano;

-- TABLA DEPARTAMENTO
INSERT INTO bd1_proyecto1.departamento SELECT * FROM bd1_proyecto1.temp_departamento;

-- TABLA MESA
INSERT INTO bd1_proyecto1.mesa SELECT * FROM bd1_proyecto1.temp_mesa;

-- TABLA VOTO
INSERT INTO bd1_proyecto1.voto SELECT DISTINCT id_voto, fecha_hora, dpi, mesa_id FROM bd1_proyecto1.temp_votaciones;

-- TABLA PAPELETA
INSERT INTO bd1_proyecto1.papeleta (voto_id, candidato_id) SELECT id_voto, id_candidato FROM bd1_proyecto1.temp_votaciones;