-- =========================================
-- DAY 2: Filtering & Aggregation
-- =========================================


-- 1. IN
SELECT *
FROM products
WHERE category IN ('electronics', 'motor');


-- 2. BETWEEN
SELECT *
FROM products
WHERE price BETWEEN 100000 AND 500000;


-- 3. LIKE
SELECT *
FROM products
WHERE name LIKE 't%';


-- 4. NOT
SELECT *
FROM products
WHERE NOT category = 'electronics';


-- 5. COUNT
SELECT COUNT(*)
FROM products;


-- 6. SUM
SELECT SUM(price)
FROM products;


-- 7. AVG
SELECT AVG(price)
FROM products;


-- 8. MIN
SELECT MIN(price)
FROM products;


-- 9. MAX
SELECT MAX(price)
FROM products;


-- 10. GROUP BY + COUNT
SELECT category, COUNT(*)
FROM products
GROUP BY category;


-- 11. GROUP BY + SUM
SELECT category, SUM(price)
FROM products
GROUP BY category;


-- 12. GROUP BY + AVG
SELECT category, AVG(price)
FROM products
GROUP BY category;


-- 13. GROUP BY + HAVING
SELECT category, SUM(price)
FROM products
GROUP BY category
HAVING SUM(price) > 100000;


-- 14. HAVING + COUNT
SELECT category, COUNT(*)
FROM products
GROUP BY category
HAVING COUNT(*) > 1;


-- 15. HAVING + AVG
SELECT category, AVG(price)
FROM products
GROUP BY category
HAVING COUNT(*) > 1;


-- 16. HAVING + MAX
SELECT category, MAX(price)
FROM products
GROUP BY category
HAVING MAX(price) > 100000;