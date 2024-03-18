-- Prepares a MySQL server for the testing environment

-- Step 1: Create the test database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Step 2: Create the test user (if it doesn't exist)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Step 3: Grant privileges to the test user
-- Grant all privileges on the hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Step 4: Flush privileges to ensure changes take effect
FLUSH PRIVILEGES;
