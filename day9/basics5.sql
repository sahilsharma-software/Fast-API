/*
==========================================================
DAY 5 — DATABASE DESIGN, NORMALIZATION & INDEXES
==========================================================

Topics:
1. Database Design
2. Normalization
3. 1NF
4. 2NF
5. 3NF
6. Relationships in Database Design
7. Indexes
8. Composite Index
9. EXPLAIN QUERY PLAN
*/


/*
==========================================================
1. DATABASE DESIGN
==========================================================

A good database design:

- Reduces duplicate data
- Avoids unnecessary NULL values
- Prevents update anomalies
- Makes data easier to maintain
- Improves scalability

Instead of storing everything in one large table,
we separate data into related tables.

Example:

customers
products
orders
order_products
*/


/*
==========================================================
2. NORMALIZATION
==========================================================

Normalization is the process of organizing data into
related tables to reduce redundancy and improve
data consistency.

Main normal forms:

1NF → Atomic values
2NF → No partial dependency
3NF → No transitive dependency
*/


/*
==========================================================
3. FIRST NORMAL FORM (1NF)
==========================================================

Rules:

- Each cell should contain a single/atomic value.
- No repeating groups.

BAD:

student_id | student_name | courses
1          | Sahil        | SQL, Python, FastAPI

courses contains multiple values.

GOOD:

student_id | student_name | course
1          | Sahil        | SQL
1          | Sahil        | Python
1          | Sahil        | FastAPI

Important:
Repeated values across different rows do NOT violate 1NF.

The problem is multiple values inside one cell.
*/


/*
==========================================================
4. SECOND NORMAL FORM (2NF)
==========================================================

2NF requires:

1. Table must be in 1NF.
2. No partial dependency on a composite primary key.

Example:

student_id | course_id | student_name | course_name
1          | 101       | Sahil        | SQL
1          | 102       | Sahil        | Python
2          | 101       | Aman         | SQL

Assume:

PRIMARY KEY = (student_id, course_id)

Dependencies:

student_id  → student_name
course_id   → course_name

These attributes depend on only PART of the
composite key.

This is a partial dependency.

Therefore, the table violates 2NF.


Solution:

students
--------
student_id
student_name

courses
-------
course_id
course_name

student_course
--------------
student_id
course_id
*/


/*
==========================================================
5. THIRD NORMAL FORM (3NF)
==========================================================

3NF requires:

1. Table must be in 2NF.
2. No transitive dependency.

Example:

student_id | student_name | department_id | department_name

Dependencies:

student_id → department_id
department_id → department_name

Therefore:

student_id → department_name

through department_id.

This is a transitive dependency.

Solution:

students
--------
student_id
student_name
department_id

departments
-----------
department_id
department_name
*/


/*
==========================================================
6. E-COMMERCE DATABASE DESIGN
==========================================================

Instead of one large table:

orders
------------------------------------------------
order_id
customer_id
customer_name
customer_city
product_id
product_name
category
price
quantity

Separate entities:

customers
---------
id
name
city

products
--------
id
name
category
price

orders
------
id
customer_id

order_products
--------------
order_id
product_id
quantity


Relationship:

Customer 1 : N Order

Order N : M Product

The N:M relationship is implemented using
order_products (junction/bridge table).

Quantity belongs to order_products because it depends
on a particular order + product combination.
*/


/*
==========================================================
7. WHY NOT DIRECTLY CUSTOMER ↔ PRODUCT?
==========================================================

A customer may buy the same product multiple times.

For example:

Order 1 → Laptop → quantity 1
Order 2 → Laptop → quantity 2

A direct:

customer_product
----------------
customer_id
product_id

would not tell us:

- Which order?
- Quantity?
- Purchase date?
- Price at purchase?
- Discount?

Therefore:

Customer → Orders
Order → Products

is a better representation for an e-commerce system.
*/


/*
==========================================================
8. INDEX
==========================================================

An index is an additional data structure used to
speed up data retrieval.

Example:

CREATE INDEX idx_products_category
ON products(category);

The table data does not change.

The database maintains an additional structure
to find matching rows faster.
*/


/*
==========================================================
9. CHECK INDEXES
==========================================================

SQLite command:

.indexes products

This shows indexes associated with the table.
*/


/*
==========================================================
10. EXPLAIN QUERY PLAN
==========================================================

Used to understand how the database plans to execute
a query.

Example:

EXPLAIN QUERY PLAN
SELECT *
FROM products
WHERE category = 'electronics';

If an index is being used, SQLite may show:

SEARCH products USING INDEX ...
*/


/*
==========================================================
11. COMPOSITE INDEX
==========================================================

An index created on multiple columns.

Example:

CREATE INDEX idx_products_category_price
ON products(category, price);

This index is ordered by:

category
    ↓
price


Leftmost-prefix rule:

(category)
    → can use the index

(category, price)
    → can use the index

(price)
    → generally cannot efficiently use this index alone
*/


/*
==========================================================
12. WHY NOT INDEX EVERY COLUMN?
==========================================================

Indexes are not free.

Problems with too many indexes:

1. Extra storage is required.

2. INSERT operations become more expensive.

3. UPDATE operations may require index maintenance.

4. DELETE operations may require index maintenance.

5. Low-selectivity columns may provide little benefit.

Therefore:

Create indexes based on actual query patterns.
*/


/*
==========================================================
13. INDEX NAMING CONVENTION
==========================================================

Common convention:

idx_<table>_<column>

Examples:

idx_products_category

idx_products_category_price
*/


/*
==========================================================
14. QUICK REVISION
==========================================================

Normalization
→ Organizes data and reduces redundancy.

1NF
→ Atomic values, no repeating groups.

2NF
→ 1NF + no partial dependency.

3NF
→ 2NF + no transitive dependency.

Index
→ Additional data structure for faster retrieval.

Composite Index
→ Index on multiple columns.

Leftmost-prefix rule
→ For (A, B), A or (A, B) can use the index;
  B alone generally cannot efficiently use it.

EXPLAIN QUERY PLAN
→ Shows how the database plans to execute a query.

Too many indexes
→ More storage + write/maintenance overhead.
*/