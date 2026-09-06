CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    category TEXT
);

INSERT INTO products (id, name, price, category)
VALUES (1, 'laptop', 100000, 'electronics');

INSERT INTO products (id, name, price, category)
VALUES (2, 'phone', 200000, 'electronics');

INSERT INTO products (id, name, price, category)
VALUES (3, 'kawasaki', 1000000, 'motor');

-- SELECT
SELECT * FROM products;

SELECT id, name
FROM products;

-- WHERE
SELECT *
FROM products
WHERE price = 100000;

SELECT *
FROM products
WHERE category = 'electronics';

SELECT *
FROM products
WHERE price >= 100000;

-- AND / OR
SELECT *
FROM products
WHERE price > 100000
AND category = 'electronics';

SELECT *
FROM products
WHERE price = 100000
OR category = 'motor';

-- ORDER BY
SELECT *
FROM products
ORDER BY price;

SELECT *
FROM products
ORDER BY price DESC;

-- LIMIT / OFFSET
SELECT *
FROM products
ORDER BY price
LIMIT 2;

SELECT *
FROM products
ORDER BY price
LIMIT 2 OFFSET 1;

-- UPDATE
UPDATE products
SET price = 150000
WHERE name = 'phone';

-- DELETE
DELETE FROM products
WHERE name = 'tablet';