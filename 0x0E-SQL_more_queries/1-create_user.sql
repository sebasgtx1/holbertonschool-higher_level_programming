-- Create User
-- Query to create the server user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
