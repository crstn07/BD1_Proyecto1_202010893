-- CONSULTA 4: Cantidad de candidatos por partido (presidentes, vicepresidentes, diputados, alcaldes).
SELECT COUNT(C.id) AS Cantidad, P.nombre AS Partido FROM bd1_proyecto1.candidato C
INNER JOIN bd1_proyecto1.partido P
ON C.partido_id = P.id
WHERE cargo_id != -1
GROUP BY P.nombre;