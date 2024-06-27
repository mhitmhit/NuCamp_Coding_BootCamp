-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

-- TODO create more tables here...
-- create supplier table
CREATE TABLE suppliers(
	name TEXT NOT NULL,
	id SERIAL,
	PRIMARY KEY (id)
);


-- create customer table
CREATE TABLE customers(
	id SERIAL,
	customer_name TEXT NOT NULL, -- name TEXT NOT NULL, (naming convention)
	PRIMARY KEY (id)
);


-- create employees table
CREATE TABLE employees(
	id SERIAL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	PRIMARY KEY (id)
);

-- create orders table
CREATE TABLE orders(
	id SERIAL,
	order_date DATE,
	customer_id INT NOT NULL,
	employee_id INT,
	PRIMARY KEY (id)
);


-- create orders products in orders table
CREATE TABLE orders_products(
	product_id INT NOT NULL,
	order_id INT NOT NULL,
	quantity INT NOT NULL,
	discount NUMERIC NOT NULL,
	PRIMARY KEY (product_id, order_id)
);


-- create territories table
CREATE TABLE territories(
	id SERIAL,
	description TEXT NOT NULL,
	PRIMARY KEY (id)
);


-- create employees's territories table
CREATE TABLE employees_territories(
	employee_id INT,
	territory_id INT,
	PRIMARY KEY (employee_id, territory_id)
);


-- create offices table
CREATE TABLE offices(
	id SERIAL,
	address_line TEXT NOT NULL,
	territory_id INT NOT NULL,
	PRIMARY KEY (id)
);

-- create us states table
CREATE TABLE us_states(
	id SERIAL,
	name TEXT NOT NULL,
	abbreviation CHARACTER(2) NOT NULL,
	PRIMARY KEY (id)
);

---
--- Add foreign key constraints
---

-- PRODUCTS

ALTER TABLE products
ADD CONSTRAINT fk_products_categories
FOREIGN KEY (category_id)
REFERENCES categories (id);

-- add foreign key for Order-to-Consumer

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id)
REFERENCES customers (id);

-- add foreign key for Order-to-Employee

ALTER TABLE orders
ADD CONSTRAINT fk_orders_employees
FOREIGN KEY (employee_id)
REFERENCES employees (id);


-- TODO create more constraints here...

-- add foreign key for suppliers and products
ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id)
REFERENCES suppliers (id);


-- add foreign keys to orders-products table

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_orders
FOREIGN KEY (order_id)
REFERENCES orders (id);

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products_products
FOREIGN KEY (product_id)
REFERENCES products (id);


-- add foreign keys to employees-territories table

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_employees
FOREIGN KEY (employee_id)
REFERENCES employees (id);

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_territories
FOREIGN KEY (territory_id)
REFERENCES territories (id);


-- add foreign keys to offices table

ALTER TABLE offices
ADD CONSTRAINT fk_offices_territories
FOREIGN KEY (territory_id)
REFERENCES territories; -- REFERENCES territories(id); (specify the column you want to reference)
