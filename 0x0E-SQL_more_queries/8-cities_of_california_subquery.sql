-- This list all cities in the DB
SELECT cities.* FROM cities, states WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
