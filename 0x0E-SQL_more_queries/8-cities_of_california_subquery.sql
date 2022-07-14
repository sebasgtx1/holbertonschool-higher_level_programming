-- Script that lists all the cities of California
-- Query to list all the cities from California
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
