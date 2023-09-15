-- CONSULTA 5: Cantidad de votaciones por departamentos.
SELECT D.nombre AS Departamento, COUNT(D.id) AS `Cantidad Votaciones` FROM bd1_proyecto1.departamento D
INNER JOIN bd1_proyecto1.mesa M
ON D.id = M.departamento_id
INNER JOIN bd1_proyecto1.voto V
ON V.mesa_id = M.id
GROUP BY D.id;