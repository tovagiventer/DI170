CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab (id, name) VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab 
-- since there's no NOT NULL order, it should execute with no issues

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)

SELECT * FROM SecondTab 
-- again, should execute with no issues, especially since it worked with the first table

-- Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- This should count the all the IDs in FirstTab that are nott NULL, so it should be 3.
-- Now that it ran and the result was 0, I figured out that a 'null' value cancels out everything else.

-- Q2. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- This sounds like it should be 4, since it should include all IDs from FirstTab that are not 5, but I expect it will get the same total as the last query(0)..
-- I figured out that the count excludes both the NULL row and the id=5 row, so it ounly counts the other two.

-- Q3. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- This should get 2, because it counts all the rows with IDs unidentical to the IDs in SecondTab, so not 5 and not null.
-- I forgot. Once there is a null value, it cancels out everything else, so since there is a null id in SecondTab, it won't count anything.

-- Q4. What will be the OUTPUT of the following statement?
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- ID from SecondTab should be id=5, so the count from FirstTab should be everything but id=5, but since there is a NULL there too, it sould still get 0.
-- I second-guessed myself. The NULL in FirstTab just means it won't count THAT row, not that it won't count any.