-- Creates a Database and Table in it
-- Query to create a table in a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
