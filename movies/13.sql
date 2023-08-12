SELECT
  name
FROM
  people
  JOIN stars ON people.id = stars.person_id
  JOIN movies ON stars.movie_id = movies.id
WHERE
  NOT name = 'Kevin Bacon'
  AND title IN (
    SELECT
      title
    FROM
      movies
      JOIN stars ON stars.movie_id = movies.id
      JOIN people ON stars.person_id = people.id
    WHERE
      name = 'Kevin Bacon'
      AND birth = 1958
  )
GROUP BY
  name;