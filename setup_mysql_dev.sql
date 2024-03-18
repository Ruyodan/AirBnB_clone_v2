-- Prepares a MySQL server for the project

-- Step 1: Create the database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Step 2: Create the user (if it doesn't exist)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Step 3: Grant privileges to the user
-- Grant all privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Step 4: Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;
