-- CONSULTA 10: Top 5 la hora más concurrida en que los ciudadanos fueron a votar.
SELECT fecha_hora AS `Hora y Minuto`, COUNT(fecha_hora) AS Votos
FROM bd1_proyecto1.voto
GROUP BY fecha_hora
ORDER BY COUNT(fecha_hora) DESC
LIMIT 5;

SELECT HOUR(fecha_hora) AS Hora, COUNT(HOUR(fecha_hora)) AS Votos FROM bd1_proyecto1.voto
GROUP BY HOUR(fecha_hora)
ORDER BY COUNT(HOUR(fecha_hora)) DESC
LIMIT 5;
