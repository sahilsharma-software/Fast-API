/*
==========================================================
DAY 4 — SQL JOINS
==========================================================

JOIN is used to combine rows from two or more tables
using a related column.

Usually:
Primary Key ↔ Foreign Key

Example:
customers.id = orders.customer_id
*/


/*
==========================================================
1. INNER JOIN
==========================================================

Returns only rows that have a match in BOTH tables.

Example:
customers
id | name

orders
id | product | customer_id
*/

SELECT customers.name, orders.product
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;


/*
----------------------------------------------------------
INNER JOIN + WHERE
----------------------------------------------------------

Find products ordered by Aman.
*/

SELECT orders.product
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
WHERE customers.name = 'Aman';


/*
==========================================================
2. LEFT JOIN
==========================================================

Returns ALL rows from the LEFT table.

If no matching row exists in the right table,
the right-side columns become NULL.

Example:
Show every customer and their orders.
*/

SELECT customers.name, orders.product
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id;


/*
==========================================================
3. LEFT JOIN + GROUP BY + COUNT
==========================================================

Find how many orders each customer has.

COUNT(orders.id) is important because orders.id
will be NULL when a customer has no orders.

COUNT(column) ignores NULL values.
*/

SELECT customers.name, COUNT(orders.id)
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.id;


/*
==========================================================
4. LEFT JOIN + HAVING
==========================================================

Find customers who have placed more than 1 order.
*/

SELECT customers.name, COUNT(orders.id)
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.id
HAVING COUNT(orders.id) > 1;


/*
==========================================================
5. COUNT(*) vs COUNT(column)
==========================================================

For a LEFT JOIN:

COUNT(*) 
→ Counts the resulting row.

COUNT(orders.id)
→ Counts only non-NULL order IDs.

Therefore, if a customer has zero orders:

COUNT(*)        → 1
COUNT(orders.id) → 0
*/


/*
==========================================================
6. IMPORTANT: CONDITION IN ON vs WHERE
==========================================================

Suppose we want ALL customers, but we don't want
to count Phone orders.

Put the condition in ON:

*/

SELECT customers.name, COUNT(orders.id)
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
AND orders.product != 'Phone'
GROUP BY customers.id;


/*
If we put the condition in WHERE instead:

WHERE orders.product != 'Phone'

customers with no orders have orders.product = NULL
and may get filtered out.

So with LEFT JOIN:

Condition in ON
→ preserves unmatched rows.

Condition in WHERE
→ can remove unmatched rows.
*/


/*
==========================================================
7. RIGHT JOIN
==========================================================

RIGHT JOIN returns all rows from the RIGHT table.

SQLite traditionally did not support RIGHT JOIN,
so we can usually swap the tables and use LEFT JOIN.

Example:

RIGHT JOIN idea:

A RIGHT JOIN B

can often be rewritten as:

B LEFT JOIN A
*/


/*
==========================================================
8. FULL OUTER JOIN
==========================================================

Returns:

- Matching rows
- Unmatched rows from LEFT table
- Unmatched rows from RIGHT table

Conceptually:

INNER JOIN
+
unmatched LEFT rows
+
unmatched RIGHT rows
*/

SELECT employees.name, salaries.salary
FROM employees
FULL OUTER JOIN salaries
ON employees.id = salaries.employee_id;


/*
==========================================================
9. JOIN TYPES — QUICK REVISION
==========================================================

INNER JOIN
→ Only matching rows.

LEFT JOIN
→ All rows from LEFT table
  + matching rows from RIGHT table.

RIGHT JOIN
→ All rows from RIGHT table
  + matching rows from LEFT table.

FULL OUTER JOIN
→ All rows from both tables.
*/


/*
==========================================================
10. INTERVIEW POINTS
==========================================================

1. JOIN combines related data from multiple tables.

2. INNER JOIN returns only matching records.

3. LEFT JOIN keeps all records from the left table.

4. In LEFT JOIN, COUNT(right_table.id) can return 0
   for unmatched rows because NULL values are ignored.

5. WHERE filters rows.
   HAVING filters groups after GROUP BY.

6. When using LEFT JOIN, a condition on the right table
   in WHERE can remove unmatched rows.

7. JOIN is commonly performed using:
   Primary Key ↔ Foreign Key
*/