SELECT
  name
FROM
  people
  JOIN stars ON people.id = stars.person_id
  JOIN movies ON stars.movie_id = movies.id
WHERE
  YEAR = '2004'
ORDER BY
  birth;