SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;

SELECT DISTINCT game
FROM stream;

SELECT DISTINCT channel
FROM stream;

SELECT game, COUNT(*) as number_views
FROM stream
GROUP BY game
ORDER BY number_views DESC;

SELECT country, game, COUNT(*) as number_viewers
FROM stream
WHERE game == "League of Legends"
GROUP BY country
ORDER BY number_viewers DESC;

SELECT player, COUNT(*) as number_streamers
FROM stream
GROUP BY player
ORDER BY number_streamers DESC;

SELECT game,
CASE
  WHEN game == "League of Legends"
    THEN "MOBA"
  WHEN game == "Dota 2"
    THEN "MOBA"
  WHEN game == "Heroes of the Strom"
    THEN "MOBA"
  WHEN game == "Counter-Strike: Global Offensive"
    THEN "FPS"
  WHEN game == "DayZ"
    THEN "Survival"
  WHEN game == "ARK: Survival Evolved"
    THEN "Survival"
  ELSE "Other"
  END AS "genre",
  COUNT(*) AS number_viewers
FROM stream
GROUP BY game
ORDER BY number_viewers DESC;

SELECT time
FROM stream
LIMIT 10;

SELECT time,
   strftime("%S", time)
FROM stream
GROUP BY 1
LIMIT 20;

SELECT strftime("%H", time) as "hour",
   COUNT(*) AS viewer_by_hour,
   country
FROM stream
WHERE country == "BR"
GROUP BY hour
ORDER BY viewer_by_hour DESC;

SELECT stream.game,
  stream.country,
  stream.channel,
  strftime("%H", stream.time) as "hour",
  COUNT(*) viewer_by_country_hour
FROM stream
JOIN chat 
  ON stream.device_id = chat.device_id
GROUP BY hour
ORDER BY viewer_by_country_hour DESC;
