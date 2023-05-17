-- This script that creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If user and Database already exist code should still run

database="hbtn_0d_2"
user="user_0d_2"
password="user_0d_2_pwd"

CREATE DATABASE IF NOT EXISTS $database;
CREATE USER IF NOT EXISTS '$user'@'localhost' IDENTIFIED BY '$password'; 
GRANT SELECT ON $database.* TO '$user'@'localhost';"
