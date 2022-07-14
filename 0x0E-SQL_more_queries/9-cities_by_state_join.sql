-- Script that lists all cities with their state name
-- Query to join the cities of each state
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
