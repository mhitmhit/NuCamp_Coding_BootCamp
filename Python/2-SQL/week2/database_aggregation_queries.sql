SELECT * FROM books;

SELECT COUNT(*) FROM books; -- number of rows in the table

SELECT MAX(year) FROM books; -- returns the max year in year column

SELECT genre, COUNT(*) AS ct FROM books GROUP BY genre;-- counts number in each genre

SELECT genre, COUNT(*) AS ct FROM books GROUP BY genre HAVING COUNT(*) > 1;

SELECT customer_id, MIN(order_date) FROM orders
GROUP BY customer_id
ORDER BY customer_id;

select customer_id, AVG(freight) AS af from orders
GROUP BY customer_id
ORDER BY af
;

SELECT * from order_details;

SELECT order_id, COUNT(*) AS product_count from order_details
GROUP BY order_id
HAVING COUNT(*) > 4
ORDER BY product_count DESC
;

SELECT o.order_id, count(DISTINCT product_id) AS product_count
FROM order_details o
GROUP BY order_id HAVING(count(*)) >= 5
ORDER BY product_count DESC;
