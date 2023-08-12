SELECT
    name
FROM
    people
    JOIN 

    SELECT
        title
    FROM
        movies
        JOIN stars ON stars.movie_id = movies.id
        JOIN people ON stars.person_id = people.id
    WHERE
        name = 'Kevin Bacon'
        AND birth = 1958;