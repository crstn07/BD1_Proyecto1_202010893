-- CONSULTA 11: Cantidad de votos por genero (Masculino, Femenino)
SELECT C.genero, COUNT(C.dpi) AS Votos
FROM bd1_proyecto1.ciudadano C
INNER JOIN bd1_proyecto1.voto V
ON C.dpi = V.ciudadano_dpi
GROUP BY C.genero;
