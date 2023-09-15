-- CONSULTA 9: Top 5 de mesas más frecuentadas
SELECT  M.id AS Mesa, D.nombre AS Departamento, COUNT(M.id) AS `Cantidad de Votos`
FROM bd1_proyecto1.mesa M
INNER JOIN bd1_proyecto1.departamento D
ON M.departamento_id = D.id
INNER JOIN bd1_proyecto1.voto V
ON V.mesa_id = M.id
GROUP BY M.id
ORDER BY COUNT(M.id) DESC
LIMIT 5;