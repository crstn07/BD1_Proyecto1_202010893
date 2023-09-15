-- CONSULTA 3: Nombre de los candidatos a alcalde por partido
SELECT C.nombres AS Nombre, P.nombre AS Partido FROM bd1_proyecto1.candidato C
INNER JOIN bd1_proyecto1.partido P
ON C.partido_id = P.id
WHERE cargo_id = 6
GROUP BY P.nombre;