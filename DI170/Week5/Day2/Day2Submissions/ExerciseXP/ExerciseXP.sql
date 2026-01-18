-- CREATE TABLE item (
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR (50), 
-- price INTEGER
-- )

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

-- INSERT INTO item (item_name, price)
-- VALUES
--     ('Small Desk', 100),
--     ('Large Desk', 300),
--     ('Fan', 80);

SELECT * from item;

-- Use SQL to fetch the following data from the database:
-- All the items.
-- All the items with a price above 80 (80 not included).
-- All the items with a price below 300. (300 included)

-- SELECT select_list
-- FROM table_name
-- WHERE condition;

SELECT * from item WHERE price > 80;

SELECT * from item WHERE price <= 300;


-- CREATE TABLE customer (
-- customer_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50),
-- last_name VARCHAR (50)
-- )

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

-- INSERT INTO customer (first_name, last_name)
-- VALUES
--   ('Greg', 'Jones'),
--   ('Sandra', 'Jones'),
--   ('Scott', 'Scott'),
--   ('Trevor', 'Green'),
--   ('Melanie', 'Johnson');

-- SELECT * from customer;

-- Use SQL to fetch the following data from the database:
-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- All customers whose last name is ‘Jones’.
-- All customers whose firstname is not ‘Scott’.

-- SELECT select_list
-- FROM table_name
-- WHERE condition;

SELECT * from customer WHERE last_name = 'Smith';

SELECT * from customer WHERE last_name = 'Jones';

SELECT * from customer WHERE first_name != 'Scott';