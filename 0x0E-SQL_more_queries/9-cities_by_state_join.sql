-- Lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN ON cities.state_id=states.id
ORDER BY cities.id;
