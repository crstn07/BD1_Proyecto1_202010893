-- CONSULTA 2: Número de candidatos a diputados por cada partido
SELECT COUNT(C.id) AS Cantidad, P.nombre AS Partido FROM bd1_proyecto1.candidato C
INNER JOIN bd1_proyecto1.partido P
ON C.partido_id = P.id
WHERE cargo_id = 3 OR cargo_id = 4 OR cargo_id = 5
GROUP BY P.nombre;
