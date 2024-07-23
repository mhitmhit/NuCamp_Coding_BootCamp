

SELECT * FROM pg_indexes;



SELECT tablename, indexname, indexdef FROM pg_indexes WHERE tablename NOT LIKE 'pg_%';



CREATE INDEX moma_works_btree_index ON moma_works(artist);




DROP INDEX moma_works_btree_index;
CREATE INDEX moma_works_hash_index ON moma_works USING HASH (artist);

EXPLAIN SELECT date_acquired FROM moma_works
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';



EXPLAIN ANALYZE SELECT date_acquired FROM moma_works
WHERE date_acquired BETWEEN '1950-01-01' AND '1959-12-31';
