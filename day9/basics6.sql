/*
==========================================================
DAY 6 — SQLITE & POSTGRESQL
==========================================================

Topics:
1. SQLite
2. PostgreSQL
3. SQLite vs PostgreSQL
4. PostgreSQL Architecture
5. psql
6. PostgreSQL CRUD
7. Identity Columns
8. PostgreSQL Data Types
9. psql Meta-Commands
*/


/*
==========================================================
1. SQLITE
==========================================================

SQLite is a lightweight, file-based relational database.

Characteristics:

- Database is stored in a file.
- No separate database server is required.
- Easy to set up.
- Good for learning, local applications and small projects.

Example:

learning.db
    ↓
Tables
    ↓
Rows
*/


/*
==========================================================
2. POSTGRESQL
==========================================================

PostgreSQL is a client-server relational database.

Characteristics:

- Requires a running database server.
- Supports multiple concurrent clients.
- Strong SQL and transaction support.
- Provides many advanced database features.
- Commonly used for backend and production applications.

Architecture:

Application
    ↓
Database Client / Driver
    ↓
PostgreSQL Server
    ↓
Database
    ↓
Schema
    ↓
Tables
    ↓
Rows
*/


/*
==========================================================
3. SQLITE vs POSTGRESQL
==========================================================

SQLite:
- File-based
- No separate server
- Lightweight
- Simple setup
- Good for local/small applications

PostgreSQL:
- Client-server database
- Requires a database server
- Supports many concurrent clients
- Rich SQL and advanced features
- Suitable for production backend systems
*/


/*
==========================================================
4. POSTGRESQL HIERARCHY
==========================================================

PostgreSQL Server
        ↓
     Database
        ↓
      Schema
        ↓
      Tables
        ↓
       Rows

Default schema:
public


Example:

PostgreSQL Server
    ↓
company_db
    ↓
public
    ↓
products
    ↓
rows
*/


/*
==========================================================
5. psql
==========================================================

psql is the PostgreSQL command-line client.

It allows us to:

- Connect to PostgreSQL
- Execute SQL queries
- Manage databases and tables
- Inspect database structures

psql is NOT the database itself.

PostgreSQL → Database system
psql       → Command-line client
*/


/*
==========================================================
6. IMPORTANT psql META-COMMANDS
==========================================================

These are psql commands, NOT standard SQL.

\l
→ List databases

\c database_name
→ Connect to a database

\dt
→ List tables

\d table_name
→ Describe table structure

\q
→ Quit psql
*/


/*
==========================================================
7. CREATE DATABASE
==========================================================
*/

CREATE DATABASE company_db;


/*
Connect to database using psql:

\c company_db
*/


/*
==========================================================
8. CREATE TABLE IN POSTGRESQL
==========================================================
*/

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INTEGER CHECK (price > 0),
    category VARCHAR(50)
);


/*
==========================================================
9. INSERT DATA
==========================================================
*/

INSERT INTO products (id, name, price, category)
VALUES
(1, 'laptop', 100000, 'electronics'),
(2, 'MOBILE', 120000, 'electronics'),
(3, 'KAWASAKI', 2300000, 'MOTOR');


/*
==========================================================
10. SELECT
==========================================================
*/

SELECT *
FROM products;


/*
==========================================================
11. UPDATE
==========================================================
*/

UPDATE products
SET price = 120000
WHERE id = 2;


/*
==========================================================
12. DELETE
==========================================================
*/

DELETE FROM products
WHERE id = 3;


/*
==========================================================
13. POSTGRESQL CONSTRAINTS
==========================================================

PRIMARY KEY
→ Uniquely identifies each row.

NOT NULL
→ Value is required.

CHECK
→ Restricts values based on a condition.

Example:

price INTEGER CHECK (price > 0)
*/


/*
==========================================================
14. ALTER TABLE
==========================================================

ALTER TABLE modifies an existing table structure.

Example:

ADD COLUMN:

ALTER TABLE products
ADD COLUMN brand TEXT;

Without a DEFAULT value, existing rows get NULL
for the new column.
*/


/*
==========================================================
15. IDENTITY COLUMN
==========================================================

PostgreSQL can automatically generate IDs using
IDENTITY columns.

Modern syntax:

id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY

Example:
*/

CREATE TABLE customers (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


/*
Now ID does not need to be provided manually.

Example:

INSERT INTO customers (name)
VALUES ('Sahil');

INSERT INTO customers (name)
VALUES ('Aman');

The database generates the IDs.
*/


/*
==========================================================
16. SQLITE vs POSTGRESQL — ID GENERATION
==========================================================

SQLite:

id INTEGER PRIMARY KEY

→ Can automatically generate IDs.

PostgreSQL:

id INTEGER PRIMARY KEY

→ Does NOT automatically generate IDs by itself.

For automatic generation:

id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY


Important distinction:

PRIMARY KEY
→ Uniqueness + NOT NULL

IDENTITY
→ Automatic ID generation
*/


/*
==========================================================
17. COMMON POSTGRESQL DATA TYPES
==========================================================

INTEGER
→ Whole numbers

NUMERIC
→ Exact decimal numbers

VARCHAR(n)
→ String with maximum length n

TEXT
→ Text/string

BOOLEAN
→ TRUE / FALSE

DATE
→ Date

TIMESTAMP
→ Date + time
*/


/*
==========================================================
18. DATA TYPE EXAMPLE
==========================================================
*/

CREATE TABLE user_profile (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    bio TEXT,
    age INTEGER,
    is_active BOOLEAN,
    birth_date DATE,
    created_at TIMESTAMP
);


/*
Example:

INSERT INTO user_profile
(username, bio, age, is_active, birth_date, created_at)
VALUES
(
    'Sahil',
    'CSE student',
    21,
    TRUE,
    '2004-05-15',
    CURRENT_TIMESTAMP
);
*/


/*
==========================================================
19. CURRENT_TIMESTAMP
==========================================================

CURRENT_TIMESTAMP
→ Returns the current date and time.

Common backend use:

created_at
updated_at
*/


/*
==========================================================
20. INTERVIEW — WHEN TO USE POSTGRESQL?
==========================================================

For a production FastAPI backend with many concurrent
users, PostgreSQL is generally preferred because:

- It is a client-server database.
- It supports concurrent clients.
- It provides strong transaction support.
- It has rich SQL and advanced database features.
- It is suitable for production backend applications.

Do not choose PostgreSQL only because of automatic
ID generation; SQLite can also generate IDs.
*/


/*
==========================================================
21. QUICK REVISION
==========================================================

SQLite
→ File-based relational database.

PostgreSQL
→ Client-server relational database.

PostgreSQL hierarchy:

Server
  ↓
Database
  ↓
Schema
  ↓
Table
  ↓
Rows

psql
→ PostgreSQL command-line client.

public
→ Default PostgreSQL schema.

\l
→ List databases.

\c
→ Connect to database.

\dt
→ List tables.

\d
→ Describe table.

Identity
→ Automatically generates IDs.

PRIMARY KEY
→ Uniquely identifies rows.

INTEGER
→ Whole numbers.

NUMERIC
→ Exact decimal values.

VARCHAR
→ Limited-length text.

TEXT
→ Text.

BOOLEAN
→ TRUE/FALSE.

DATE
→ Date.

TIMESTAMP
→ Date + time.
*/