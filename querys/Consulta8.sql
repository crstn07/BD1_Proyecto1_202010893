-- CONSULTA 8: Top 10 de candidatos más votados para presidente y vicepresidente
SELECT  Presi.nombres AS Presidente, Vice.nombres AS Vicepresidente, COUNT(Presi.id) AS `Votos Totales`
FROM (SELECT C.id, C.nombres, C.partido_id FROM bd1_proyecto1.candidato C WHERE C.cargo_id = 1) Presi
INNER JOIN (SELECT C.nombres, C.partido_id FROM bd1_proyecto1.candidato C WHERE C.cargo_id = 2) Vice
ON Presi.partido_id = Vice.partido_id
INNER JOIN bd1_proyecto1.papeleta P
ON Presi.id = P.candidato_id
GROUP BY Presi.id
ORDER BY COUNT(Presi.id) DESC
LIMIT 10;