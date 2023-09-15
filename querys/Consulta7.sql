-- CONSULTA 7: Top 10 de edad de ciudadanos que realizaron su voto
SELECT COUNT(C.dpi) AS Cantidad, C.edad FROM bd1_proyecto1.ciudadano C
INNER JOIN bd1_proyecto1.voto V
ON C.dpi = V.ciudadano_dpi
GROUP BY C.edad
ORDER BY COUNT(C.dpi) DESC
LIMIT 10;