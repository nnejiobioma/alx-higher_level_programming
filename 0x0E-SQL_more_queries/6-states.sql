-- This script that creates the database hbtn_0d_usa and the 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; 
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL 
    PRIMARY KEY, name VARCHAR(256) NOT NULL 
);