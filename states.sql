-- Create a temporary table to store the initial count
CREATE TEMPORARY TABLE temp_state_count (count INT);
INSERT INTO temp_state_count (count) SELECT COUNT(*) FROM states;

-- Execute the console command to create a new state
INSERT INTO states (name) VALUES ('California');

-- Get the updated count of records in the states table
SELECT COUNT(*) INTO @updated_count FROM states;

-- Get the initial count from the temporary table
SELECT count INTO @initial_count FROM temp_state_count;

-- Calculate the difference
SET @difference = @updated_count - @initial_count;

-- Check if the difference is +1
SELECT
  CASE
    WHEN @difference = 1 THEN 'Test passed'
    ELSE 'Test failed'
  END AS 'Test Result';

-- Clean up the temporary table
DROP TEMPORARY TABLE temp_state_count;
