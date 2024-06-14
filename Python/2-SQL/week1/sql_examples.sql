CREATE TABLE events (
	show_time TIMESTAMP,
	id SERIAL,
	auditorium_id INT,
	film_id INT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE auditoria (
	id SERIAL,
	capacity INTEGER NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE films (
	id SERIAL,
	title TEXT NOT NULL,
	runtime INTEGER,
	PRIMARY KEY (id)
);

CREATE TABLE accounts (
	id SERIAL,
	username TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	customer_id INT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE customers (
	id SERIAL,
	name TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE event_purchases(
	customer_id INT NOT NULL,
	event_id INT NOT NULL,
	PRIMARY KEY (customer_id, event_id),
	price NUMERIC NOT NULL
);




ALTER TABLE events
ADD CONSTRAINT fk_events_auditoria
FOREIGN KEY (auditorium_id)
REFERENCES auditoria;

ALTER TABLE events
ADD CONSTRAINT fk_events_films
FOREIGN KEY (film_id)
REFERENCES films;

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_customers
FOREIGN KEY (customer_id)
REFERENCES customers;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_events
FOREIGN KEY (event_id)
REFERENCES events;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_customers
FOREIGN KEY (customer_id)
REFERENCES customers;

CREATE TABLE categories (
    id SERIAL,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    category_id INT,
    PRIMARY KEY (id)
);


ALTER TABLE products
ADD CONSTRAINT fk_products_categories   -- constraint name
FOREIGN KEY (category_id)               -- which column in the table to alter
REFERENCES categories;                  -- key from the external table (sql recongines if the column names are the same in both tables,
                                        -- if names are not same use: other_table_name(column_name_from_other_table)
                                        --)
