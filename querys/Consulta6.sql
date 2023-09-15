-- CONSULTA 6: Cantidad de votos nulos.
SELECT COUNT(N.voto_id) AS `Votos Nulos` FROM
(SELECT DISTINCT P.voto_id FROM bd1_proyecto1.papeleta P
INNER JOIN bd1_proyecto1.Candidato C
ON P.candidato_id = C.id
INNER JOIN bd1_proyecto1.voto V
ON P.voto_id = V.id
WHERE C.cargo_id = -1) N;