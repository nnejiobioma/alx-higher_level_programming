-- This script creates a user user_0d_1
-- Grants all privillages
-- Users IDENTIFIED BY 
-- Still runs even if the user name already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
