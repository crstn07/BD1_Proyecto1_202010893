-- CONSULTA 1: nombre de los candidatos a presidentes y vicepresidentes por partido
SELECT A.presidente, B.vicepresidente, A.partido  FROM
(SELECT C.nombres AS Presidente, P.nombre AS Partido FROM bd1_proyecto1.candidato C
INNER JOIN bd1_proyecto1.partido P 
ON C.partido_id = P.id
WHERE cargo_id = 1) A
INNER JOIN
(SELECT  C.nombres AS Vicepresidente, P.nombre AS Partido FROM bd1_proyecto1.candidato C
INNER JOIN bd1_proyecto1.partido P 
ON C.partido_id = P.id
WHERE cargo_id = 2) B
ON A.partido = B.partido;
