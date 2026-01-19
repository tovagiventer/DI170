CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','1970-10-08', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','1961-05-06', 2);

UPDATE actors 
SET age='1970-01-01' 
WHERE first_name='Matt' AND last_name='Damon'
RETURNING 
    actor_id,
    first_name, 
    last_name,
    age;

ALTER TABLE actors RENAME COLUMN age TO birth_date;

-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Angelina', 'Jolie', 2); 
--   -- I expect an error -> it can't add it without all values defined

INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Ben', 'Affleck', '', 2);
  -- I expect this also not to work because all fields say NOT NULL