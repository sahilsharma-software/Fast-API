-- DAY 3: Keys, Constraints & Relationships


-- 1. PRIMARY KEY

CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- Test students
INSERT INTO student (id, name, age)
VALUES (1, 'Sahil', 21);

INSERT INTO student (id, name, age)
VALUES (2, 'Aman', 22);

SELECT * FROM student;


-- 2. CONSTRAINTS

CREATE TABLE products2 (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER CHECK(price > 0),
    category TEXT DEFAULT 'GENERAL',
    sku TEXT UNIQUE
);

-- Valid product
INSERT INTO products2 (id, name, price, sku)
VALUES (1, 'Laptop', 100000, 'LP101');

SELECT * FROM products2;


-- 3. FOREIGN KEY

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO customers (id, name)
VALUES (1, 'Sahil');

INSERT INTO customers (id, name)
VALUES (2, 'Aman');


CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Valid orders
INSERT INTO orders (id, product, customer_id)
VALUES (1, 'Laptop', 1);

INSERT INTO orders (id, product, customer_id)
VALUES (2, 'Phone', 2);

SELECT * FROM orders;


-- Enable Foreign Key checking in SQLite
PRAGMA foreign_keys = ON;


-- 4. RELATIONSHIP EXAMPLE
-- Customer → Orders = One-to-Many