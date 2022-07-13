-- Displays the average temperature of the top 3 cities
-- Query to display the top 3 average temperature by city ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
