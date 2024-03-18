-- Get the initial number of records in the states table
SELECT COUNT(*) INTO @initial_count FROM states;

-- Execute the console command to create a new state
INSERT INTO states (name) VALUES ('California');

-- Get the updated number of records in the states table
SELECT COUNT(*) INTO @updated_count FROM states;

-- Check if the difference is +1
SET @difference = @updated_count - @initial_count;
SELECT
  CASE
    WHEN @difference = 1 THEN 'Test passed'
    ELSE 'Test failed'
  END AS 'Test Result';
