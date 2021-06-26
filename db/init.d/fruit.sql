DROP SCHEMA IF EXISTS test;
CREATE SCHEMA test;
USE test;

DROP TABLE IF EXISTS fruit;
CREATE TABLE fruit(id int auto_increment, name varchar(10), index(id));

INSERT INTO fruit(name) VALUES ('apple'), ('orange'), ('banana');