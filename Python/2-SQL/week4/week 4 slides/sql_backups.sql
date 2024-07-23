-- docker command for help on backups
docker exec pg_container pg_dump --help

-- create a backup
docker exec pg_container pg_dump --verbose --file moma_dump.sql moma

-- restore from backup (start by creating an empty db)
docker exec pg_container psql -c 'CREATE DATABASE moma_copy;'

-- copy the backup into the new db
docker exec pg_container psql moma_copy -f moma_dump.sql
